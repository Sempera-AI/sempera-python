"""The Sempera Python SDK. Quick start: https://api.sempera.org/docs/sdks.md."""

from ._generated import API_VERSION, DEFAULT_BASE_URL, ERROR_CODES, OPERATIONS, Operations
from ._runtime import (
    AuthenticationError,
    ConflictError,
    ConnectionFailure,
    IdempotencyKeyReusedError,
    NotFoundError,
    PermissionDeniedError,
    RateLimitError,
    SemperaError,
    ServerError,
    ValidationError,
    paginate,
)
from .webhooks import WebhookSignatureError, construct_event, verify_signature


class Sempera(Operations):
    """`Sempera(api_key)` then `client.list_agents()`; one method per operation, named in snake_case."""


__all__ = [
    "API_VERSION", "DEFAULT_BASE_URL", "ERROR_CODES", "OPERATIONS", "Sempera", "paginate",
    "SemperaError", "ValidationError", "AuthenticationError", "PermissionDeniedError", "NotFoundError",
    "ConflictError", "IdempotencyKeyReusedError", "RateLimitError", "ServerError", "ConnectionFailure",
    "WebhookSignatureError", "construct_event", "verify_signature",
]
