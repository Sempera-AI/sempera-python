"""The hand-written core of the Sempera Python SDK: authentication, errors, retries, idempotency, paging.

Standard library only. The per-operation methods are generated in `_generated.py`.
"""

from __future__ import annotations

import json
import os
import random
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from typing import Any, Callable, Iterator, Mapping

DEFAULT_BASE_URL = "https://api.sempera.org"
SDK_VERSION = "0.1.0"

# (method, url, headers, body, timeout seconds) -> (status, response headers, response bytes)
Transport = Callable[[str, str, Mapping[str, str], "bytes | None", float], "tuple[int, Mapping[str, str], bytes]"]


class SemperaError(Exception):
    """Any non-2xx answer. `code` is the stable machine-readable code; branch on `code` or `reason`, never on `message`."""

    def __init__(self, status: int, code: str, message: str, *, request_id: str | None = None,
                 reason: str | None = None, field: str | None = None, headers: Mapping[str, str] | None = None,
                 body: Any = None) -> None:
        super().__init__(f"{status} {code}: {message}")
        self.status, self.code, self.message = status, code, message
        self.request_id, self.reason, self.field = request_id, reason, field
        self.headers, self.body = dict(headers or {}), body


class ValidationError(SemperaError): """400: a field is missing or wrong."""
class AuthenticationError(SemperaError): """401: no credential, or an unknown, expired or revoked key."""
class PermissionDeniedError(SemperaError): """403: the key lacks the scope, or the role cannot do this."""
class NotFoundError(SemperaError): """404: no such resource in your scope."""
class ConflictError(SemperaError): """409: a rule refused the request."""
class IdempotencyKeyReusedError(ConflictError): """409 idempotency_key_reused: the same key was sent with a different request."""
class RateLimitError(SemperaError):
    """429: wait `retry_after` seconds."""
    retry_after: float | None = None
class ServerError(SemperaError): """5xx: the API or a provider behind it failed. Quote `request_id` to support."""
class ConnectionFailure(SemperaError):
    """No answer: DNS, TCP, TLS or a timeout. `status` is 0."""


def _error_for(status: int, headers: Mapping[str, str], payload: Any) -> SemperaError:
    envelope = payload.get("error") if isinstance(payload, dict) and isinstance(payload.get("error"), dict) else {}
    code = str(envelope.get("code") or (payload.get("code") if isinstance(payload, dict) else None) or f"http_{status}")
    message = str(envelope.get("message") or (payload.get("message") if isinstance(payload, dict) else None) or f"HTTP {status}")
    kwargs = dict(request_id=envelope.get("request_id") or headers.get("x-request-id"), reason=envelope.get("reason"),
                  field=envelope.get("field"), headers=headers, body=payload)
    if code == "idempotency_key_reused":
        cls: type[SemperaError] = IdempotencyKeyReusedError
    else:
        cls = {400: ValidationError, 401: AuthenticationError, 403: PermissionDeniedError, 404: NotFoundError,
               409: ConflictError, 429: RateLimitError}.get(status, ServerError if status >= 500 else SemperaError)
    error = cls(status, code, message, **kwargs)
    if isinstance(error, RateLimitError):
        error.retry_after = _retry_after(headers)
    return error


def _retry_after(headers: Mapping[str, str]) -> float | None:
    try:
        return max(0.0, float(headers.get("retry-after", "")))
    except ValueError:
        return None


def _urllib_transport(method: str, url: str, headers: Mapping[str, str], body: bytes | None,
                      timeout: float) -> tuple[int, Mapping[str, str], bytes]:
    request = urllib.request.Request(url, data=body, method=method, headers=dict(headers))
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:  # noqa: S310 - https base URL
            return response.status, {k.lower(): v for k, v in response.headers.items()}, response.read()
    except urllib.error.HTTPError as exc:
        return exc.code, {k.lower(): v for k, v in exc.headers.items()}, exc.read()


def _multipart(fields: Mapping[str, Any]) -> tuple[bytes, str]:
    """Encode `{name: text}` or `{name: (filename, bytes, content_type)}`."""
    boundary = "sempera-" + uuid.uuid4().hex
    chunks: list[bytes] = []
    for name, value in fields.items():
        chunks.append(f"--{boundary}\r\n".encode())
        if isinstance(value, tuple):
            filename, data, ctype = value
            chunks.append(f'Content-Disposition: form-data; name="{name}"; filename="{filename}"\r\n'
                          f"Content-Type: {ctype}\r\n\r\n".encode() + data + b"\r\n")
        else:
            chunks.append(f'Content-Disposition: form-data; name="{name}"\r\n\r\n{value}\r\n'.encode())
    chunks.append(f"--{boundary}--\r\n".encode())
    return b"".join(chunks), f"multipart/form-data; boundary={boundary}"


class SemperaCore:
    """Sends requests. `Sempera` (in `sempera/__init__.py`) adds one method per operation."""

    def __init__(self, api_key: str | None = None, *, base_url: str | None = None, max_retries: int = 2,
                 timeout: float = 60.0, transport: Transport | None = None,
                 sleep: Callable[[float], None] = time.sleep, headers: Mapping[str, str] | None = None) -> None:
        self.api_key = api_key if api_key is not None else os.environ.get("SEMPERA_API_KEY")
        self.base_url = (base_url or os.environ.get("SEMPERA_BASE_URL") or DEFAULT_BASE_URL).rstrip("/")
        self.max_retries, self.timeout = max_retries, timeout
        self._transport, self._sleep = transport or _urllib_transport, sleep
        self._headers = dict(headers or {})

    def _url(self, op: Mapping[str, Any], params: Mapping[str, Any]) -> str:
        path = op["path"]
        for name in op["path_params"]:
            if params.get(name) is None:
                raise TypeError(f"missing path parameter {name!r}")
            path = path.replace("{" + name + "}", urllib.parse.quote(str(params[name]), safe=""))
        query = [(n, _query_value(params[n])) for n in op["query"] if params.get(n) is not None]
        return self.base_url + path + ("?" + urllib.parse.urlencode(query) if query else "")

    def _call(self, op: Mapping[str, Any], params: Mapping[str, Any], body: Any, idempotency_key: str | None,
              request_options: Mapping[str, Any] | None) -> Any:
        options = dict(request_options or {})
        headers = {"Accept": "application/json", "User-Agent": f"sempera-python/{SDK_VERSION}", **self._headers,
                   **options.get("headers", {})}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        payload: bytes | None = None
        if body is not None:
            if op["body"] == "multipart":
                payload, headers["Content-Type"] = _multipart(body)
            else:
                payload, headers["Content-Type"] = json.dumps(body).encode(), "application/json"
        # One key per logical request, reused by every retry, so a retry can never act twice.
        if op["idempotent"]:
            headers["Idempotency-Key"] = idempotency_key or uuid.uuid4().hex
        url = self._url(op, params)
        retries = options.get("max_retries", self.max_retries)
        safe = op["method"] == "GET" or "Idempotency-Key" in headers
        attempt = 0
        while True:
            try:
                status, rheaders, raw = self._transport(op["method"], url, headers, payload, options.get("timeout", self.timeout))
            except (urllib.error.URLError, TimeoutError, ConnectionError, OSError) as exc:
                if attempt < retries and safe:
                    self._sleep(self._delay(attempt, None))
                    attempt += 1
                    continue
                raise ConnectionFailure(0, "connection_failed", str(exc)) from exc
            rheaders = {k.lower(): v for k, v in rheaders.items()}
            if status < 400:
                return self._decode(op, rheaders, raw)
            error = _error_for(status, rheaders, _json_or_none(raw))
            retryable = status in (429, 502, 504) or (status == 503 and error.code == "service_unavailable")
            if retryable and attempt < retries and (status == 429 or safe):
                self._sleep(self._delay(attempt, _retry_after(rheaders)))
                attempt += 1
                continue
            raise error

    @staticmethod
    def _delay(attempt: int, retry_after: float | None) -> float:
        if retry_after is not None:
            return min(retry_after, 60.0)
        return min(8.0, 0.5 * 2 ** attempt) * (0.5 + random.random() / 2)

    @staticmethod
    def _decode(op: Mapping[str, Any], headers: Mapping[str, str], raw: bytes) -> Any:
        if op["response"] == "none" or not raw:
            return None
        if op["response"] == "text":
            return raw.decode("utf-8")
        return json.loads(raw)


def _query_value(value: Any) -> str:
    return ("true" if value else "false") if isinstance(value, bool) else str(value)


def _json_or_none(raw: bytes) -> Any:
    try:
        return json.loads(raw)
    except ValueError:
        return None


def paginate(fetch_page: Callable[[str | None], Mapping[str, Any]]) -> Iterator[Any]:
    """Yield every item of a cursor-paged list, following `next_cursor` until `has_more` is false.

    `fetch_page` receives the cursor (None for the first page) and returns one list response::

        for agent in paginate(lambda cursor: client.list_agents(limit=100, cursor=cursor)):
            ...

    Compatibility routes keep their own envelopes (`tools`, `voices`, ...); this helper follows the native
    `{"object": "list", "data": [...], "has_more", "next_cursor"}` envelope only, and raises on anything else.
    """
    cursor: str | None = None
    while True:
        page = fetch_page(cursor)
        if not isinstance(page, Mapping) or not isinstance(page.get("data"), list):
            raise ValueError("paginate() needs a native list response with a `data` array")
        yield from page["data"]
        cursor = page.get("next_cursor")
        if not page.get("has_more") or not cursor:
            return
