"""Tests for the Sempera Python SDK. The HTTP layer is a scripted fake: no network, no key."""

import hashlib
import hmac
import json
import os
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import sempera  # noqa: E402

# A published known answer: the signature the server produces for these exact inputs.
SECRET = "whsec_vector_0123456789"
STAMP = 1790000000
BODY = ('{"created_at":"2026-09-28T12:00:00+00:00","data":{"actor":"vector","endpoint_id":"22222222-2222-4222-8222-222222222222"},'
        '"id":"evt_00000000000000000000000000000001","object":"event","type":"webhook.test","workspace_id":"11111111-1111-4111-8111-111111111111"}')
SIGNATURE = f"t={STAMP},v1=1f4226699ca9fa61b71fbb57dbd2f57efa6788488437ee2e411ea4e3002be3c1"


class Script:
    """Returns the queued answers in order and records every request."""

    def __init__(self, *answers):
        self.answers, self.calls, self.waits = list(answers), [], []

    def __call__(self, method, url, headers, body, timeout):
        self.calls.append({"method": method, "url": url, "headers": dict(headers), "body": body})
        answer = self.answers.pop(0)
        if isinstance(answer, Exception):
            raise answer
        return answer

    def client(self, **kw):
        return sempera.Sempera("sempera_sk_test", transport=self, sleep=self.waits.append, **kw)


def reply(status, body=None, **headers):
    return status, headers, json.dumps(body).encode() if body is not None else b""


def sent(call):
    return json.loads(call["body"])


class RequestShapeTests(unittest.TestCase):
    def test_sends_the_bearer_key_and_builds_path_and_query(self):
        s = Script(reply(200, {"id": "ses_1"}))
        out = s.client().get_session("a b/c", agent_id="agt_1")
        self.assertEqual(out, {"id": "ses_1"})
        call = s.calls[0]
        self.assertEqual(call["url"], "https://api.sempera.org/v1/sessions/a%20b%2Fc?agent_id=agt_1")
        self.assertEqual(call["headers"]["Authorization"], "Bearer sempera_sk_test")

    def test_the_key_defaults_to_the_environment(self):
        os.environ["SEMPERA_API_KEY"] = "sempera_sk_env"
        try:
            s = Script(reply(200, {}))
            sempera.Sempera(transport=s).get_me()
        finally:
            del os.environ["SEMPERA_API_KEY"]
        self.assertEqual(s.calls[0]["headers"]["Authorization"], "Bearer sempera_sk_env")

    def test_a_missing_path_parameter_is_refused_before_any_request(self):
        s = Script()
        with self.assertRaises(TypeError):
            s.client()._call(sempera.OPERATIONS["get_session"], {}, None, None, None)
        self.assertEqual(s.calls, [])


class ResourceTests(unittest.TestCase):
    def test_agents_list_and_get(self):
        s = Script(reply(200, {"object": "list", "data": [{"id": "agt_1"}], "has_more": False}), reply(200, {"id": "agt_1"}))
        c = s.client()
        self.assertEqual(c.list_agents(limit=5)["data"][0]["id"], "agt_1")
        self.assertEqual(c.get_agent("agt_1")["id"], "agt_1")
        self.assertEqual([x["method"] for x in s.calls], ["GET", "GET"])
        self.assertTrue(s.calls[0]["url"].endswith("/v1/agents?limit=5"))
        self.assertTrue(s.calls[1]["url"].endswith("/v1/agents/agt_1"))

    def test_calls_create_get_and_list(self):
        s = Script(reply(201, {"id": "call_1"}), reply(200, {"id": "call_1"}), reply(200, {"object": "list", "data": [], "has_more": False}))
        c = s.client()
        c.create_call({"agent_id": "agt_1", "mode": "prompt", "consent_basis": "asked"}, idempotency_key="k-1")
        c.get_call("call_1")
        c.list_calls(agent_id="agt_1", limit=10)
        create = s.calls[0]
        self.assertEqual((create["method"], create["url"]), ("POST", "https://api.sempera.org/v1/calls"))
        self.assertEqual(create["headers"]["Idempotency-Key"], "k-1")
        self.assertEqual(create["headers"]["Content-Type"], "application/json")
        self.assertEqual(sent(create)["mode"], "prompt")
        self.assertTrue(s.calls[1]["url"].endswith("/v1/calls/call_1"))
        self.assertIn("agent_id=agt_1", s.calls[2]["url"])

    def test_conversations(self):
        s = Script(reply(200, {"data": []}), reply(200, {"id": "conv_1"}))
        c = s.client()
        c.messaging_conversations("agt_1", "sms")
        c.messaging_conversation("agt_1", "sms", "conv_1")
        self.assertTrue(s.calls[0]["url"].endswith("/v1/agents/agt_1/messaging/sms/conversations"))
        self.assertTrue(s.calls[1]["url"].endswith("/v1/agents/agt_1/messaging/sms/conversations/conv_1"))

    def test_phone_numbers(self):
        s = Script(reply(200, {"object": "list", "data": [{"number": "+14155550100"}], "has_more": False}))
        out = s.client().list_phone_numbers(agent_id="agt_1")
        self.assertEqual(out["data"][0]["number"], "+14155550100")
        self.assertTrue(s.calls[0]["url"].endswith("/v1/phone-numbers?agent_id=agt_1"))

    def test_sms_send_carries_its_body_and_an_idempotency_key(self):
        s = Script(reply(201, {"data": {"status": "sent"}}))
        message = {"agent_id": "agt_1", "agent_number": "+14155550100", "user_number": "+14155550123",
                   "agent_message": "Confirmed.", "consent_basis": "asked"}
        s.client().send_sms(message)
        call = s.calls[0]
        self.assertEqual((call["method"], call["url"]), ("POST", "https://api.sempera.org/v1/sms/send"))
        self.assertEqual(sent(call), message)
        self.assertTrue(call["headers"]["Idempotency-Key"])

    def test_knowledge_sources(self):
        s = Script(reply(200, {"object": "list", "data": [], "has_more": False}), reply(201, {"id": "ks_1"}))
        c = s.client()
        c.list_knowledge_sources(agent_id="agt_1")
        c.create_text_knowledge_source({"agent_id": "agt_1", "name": "Hours", "content": "9 to 5"})
        self.assertTrue(s.calls[0]["url"].endswith("/v1/knowledge-sources?agent_id=agt_1"))
        self.assertTrue(s.calls[1]["url"].endswith("/v1/knowledge-sources/text"))
        self.assertEqual(sent(s.calls[1])["name"], "Hours")


class ErrorTests(unittest.TestCase):
    def test_error_envelopes_become_typed_errors(self):
        cases = [(400, sempera.ValidationError), (401, sempera.AuthenticationError), (403, sempera.PermissionDeniedError),
                 (404, sempera.NotFoundError), (409, sempera.ConflictError)]
        for status, cls in cases:
            with self.subTest(status=status):
                s = Script(reply(status, {"error": {"code": "some_code", "message": "no", "request_id": "req_1", "reason": "why", "field": "f"}}))
                with self.assertRaises(cls) as ctx:
                    s.client().get_agent("agt_1")
                err = ctx.exception
                self.assertEqual((err.status, err.code, err.request_id, err.reason, err.field), (status, "some_code", "req_1", "why", "f"))
                self.assertIsInstance(err, sempera.SemperaError)

    def test_a_reused_idempotency_key_has_its_own_class(self):
        s = Script(reply(409, {"error": {"code": "idempotency_key_reused", "message": "no"}}))
        with self.assertRaises(sempera.IdempotencyKeyReusedError):
            s.client().create_call({"agent_id": "a"}, idempotency_key="k")


class RetryTests(unittest.TestCase):
    def test_a_429_is_retried_after_the_retry_after_wait(self):
        s = Script(reply(429, {"error": {"code": "rate_limited", "message": "slow"}}, **{"retry-after": "2"}), reply(200, {"id": "agt_1"}))
        self.assertEqual(s.client().get_agent("agt_1"), {"id": "agt_1"})
        self.assertEqual(len(s.calls), 2)
        self.assertEqual(s.waits[0], 2)

    def test_a_503_is_retried_and_a_retried_post_keeps_its_key(self):
        err = {"error": {"code": "service_unavailable", "message": "later"}}
        s = Script(reply(503, err), reply(201, {"id": "call_1"}))
        s.client().create_call({"agent_id": "a"})
        keys = {c["headers"]["Idempotency-Key"] for c in s.calls}
        self.assertEqual(len(s.calls), 2)
        self.assertEqual(len(keys), 1)

    def test_retries_stop_at_the_limit(self):
        err = {"error": {"code": "internal", "message": "boom"}}
        s = Script(reply(502, err), reply(502, err), reply(502, err))
        with self.assertRaises(sempera.ServerError):
            s.client().get_agent("agt_1")
        self.assertEqual(len(s.calls), 3)

    def test_a_dropped_connection_is_retried_then_reported(self):
        s = Script(ConnectionResetError("reset"), ConnectionResetError("reset"), ConnectionResetError("reset"))
        with self.assertRaises(sempera.ConnectionFailure):
            s.client().get_agent("agt_1")

    def test_a_validation_error_is_never_retried(self):
        s = Script(reply(400, {"error": {"code": "validation_failed", "message": "bad"}}))
        with self.assertRaises(sempera.ValidationError):
            s.client().get_agent("agt_1")
        self.assertEqual(len(s.calls), 1)


class PaginationTests(unittest.TestCase):
    def test_paginate_follows_the_cursor_until_has_more_is_false(self):
        s = Script(reply(200, {"object": "list", "data": [{"id": 1}, {"id": 2}], "has_more": True, "next_cursor": "c2"}),
                   reply(200, {"object": "list", "data": [{"id": 3}], "has_more": False}))
        c = s.client()
        ids = [a["id"] for a in sempera.paginate(lambda cursor: c.list_agents(limit=2, cursor=cursor))]
        self.assertEqual(ids, [1, 2, 3])
        self.assertIn("cursor=c2", s.calls[1]["url"])

    def test_paginate_refuses_a_response_that_is_not_a_list(self):
        with self.assertRaises(ValueError):
            list(sempera.paginate(lambda cursor: {"not": "a list"}))


class WebhookTests(unittest.TestCase):
    def test_the_published_known_answer_verifies(self):
        sempera.verify_signature(SECRET, BODY, SIGNATURE, now=STAMP + 10)
        sempera.verify_signature(SECRET, BODY.encode(), SIGNATURE, now=STAMP - 10)
        self.assertEqual(sempera.construct_event(SECRET, BODY, SIGNATURE, now=STAMP)["type"], "webhook.test")

    def test_the_scheme_is_hmac_sha256_over_t_dot_body(self):
        expected = hmac.new(SECRET.encode(), f"{STAMP}.{BODY}".encode(), hashlib.sha256).hexdigest()
        self.assertEqual(SIGNATURE.split("v1=")[1], expected)

    def test_a_fresh_signature_made_with_the_documented_recipe_verifies(self):
        body = '{"id":"evt_2","type":"call.completed"}'
        mac = hmac.new(b"whsec_other_0123456789", f"{STAMP}.{body}".encode(), hashlib.sha256).hexdigest()
        self.assertEqual(sempera.construct_event("whsec_other_0123456789", body, f"t={STAMP},v1={mac}", now=STAMP)["id"], "evt_2")

    def test_tampering_wrong_secret_stale_timestamps_and_bad_headers_are_refused(self):
        bad = [(SECRET, BODY + " ", SIGNATURE, STAMP), ("whsec_other", BODY, SIGNATURE, STAMP),
               (SECRET, BODY, SIGNATURE, STAMP + 301), (SECRET, BODY, SIGNATURE, STAMP - 301),
               (SECRET, BODY, SIGNATURE.replace("v1=1f", "v1=2f"), STAMP), (SECRET, BODY, f"t={STAMP},v1=short", STAMP),
               (SECRET, BODY, "", STAMP), (SECRET, BODY, None, STAMP), (SECRET, BODY, "garbage", STAMP),
               (SECRET, BODY, "t=abc," + SIGNATURE.split(",")[1], STAMP)]
        for secret, body, header, now in bad:
            with self.subTest(header=header, now=now), self.assertRaises(sempera.WebhookSignatureError):
                sempera.verify_signature(secret, body, header, now=now)

    def test_five_minutes_exactly_is_inside_the_window_and_the_window_is_configurable(self):
        sempera.verify_signature(SECRET, BODY, SIGNATURE, now=STAMP + 300)
        sempera.verify_signature(SECRET, BODY, SIGNATURE, tolerance=1000, now=STAMP + 900)


if __name__ == "__main__":
    unittest.main()
