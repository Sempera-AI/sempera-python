# sempera

[Documentation](https://docs.sempera.org) | [SDKs](https://docs.sempera.org/sdks) | [OpenAPI document](https://api.sempera.org/openapi.json) | [MIT licence](LICENSE)

The official Python client for the [Sempera](https://sempera.org) API at `https://api.sempera.org`.

* One method for every operation in the public OpenAPI document (`https://api.sempera.org/openapi.json`), generated from it, so the client follows the API.
* A small hand-written core: bearer-key authentication, typed errors, retries with exponential backoff, automatic idempotency keys, cursor paging and webhook signature verification.
* Standard library only. Python 3.9 or newer.

## Install

```bash
pip install sempera
```

## Quick start

Create an API key in the Sempera App and keep it on your server. Pass it to the constructor, or set `SEMPERA_API_KEY` and omit it.

```python
from sempera import Sempera

client = Sempera("sempera_sk_example")   # or Sempera() with SEMPERA_API_KEY set
print(client.get_me())
```

Methods are named after the operation id in the contract, in snake_case (`list_agents`, `create_call`, `send_sms`). Path and query parameters are named exactly as in the contract. A request body is a plain dict, passed first. Answers are plain dicts.

### Agents

```python
from sempera import paginate

page = client.list_agents(limit=20)
for agent in page["data"]:
    print(agent["id"])

# Or follow every page:
for agent in paginate(lambda cursor: client.list_agents(limit=100, cursor=cursor)):
    print(agent["id"])

one = client.get_agent("agt_example")
```

### Calls

```python
call = client.create_call(
    {
        "agent_id": "agt_example",
        "mode": "prompt",
        "phone_number": "+14155550123",
        "task": "Confirm Friday at 3pm. Ask whether that time still suits.",
        "consent_basis": "This person asked us to call them about Friday.",
    },
    idempotency_key="friday-3pm-ada",
)

same = client.get_call(call["id"])
recent = client.list_calls(agent_id="agt_example", limit=10)
```

### Phone numbers and text messages

```python
numbers = client.list_phone_numbers(agent_id="agt_example")

client.send_sms({
    "agent_id": "agt_example",
    "agent_number": "+14155550100",
    "user_number": "+14155550123",
    "agent_message": "Your table is confirmed for Friday at 3pm.",
    "consent_basis": "This person asked us to text them a confirmation.",
})
```

### Conversations

```python
threads = client.messaging_conversations("agt_example", "sms")
thread = client.messaging_conversation("agt_example", "sms", "conv_example")
```

### Knowledge sources

```python
sources = client.list_knowledge_sources(agent_id="agt_example")
client.create_text_knowledge_source({
    "agent_id": "agt_example",
    "name": "Opening hours",
    "content": "Open 9 to 5, Monday to Friday.",
})
```

### Webhooks

Verify every delivery against the raw request body before you parse it. The helper checks the `X-Sempera-Signature` header (`t=<unix seconds>,v1=<hex HMAC-SHA256 over "<t>." + body>`) in constant time and rejects a timestamp more than 300 seconds from your clock. Answer `400` and process nothing when it raises.

```python
from sempera import WebhookSignatureError, construct_event

def handle(raw_body: bytes, signature_header: str) -> int:
    try:
        event = construct_event("whsec_example", raw_body, signature_header)
    except WebhookSignatureError:
        return 400
    print(event["type"], event["id"])
    return 200
```

## Errors

Every refusal raises a typed error carrying `status`, the stable `code`, an optional `reason` and `field`, and the `request_id` to quote to support. Branch on `code` or `reason`, never on the message.

```python
from sempera import NotFoundError, RateLimitError, SemperaError

try:
    client.get_agent("agt_missing")
except NotFoundError as err:
    print(err.code, err.request_id)
except RateLimitError as err:
    print("retry in", err.retry_after)
except SemperaError as err:
    print(err.status, err.code, err.reason)
```

Classes: `ValidationError` (400), `AuthenticationError` (401), `PermissionDeniedError` (403), `NotFoundError` (404), `ConflictError` (409), `IdempotencyKeyReusedError` (409), `RateLimitError` (429), `ServerError` (5xx) and `ConnectionFailure` (no answer).

## Retries and idempotency

The client retries a `429`, a `502`, a `504`, a `503` with code `service_unavailable` and a dropped connection, two times by default, with exponential backoff and jitter, waiting the `Retry-After` it is sent. Change the count with `max_retries` on the client or on one call. A write is retried only when it carries an idempotency key (generated for you, and reused by every retry) or after a `429`. Pass your own `idempotency_key` to make a retry safe across process restarts.

## Develop

```bash
python -m unittest discover -s tests
```

The tests replace the HTTP layer with a scripted fake, so they need no network and no key.

## Licence

MIT. Copyright Sempera Labs, Inc.
