"""Verify the `X-Sempera-Signature` header on a webhook delivery.

The header is ``t=<unix seconds>,v1=<lowercase hex HMAC-SHA256>``, the HMAC keyed with your endpoint secret
over ``"<t>." + raw_body``. Verify against the exact bytes received, before parsing the JSON.
"""

from __future__ import annotations

import hashlib
import hmac
import json
import time
from typing import Any

HEADER = "X-Sempera-Signature"
DEFAULT_TOLERANCE_SECONDS = 300


class WebhookSignatureError(Exception):
    """The delivery is not provably from Sempera, or is too old. Answer 400 and do not process it."""


def verify_signature(secret: str, body: bytes | str, header: str | None, *, tolerance: int = DEFAULT_TOLERANCE_SECONDS,
                     now: float | None = None) -> None:
    """Raise `WebhookSignatureError` unless the signature is valid and within `tolerance` seconds of now."""
    if not header:
        raise WebhookSignatureError(f"missing {HEADER} header")
    raw = body.encode("utf-8") if isinstance(body, str) else bytes(body)
    parts: dict[str, str] = {}
    for piece in header.split(","):
        key, sep, value = piece.strip().partition("=")
        if sep:
            parts.setdefault(key, value)
    try:
        stamp, supplied = int(parts["t"]), parts["v1"]
    except (KeyError, ValueError):
        raise WebhookSignatureError(f"malformed {HEADER} header") from None
    if abs((time.time() if now is None else now) - stamp) > tolerance:
        raise WebhookSignatureError("timestamp outside the tolerance window")
    expected = hmac.new(secret.encode("utf-8"), f"{stamp}.".encode() + raw, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected, supplied):
        raise WebhookSignatureError("signature mismatch")


def construct_event(secret: str, body: bytes | str, header: str | None, *, tolerance: int = DEFAULT_TOLERANCE_SECONDS,
                    now: float | None = None) -> dict[str, Any]:
    """Verify, then parse. Drop an event whose `id` (also `X-Sempera-Event-Id`) you have already processed."""
    verify_signature(secret, body, header, tolerance=tolerance, now=now)
    return json.loads(body)
