"""GENERATED from the live Sempera OpenAPI document. Do not edit by hand; it is rewritten when the API changes.
spec sha256 407e1e6661535ba651988eb9896c1ddf3f1250c492a0374bb6460ec8728d975f
"""

from __future__ import annotations

from typing import Any

from ._runtime import SemperaCore

DEFAULT_BASE_URL = "https://api.sempera.org"
API_VERSION = "1.0.0"
ERROR_CODES = ('AGENT_ENV_UNPINNED', 'CALL_RL_PLAN_ALLOWANCE', 'CALL_RL_PLAN_CONCURRENCY', 'CALL_RL_PLAN_DAILY', 'CALL_RL_PLAN_DAILY_MINUTES', 'CALL_RL_PLAN_HOURLY', 'PHONE_AGENT_UNPINNED', 'PHONE_APPROVAL_EXPIRED', 'PHONE_APPROVAL_INVALID', 'PHONE_APPROVAL_REQUIRED', 'PHONE_COST_UNKNOWN', 'PHONE_DESTINATION_BLOCKED', 'PHONE_FUNDING_NOT_LIVE', 'PHONE_NUMBER_MISSING', 'PHONE_OUTSIDE_HOURS', 'PHONE_PLAN_INACTIVE', 'PHONE_RECIPIENT_OPTED_OUT', 'SMS_RL_PLAN_ALLOWANCE', 'SMS_RL_PLAN_DAILY', 'SMS_RL_PLAN_HOURLY', 'authentication_required', 'capability_unavailable', 'conflict', 'credits_exhausted', 'credits_unavailable', 'csrf_failed', 'forbidden', 'gone', 'idempotency_key_reused', 'insufficient_scope', 'internal_error', 'invalid_credential', 'method_not_allowed', 'not_found', 'owner_setup_required', 'payload_too_large', 'provider_failed', 'provider_timeout', 'rate_limited', 'service_unavailable', 'validation_failed', 'workspace_suspended')

OPERATIONS: dict[str, dict[str, Any]] = {
    'get_doc_page': {'method': 'GET', 'path': '/docs/{page}', 'path_params': ['page'], 'query': [], 'idempotent': False, 'body': None, 'response': 'text'},
    'get_llms_txt': {'method': 'GET', 'path': '/llms.txt', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'text'},
    'get_open_api': {'method': 'GET', 'path': '/openapi.json', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'get_robots_txt': {'method': 'GET', 'path': '/robots.txt', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'text'},
    'get_root': {'method': 'GET', 'path': '/v1', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_list_agent_testing_scenarios': {'method': 'GET', 'path': '/v1/agent-testing/scenarios', 'path_params': [], 'query': ['limit', 'cursor'], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_list_scenario_eval_agents': {'method': 'GET', 'path': '/v1/agent-testing/scenarios/{uuid}/eval-agents', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'start_tornado_run': {'method': 'POST', 'path': '/v1/agent-testing/tornado', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'get_tornado_run': {'method': 'GET', 'path': '/v1/agent-testing/tornado/{run_id}', 'path_params': ['run_id'], 'query': ['agent_id'], 'idempotent': False, 'body': None, 'response': 'json'},
    'list_agents': {'method': 'GET', 'path': '/v1/agents', 'path_params': [], 'query': ['status', 'limit', 'cursor'], 'idempotent': False, 'body': None, 'response': 'json'},
    'create_agent': {'method': 'POST', 'path': '/v1/agents', 'path_params': [], 'query': [], 'idempotent': True, 'body': 'json', 'response': 'json'},
    'get_agent': {'method': 'GET', 'path': '/v1/agents/{agent_id}', 'path_params': ['agent_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'delete_agent': {'method': 'DELETE', 'path': '/v1/agents/{agent_id}', 'path_params': ['agent_id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'archive_agent': {'method': 'POST', 'path': '/v1/agents/{agent_id}/archive', 'path_params': ['agent_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'get_api_chat_channel': {'method': 'GET', 'path': '/v1/agents/{agent_id}/channels/api-chat', 'path_params': ['agent_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'update_api_chat_channel': {'method': 'PATCH', 'path': '/v1/agents/{agent_id}/channels/api-chat', 'path_params': ['agent_id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'send_api_chat_message': {'method': 'POST', 'path': '/v1/agents/{agent_id}/chat', 'path_params': ['agent_id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'list_agent_deployments': {'method': 'GET', 'path': '/v1/agents/{agent_id}/deployments', 'path_params': ['agent_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'list_dialing_pools': {'method': 'GET', 'path': '/v1/agents/{agent_id}/dialing-pools', 'path_params': ['agent_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'create_dialing_pool': {'method': 'POST', 'path': '/v1/agents/{agent_id}/dialing-pools', 'path_params': ['agent_id'], 'query': [], 'idempotent': True, 'body': 'json', 'response': 'json'},
    'get_dialing_pool': {'method': 'GET', 'path': '/v1/agents/{agent_id}/dialing-pools/{pool_id}', 'path_params': ['agent_id', 'pool_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'preview_dialing_pool': {'method': 'POST', 'path': '/v1/agents/{agent_id}/dialing-pools/{pool_id}/preview', 'path_params': ['agent_id', 'pool_id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'update_dialing_pool': {'method': 'POST', 'path': '/v1/agents/{agent_id}/dialing-pools/{pool_id}/update', 'path_params': ['agent_id', 'pool_id'], 'query': [], 'idempotent': True, 'body': 'json', 'response': 'json'},
    'get_agent_draft': {'method': 'GET', 'path': '/v1/agents/{agent_id}/draft', 'path_params': ['agent_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'patch_agent_draft': {'method': 'PATCH', 'path': '/v1/agents/{agent_id}/draft', 'path_params': ['agent_id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'discard_agent_draft': {'method': 'DELETE', 'path': '/v1/agents/{agent_id}/draft', 'path_params': ['agent_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'get_agent_identity': {'method': 'GET', 'path': '/v1/agents/{agent_id}/identity', 'path_params': ['agent_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'save_agent_identity': {'method': 'PUT', 'path': '/v1/agents/{agent_id}/identity', 'path_params': ['agent_id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'test_agent_contact_card': {'method': 'POST', 'path': '/v1/agents/{agent_id}/identity/send-test', 'path_params': ['agent_id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'none'},
    'download_agent_contact_card': {'method': 'GET', 'path': '/v1/agents/{agent_id}/identity/vcard', 'path_params': ['agent_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'text'},
    'request_agent_identity_review': {'method': 'POST', 'path': '/v1/agents/{agent_id}/identity/verification', 'path_params': ['agent_id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'get_knowledge_retrieval_settings': {'method': 'GET', 'path': '/v1/agents/{agent_id}/knowledge/retrieval-settings', 'path_params': ['agent_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'save_knowledge_retrieval_settings': {'method': 'PUT', 'path': '/v1/agents/{agent_id}/knowledge/retrieval-settings', 'path_params': ['agent_id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'enable_memory': {'method': 'PATCH', 'path': '/v1/agents/{agent_id}/memory', 'path_params': ['agent_id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'get_agent_memory_schema': {'method': 'GET', 'path': '/v1/agents/{agent_id}/memory/schema', 'path_params': ['agent_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'messaging_setup': {'method': 'GET', 'path': '/v1/agents/{agent_id}/messaging', 'path_params': ['agent_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'messaging_conversations': {'method': 'GET', 'path': '/v1/agents/{agent_id}/messaging/{channel}/conversations', 'path_params': ['agent_id', 'channel'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'messaging_conversation': {'method': 'GET', 'path': '/v1/agents/{agent_id}/messaging/{channel}/conversations/{conversation_id}', 'path_params': ['agent_id', 'channel', 'conversation_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'messaging_send_admission': {'method': 'POST', 'path': '/v1/agents/{agent_id}/messaging/{channel}/messages', 'path_params': ['agent_id', 'channel'], 'query': [], 'idempotent': False, 'body': None, 'response': 'none'},
    'preview_agent': {'method': 'POST', 'path': '/v1/agents/{agent_id}/preview', 'path_params': ['agent_id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'publish_agent': {'method': 'POST', 'path': '/v1/agents/{agent_id}/publish', 'path_params': ['agent_id'], 'query': [], 'idempotent': True, 'body': 'json', 'response': 'json'},
    'rollback_agent': {'method': 'POST', 'path': '/v1/agents/{agent_id}/rollback', 'path_params': ['agent_id'], 'query': [], 'idempotent': True, 'body': 'json', 'response': 'json'},
    'run_agent_simulations': {'method': 'POST', 'path': '/v1/agents/{agent_id}/simulations', 'path_params': ['agent_id'], 'query': [], 'idempotent': True, 'body': 'json', 'response': 'json'},
    'get_agent_simulation': {'method': 'GET', 'path': '/v1/agents/{agent_id}/simulations/{simulation_id}', 'path_params': ['agent_id', 'simulation_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'unarchive_agent': {'method': 'POST', 'path': '/v1/agents/{agent_id}/unarchive', 'path_params': ['agent_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'list_agent_versions': {'method': 'GET', 'path': '/v1/agents/{agent_id}/versions', 'path_params': ['agent_id'], 'query': ['limit', 'cursor'], 'idempotent': False, 'body': None, 'response': 'json'},
    'save_agent_version': {'method': 'POST', 'path': '/v1/agents/{agent_id}/versions', 'path_params': ['agent_id'], 'query': [], 'idempotent': True, 'body': None, 'response': 'json'},
    'get_agent_version': {'method': 'GET', 'path': '/v1/agents/{agent_id}/versions/{version_id}', 'path_params': ['agent_id', 'version_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_list_alerts': {'method': 'GET', 'path': '/v1/alerts', 'path_params': [], 'query': ['limit', 'page', 'sort', 'direction', 'agent_id'], 'idempotent': False, 'body': None, 'response': 'json'},
    'create_alert': {'method': 'POST', 'path': '/v1/alerts', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'list_alert_metrics': {'method': 'GET', 'path': '/v1/alerts/metrics', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'preview_alert': {'method': 'POST', 'path': '/v1/alerts/preview', 'path_params': [], 'query': ['hours'], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'get_alert': {'method': 'GET', 'path': '/v1/alerts/{id}', 'path_params': ['id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'update_alert': {'method': 'PATCH', 'path': '/v1/alerts/{id}', 'path_params': ['id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'delete_alert': {'method': 'DELETE', 'path': '/v1/alerts/{id}', 'path_params': ['id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'evaluate_alert': {'method': 'POST', 'path': '/v1/alerts/{id}/evaluate', 'path_params': ['id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'list_api_keys': {'method': 'GET', 'path': '/v1/api-keys', 'path_params': [], 'query': ['status', 'limit', 'cursor'], 'idempotent': False, 'body': None, 'response': 'json'},
    'create_api_key': {'method': 'POST', 'path': '/v1/api-keys', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'get_api_key': {'method': 'GET', 'path': '/v1/api-keys/{key_id}', 'path_params': ['key_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'rename_api_key': {'method': 'PATCH', 'path': '/v1/api-keys/{key_id}', 'path_params': ['key_id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'revoke_api_key': {'method': 'DELETE', 'path': '/v1/api-keys/{key_id}', 'path_params': ['key_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_list_automation_events': {'method': 'GET', 'path': '/v1/automation/events', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'list_automation_executions': {'method': 'GET', 'path': '/v1/automation/executions', 'path_params': [], 'query': ['limit', 'offset', 'status', 'trigger_id'], 'idempotent': False, 'body': None, 'response': 'json'},
    'get_automation_execution': {'method': 'GET', 'path': '/v1/automation/executions/{id}', 'path_params': ['id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'retry_automation_execution': {'method': 'POST', 'path': '/v1/automation/executions/{id}/retry', 'path_params': ['id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'create_automation_pipeline': {'method': 'POST', 'path': '/v1/automation/pipelines', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'compat_list_automation_triggers': {'method': 'GET', 'path': '/v1/automation/triggers', 'path_params': [], 'query': ['limit', 'offset', 'sort', 'agent_id', 'event'], 'idempotent': False, 'body': None, 'response': 'json'},
    'create_automation_trigger': {'method': 'POST', 'path': '/v1/automation/triggers', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'get_automation_trigger': {'method': 'GET', 'path': '/v1/automation/triggers/{id}', 'path_params': ['id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'update_automation_trigger': {'method': 'PATCH', 'path': '/v1/automation/triggers/{id}', 'path_params': ['id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'delete_automation_trigger': {'method': 'DELETE', 'path': '/v1/automation/triggers/{id}', 'path_params': ['id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'list_automation_trigger_executions': {'method': 'GET', 'path': '/v1/automation/triggers/{id}/executions', 'path_params': ['id'], 'query': ['limit', 'offset', 'status'], 'idempotent': False, 'body': None, 'response': 'json'},
    'test_automation_trigger': {'method': 'POST', 'path': '/v1/automation/triggers/{id}/test', 'path_params': ['id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'compat_check_byot': {'method': 'POST', 'path': '/v1/byot/manage/check', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'list_calls': {'method': 'GET', 'path': '/v1/calls', 'path_params': [], 'query': ['agent_id', 'limit', 'cursor'], 'idempotent': False, 'body': None, 'response': 'json'},
    'create_call': {'method': 'POST', 'path': '/v1/calls', 'path_params': [], 'query': [], 'idempotent': True, 'body': 'json', 'response': 'json'},
    'compat_list_active_calls': {'method': 'GET', 'path': '/v1/calls/active', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'stop_active_calls': {'method': 'POST', 'path': '/v1/calls/active/stop', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'compat_stream_active_calls': {'method': 'GET', 'path': '/v1/calls/active/stream', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'text'},
    'transfer_active_call': {'method': 'POST', 'path': '/v1/calls/active/transfer', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'get_call': {'method': 'GET', 'path': '/v1/calls/{call_id}', 'path_params': ['call_id'], 'query': ['agent_id'], 'idempotent': False, 'body': None, 'response': 'json'},
    'analyze_call': {'method': 'POST', 'path': '/v1/calls/{call_id}/analyze', 'path_params': ['call_id'], 'query': ['agent_id'], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'get_corrected_transcript': {'method': 'GET', 'path': '/v1/calls/{call_id}/corrected-transcript', 'path_params': ['call_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'import_corrected_transcript': {'method': 'POST', 'path': '/v1/calls/{call_id}/corrected-transcript', 'path_params': ['call_id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'stop_call': {'method': 'POST', 'path': '/v1/calls/{call_id}/stop', 'path_params': ['call_id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'list_citation_schemas': {'method': 'GET', 'path': '/v1/citation_schemas', 'path_params': [], 'query': ['limit', 'cursor', 'agent_id'], 'idempotent': False, 'body': None, 'response': 'json'},
    'backfill_citation_schemas': {'method': 'POST', 'path': '/v1/citation_schemas/backfill', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'list_citation_schemas_list_path': {'method': 'GET', 'path': '/v1/citation_schemas/list', 'path_params': [], 'query': ['limit', 'cursor', 'agent_id'], 'idempotent': False, 'body': None, 'response': 'json'},
    'list_client_grants': {'method': 'GET', 'path': '/v1/client-grants', 'path_params': [], 'query': ['status'], 'idempotent': False, 'body': None, 'response': 'json'},
    'create_client_rest_credential': {'method': 'POST', 'path': '/v1/client-grants/rest', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'revoke_client_grant': {'method': 'DELETE', 'path': '/v1/client-grants/{grant_id}', 'path_params': ['grant_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_app_list_analysis_presets': {'method': 'GET', 'path': '/v1/compat/app/analysis_presets', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_app_get_session': {'method': 'GET', 'path': '/v1/compat/app/authorization/get-session', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_app_get_agent_phone_billing': {'method': 'GET', 'path': '/v1/compat/app/billing/agent_phone', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_app_get_customer_billing': {'method': 'GET', 'path': '/v1/compat/app/billing/customer', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_app_list_byot': {'method': 'GET', 'path': '/v1/compat/app/byot/get', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_app_read_call_config': {'method': 'GET', 'path': '/v1/compat/app/call_config/read', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_app_list_dashboards': {'method': 'GET', 'path': '/v1/compat/app/dashboards/list', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_app_list_inbound': {'method': 'GET', 'path': '/v1/compat/app/inbound/get_inbound', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_app_list_keys': {'method': 'POST', 'path': '/v1/compat/app/keys/list', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'compat_app_get_org_billing': {'method': 'GET', 'path': '/v1/compat/app/orgs/{uuid}/billing', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_app_list_org_invites': {'method': 'GET', 'path': '/v1/compat/app/orgs/{uuid}/invites', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_app_list_org_members': {'method': 'GET', 'path': '/v1/compat/app/orgs/{uuid}/members', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_app_create_purchase': {'method': 'POST', 'path': '/v1/compat/app/pay/purchases', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'compat_app_get_current_webhook': {'method': 'GET', 'path': '/v1/compat/app/user/getCurrentWebhook', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_app_list_user_logs': {'method': 'GET', 'path': '/v1/compat/app/user/logs', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_app_get_user_log': {'method': 'GET', 'path': '/v1/compat/app/user/logs/{uuid}', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_app_get_user_log_enrich': {'method': 'GET', 'path': '/v1/compat/app/user/logs/{uuid}/enrich', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_app_get_rate_limits': {'method': 'GET', 'path': '/v1/compat/app/user/rateLimits', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_app_get_user': {'method': 'GET', 'path': '/v1/compat/app/user/{id}', 'path_params': ['id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'none'},
    'compat_app_get_knowledge_asset': {'method': 'GET', 'path': '/v1/compat/app/{org_uuid}/kb/{kb_uuid}/{asset_uuid}', 'path_params': ['org_uuid', 'kb_uuid', 'asset_uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_list_contacts': {'method': 'GET', 'path': '/v1/contacts', 'path_params': [], 'query': ['limit', 'cursor'], 'idempotent': False, 'body': None, 'response': 'json'},
    'merge_contacts': {'method': 'POST', 'path': '/v1/contacts/merge', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'resolve_contact': {'method': 'POST', 'path': '/v1/contacts/resolve', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'get_contact_schema': {'method': 'GET', 'path': '/v1/contacts/schema', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'save_contact_schema': {'method': 'PUT', 'path': '/v1/contacts/schema', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'compat_get_contact': {'method': 'GET', 'path': '/v1/contacts/{contact_id}', 'path_params': ['contact_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_get_migration_split': {'method': 'GET', 'path': '/v1/convo_pathway/migration_split/enabled', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'get_credit_balance': {'method': 'GET', 'path': '/v1/credits', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'list_credit_history': {'method': 'GET', 'path': '/v1/credits/history', 'path_params': [], 'query': ['limit', 'before'], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_list_dispositions': {'method': 'GET', 'path': '/v1/dispositions/', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'list_evals': {'method': 'GET', 'path': '/v1/evals', 'path_params': [], 'query': ['status', 'limit', 'cursor'], 'idempotent': False, 'body': None, 'response': 'json'},
    'create_eval': {'method': 'POST', 'path': '/v1/evals', 'path_params': [], 'query': [], 'idempotent': True, 'body': 'json', 'response': 'json'},
    'compat_list_eval_agent_templates': {'method': 'GET', 'path': '/v1/evals/agent-templates', 'path_params': [], 'query': ['limit', 'cursor'], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_list_eval_agents': {'method': 'GET', 'path': '/v1/evals/agents', 'path_params': [], 'query': ['limit', 'cursor'], 'idempotent': False, 'body': None, 'response': 'json'},
    'quick_run_eval_template': {'method': 'POST', 'path': '/v1/evals/quick-run', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'get_eval_results': {'method': 'GET', 'path': '/v1/evals/results', 'path_params': [], 'query': ['agent_id'], 'idempotent': False, 'body': None, 'response': 'json'},
    'run_evals': {'method': 'POST', 'path': '/v1/evals/run', 'path_params': [], 'query': [], 'idempotent': True, 'body': 'json', 'response': 'json'},
    'list_eval_runs': {'method': 'GET', 'path': '/v1/evals/runs', 'path_params': [], 'query': ['agent_id', 'status', 'since', 'until', 'limit', 'cursor'], 'idempotent': False, 'body': None, 'response': 'json'},
    'get_eval_run': {'method': 'GET', 'path': '/v1/evals/runs/{run_id}', 'path_params': ['run_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'list_eval_test_cases': {'method': 'GET', 'path': '/v1/evals/test-cases', 'path_params': [], 'query': ['agent_id', 'limit', 'cursor'], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_list_eval_user_templates': {'method': 'GET', 'path': '/v1/evals/user-templates', 'path_params': [], 'query': ['limit', 'cursor'], 'idempotent': False, 'body': None, 'response': 'json'},
    'create_eval_user_template': {'method': 'POST', 'path': '/v1/evals/user-templates', 'path_params': [], 'query': [], 'idempotent': True, 'body': None, 'response': 'json'},
    'get_eval': {'method': 'GET', 'path': '/v1/evals/{eval_id}', 'path_params': ['eval_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'update_eval': {'method': 'PATCH', 'path': '/v1/evals/{eval_id}', 'path_params': ['eval_id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'delete_eval': {'method': 'DELETE', 'path': '/v1/evals/{eval_id}', 'path_params': ['eval_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'align_judge': {'method': 'POST', 'path': '/v1/evals/{eval_id}/align', 'path_params': ['eval_id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'list_judge_production_calls': {'method': 'GET', 'path': '/v1/evals/{eval_id}/production-calls', 'path_params': ['eval_id'], 'query': ['agent_id'], 'idempotent': False, 'body': None, 'response': 'json'},
    'run_production_judge': {'method': 'POST', 'path': '/v1/evals/{eval_id}/production-run', 'path_params': ['eval_id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'compat_list_files': {'method': 'GET', 'path': '/v1/files/list', 'path_params': [], 'query': ['limit', 'cursor'], 'idempotent': False, 'body': None, 'response': 'json'},
    'get_health': {'method': 'GET', 'path': '/v1/health', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'list_integrations': {'method': 'GET', 'path': '/v1/integrations', 'path_params': [], 'query': ['limit', 'cursor'], 'idempotent': False, 'body': None, 'response': 'json'},
    'create_integration': {'method': 'POST', 'path': '/v1/integrations', 'path_params': [], 'query': [], 'idempotent': True, 'body': 'json', 'response': 'json'},
    'get_integration': {'method': 'GET', 'path': '/v1/integrations/{integration_id}', 'path_params': ['integration_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'update_integration': {'method': 'PATCH', 'path': '/v1/integrations/{integration_id}', 'path_params': ['integration_id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'delete_integration': {'method': 'DELETE', 'path': '/v1/integrations/{integration_id}', 'path_params': ['integration_id'], 'query': ['restore', 'revision'], 'idempotent': False, 'body': None, 'response': 'json'},
    'list_integration_actions': {'method': 'GET', 'path': '/v1/integrations/{integration_id}/actions', 'path_params': ['integration_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'verify_integration': {'method': 'POST', 'path': '/v1/integrations/{integration_id}/verify', 'path_params': ['integration_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'list_knowledge_sources': {'method': 'GET', 'path': '/v1/knowledge-sources', 'path_params': [], 'query': ['agent_id', 'limit', 'cursor'], 'idempotent': False, 'body': None, 'response': 'json'},
    'create_knowledge_source': {'method': 'POST', 'path': '/v1/knowledge-sources', 'path_params': [], 'query': ['agent_id'], 'idempotent': False, 'body': 'multipart', 'response': 'json'},
    'create_text_knowledge_source': {'method': 'POST', 'path': '/v1/knowledge-sources/text', 'path_params': [], 'query': [], 'idempotent': True, 'body': 'json', 'response': 'json'},
    'update_knowledge_source': {'method': 'PATCH', 'path': '/v1/knowledge-sources/{source_id}', 'path_params': ['source_id'], 'query': ['agent_id'], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'get_knowledge_source': {'method': 'GET', 'path': '/v1/knowledge-sources/{source_id}', 'path_params': ['source_id'], 'query': ['agent_id'], 'idempotent': False, 'body': None, 'response': 'json'},
    'delete_knowledge_source': {'method': 'DELETE', 'path': '/v1/knowledge-sources/{source_id}', 'path_params': ['source_id'], 'query': ['agent_id'], 'idempotent': False, 'body': None, 'response': 'json'},
    'reparse_knowledge_source': {'method': 'POST', 'path': '/v1/knowledge-sources/{source_id}/reparse', 'path_params': ['source_id'], 'query': ['agent_id'], 'idempotent': False, 'body': None, 'response': 'json'},
    'chat_knowledge': {'method': 'POST', 'path': '/v1/knowledge/chat', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'crawl_knowledge': {'method': 'POST', 'path': '/v1/knowledge/crawl', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'compat_get_knowledge_map': {'method': 'GET', 'path': '/v1/knowledge/map', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_list_knowledge_queries': {'method': 'GET', 'path': '/v1/knowledge/queries', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'change_knowledge_question': {'method': 'PATCH', 'path': '/v1/knowledge/questions/{question_id}', 'path_params': ['question_id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'answer_knowledge_question': {'method': 'PUT', 'path': '/v1/knowledge/questions/{question_id}/answer', 'path_params': ['question_id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'compat_list_knowledge_sources': {'method': 'GET', 'path': '/v1/knowledge/sources', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_list_knowledge_sources_picker': {'method': 'GET', 'path': '/v1/knowledge/sources/picker', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'test_knowledge_sources': {'method': 'POST', 'path': '/v1/knowledge/test', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'get_knowledge_testing_context': {'method': 'GET', 'path': '/v1/knowledge/testing-context', 'path_params': [], 'query': ['agent_id'], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_get_knowledge': {'method': 'GET', 'path': '/v1/knowledge/{uuid}', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_get_knowledge_content': {'method': 'GET', 'path': '/v1/knowledge/{uuid}/content', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_update_knowledge_content': {'method': 'PATCH', 'path': '/v1/knowledge/{uuid}/content', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'compat_list_knowledge_versions': {'method': 'GET', 'path': '/v1/knowledge/{uuid}/versions', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'stream_live_calls': {'method': 'GET', 'path': '/v1/live-calls/stream', 'path_params': [], 'query': ['agent_id'], 'idempotent': False, 'body': None, 'response': 'json'},
    'stream_live_transcript': {'method': 'GET', 'path': '/v1/live-calls/transcript/stream', 'path_params': [], 'query': ['agent_id', 'room'], 'idempotent': False, 'body': None, 'response': 'json'},
    'mcp_json_rpc': {'method': 'POST', 'path': '/v1/mcp', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'get_mcp_client_setup': {'method': 'GET', 'path': '/v1/mcp/clients/{client}', 'path_params': ['client'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'list_mcp_connections': {'method': 'GET', 'path': '/v1/mcp/connections', 'path_params': [], 'query': ['status'], 'idempotent': False, 'body': None, 'response': 'json'},
    'create_mcp_connection': {'method': 'POST', 'path': '/v1/mcp/connections', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'revoke_mcp_connection': {'method': 'DELETE', 'path': '/v1/mcp/connections/{connection_id}', 'path_params': ['connection_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'get_me': {'method': 'GET', 'path': '/v1/me', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'create_memory': {'method': 'POST', 'path': '/v1/memory', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'compat_list_memory_changes': {'method': 'GET', 'path': '/v1/memory/changes', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'reset_memory': {'method': 'POST', 'path': '/v1/memory/reset', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'update_memory': {'method': 'PATCH', 'path': '/v1/memory/{memory_id}', 'path_params': ['memory_id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'list_models_v1': {'method': 'GET', 'path': '/v1/models', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'get_service_version': {'method': 'GET', 'path': '/v1/org/service-version', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'update_service_version': {'method': 'PUT', 'path': '/v1/org/service-version', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'list_service_versions': {'method': 'GET', 'path': '/v1/org/service-versions', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'list_organizations': {'method': 'GET', 'path': '/v1/organizations', 'path_params': [], 'query': ['limit', 'cursor'], 'idempotent': False, 'body': None, 'response': 'json'},
    'organizations_create': {'method': 'POST', 'path': '/v1/organizations', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'get_organization': {'method': 'GET', 'path': '/v1/organizations/{organization_id}', 'path_params': ['organization_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_list_pathways': {'method': 'GET', 'path': '/v1/pathway', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'list_personas': {'method': 'GET', 'path': '/v1/personas', 'path_params': [], 'query': ['page', 'limit'], 'idempotent': False, 'body': None, 'response': 'json'},
    'get_persona': {'method': 'GET', 'path': '/v1/personas/{persona_id}', 'path_params': ['persona_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'create_phone_message': {'method': 'POST', 'path': '/v1/phone-messages', 'path_params': [], 'query': [], 'idempotent': True, 'body': 'json', 'response': 'json'},
    'preview_phone_message': {'method': 'POST', 'path': '/v1/phone-messages/preview', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'list_phone_numbers': {'method': 'GET', 'path': '/v1/phone-numbers', 'path_params': [], 'query': ['agent_id', 'limit', 'cursor'], 'idempotent': False, 'body': None, 'response': 'json'},
    'bind_phone_number': {'method': 'POST', 'path': '/v1/phone-numbers', 'path_params': [], 'query': [], 'idempotent': True, 'body': 'json', 'response': 'json'},
    'poll_phone_onboarding': {'method': 'POST', 'path': '/v1/phone-onboarding/poll', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'start_phone_onboarding': {'method': 'POST', 'path': '/v1/phone-onboarding/start', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'get_phone_profile': {'method': 'GET', 'path': '/v1/phone-profile', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'create_phone_task': {'method': 'POST', 'path': '/v1/phone-tasks', 'path_params': [], 'query': [], 'idempotent': True, 'body': 'json', 'response': 'json'},
    'preview_phone_task': {'method': 'POST', 'path': '/v1/phone-tasks/preview', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'get_phone_task': {'method': 'GET', 'path': '/v1/phone-tasks/{task_id}', 'path_params': ['task_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'cancel_phone_task': {'method': 'POST', 'path': '/v1/phone-tasks/{task_id}/cancel', 'path_params': ['task_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'get_phone_thread': {'method': 'GET', 'path': '/v1/phone-threads/{thread_id}', 'path_params': ['thread_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'get_platform': {'method': 'GET', 'path': '/v1/platform', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'list_prompts': {'method': 'GET', 'path': '/v1/prompts', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'create_prompt': {'method': 'POST', 'path': '/v1/prompts', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'get_prompt': {'method': 'GET', 'path': '/v1/prompts/{prompt_id}', 'path_params': ['prompt_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'get_recording': {'method': 'GET', 'path': '/v1/recordings/{recording_id}', 'path_params': ['recording_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'list_release_deployments': {'method': 'GET', 'path': '/v1/release-deployments', 'path_params': [], 'query': ['limit', 'cursor'], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_list_releases': {'method': 'GET', 'path': '/v1/releases', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_get_current_deployment': {'method': 'GET', 'path': '/v1/releases/deployments/current', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_list_deployment_history': {'method': 'GET', 'path': '/v1/releases/deployments/history', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_list_resources': {'method': 'GET', 'path': '/v1/resources', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_list_secrets': {'method': 'GET', 'path': '/v1/secrets', 'path_params': [], 'query': ['q', 'type', 'status', 'sort'], 'idempotent': False, 'body': None, 'response': 'json'},
    'create_secret': {'method': 'POST', 'path': '/v1/secrets', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'update_secret': {'method': 'PATCH', 'path': '/v1/secrets/{id}', 'path_params': ['id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'delete_secret': {'method': 'DELETE', 'path': '/v1/secrets/{id}', 'path_params': ['id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'refresh_secret': {'method': 'POST', 'path': '/v1/secrets/{id}/refresh', 'path_params': ['id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'list_sessions': {'method': 'GET', 'path': '/v1/sessions', 'path_params': [], 'query': ['agent_id', 'channel', 'limit', 'cursor'], 'idempotent': False, 'body': None, 'response': 'json'},
    'create_session': {'method': 'POST', 'path': '/v1/sessions', 'path_params': [], 'query': [], 'idempotent': True, 'body': 'json', 'response': 'json'},
    'get_session': {'method': 'GET', 'path': '/v1/sessions/{session_id}', 'path_params': ['session_id'], 'query': ['agent_id'], 'idempotent': False, 'body': None, 'response': 'json'},
    'get_request_signing': {'method': 'GET', 'path': '/v1/signing', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'patch_request_signing': {'method': 'PATCH', 'path': '/v1/signing', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'generate_signing_key': {'method': 'POST', 'path': '/v1/signing/keys', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'revoke_previous_signing_keys': {'method': 'POST', 'path': '/v1/signing/keys/revoke-previous', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'batch_sms': {'method': 'POST', 'path': '/v1/sms/batch', 'path_params': [], 'query': [], 'idempotent': True, 'body': 'json', 'response': 'json'},
    'compat_list_sms_conversations': {'method': 'GET', 'path': '/v1/sms/conversations', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'get_sms_conversation': {'method': 'GET', 'path': '/v1/sms/conversations/{conversation_id}', 'path_params': ['conversation_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'end_sms_conversation': {'method': 'POST', 'path': '/v1/sms/conversations/{conversation_id}/end', 'path_params': ['conversation_id'], 'query': [], 'idempotent': True, 'body': None, 'response': 'json'},
    'handoff_sms_conversation': {'method': 'POST', 'path': '/v1/sms/conversations/{conversation_id}/handoff', 'path_params': ['conversation_id'], 'query': [], 'idempotent': True, 'body': None, 'response': 'json'},
    'list_sms_messages': {'method': 'GET', 'path': '/v1/sms/conversations/{conversation_id}/messages', 'path_params': ['conversation_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'reply_sms': {'method': 'POST', 'path': '/v1/sms/conversations/{conversation_id}/messages', 'path_params': ['conversation_id'], 'query': [], 'idempotent': True, 'body': 'json', 'response': 'json'},
    'opt_out_sms_conversation': {'method': 'POST', 'path': '/v1/sms/conversations/{conversation_id}/opt-out', 'path_params': ['conversation_id'], 'query': [], 'idempotent': True, 'body': None, 'response': 'json'},
    'get_sms_policy': {'method': 'GET', 'path': '/v1/sms/conversations/{conversation_id}/policy', 'path_params': ['conversation_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'resume_sms_conversation': {'method': 'POST', 'path': '/v1/sms/conversations/{conversation_id}/resume', 'path_params': ['conversation_id'], 'query': [], 'idempotent': True, 'body': None, 'response': 'json'},
    'compat_list_sms_numbers': {'method': 'GET', 'path': '/v1/sms/numbers', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'send_sms': {'method': 'POST', 'path': '/v1/sms/send', 'path_params': [], 'query': [], 'idempotent': True, 'body': 'json', 'response': 'json'},
    'list_snippets': {'method': 'GET', 'path': '/v1/snippets', 'path_params': [], 'query': ['status', 'limit', 'cursor'], 'idempotent': False, 'body': None, 'response': 'json'},
    'create_snippet': {'method': 'POST', 'path': '/v1/snippets', 'path_params': [], 'query': [], 'idempotent': True, 'body': 'json', 'response': 'json'},
    'get_snippet': {'method': 'GET', 'path': '/v1/snippets/{snippet_id}', 'path_params': ['snippet_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'update_snippet': {'method': 'PATCH', 'path': '/v1/snippets/{snippet_id}', 'path_params': ['snippet_id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'delete_snippet': {'method': 'DELETE', 'path': '/v1/snippets/{snippet_id}', 'path_params': ['snippet_id'], 'query': ['restore'], 'idempotent': False, 'body': None, 'response': 'json'},
    'publish_snippet': {'method': 'POST', 'path': '/v1/snippets/{snippet_id}/publish', 'path_params': ['snippet_id'], 'query': [], 'idempotent': True, 'body': None, 'response': 'json'},
    'test_snippet': {'method': 'POST', 'path': '/v1/snippets/{snippet_id}/test', 'path_params': ['snippet_id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'get_snippet_version': {'method': 'GET', 'path': '/v1/snippets/{snippet_id}/versions/{version}', 'path_params': ['snippet_id', 'version'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'list_standards': {'method': 'GET', 'path': '/v1/standards', 'path_params': [], 'query': ['agent_id'], 'idempotent': False, 'body': None, 'response': 'json'},
    'create_standard': {'method': 'POST', 'path': '/v1/standards', 'path_params': [], 'query': [], 'idempotent': True, 'body': None, 'response': 'json'},
    'run_standards': {'method': 'POST', 'path': '/v1/standards/run', 'path_params': [], 'query': [], 'idempotent': True, 'body': None, 'response': 'json'},
    'list_standards_runs': {'method': 'GET', 'path': '/v1/standards/runs', 'path_params': [], 'query': ['agent_id'], 'idempotent': False, 'body': None, 'response': 'json'},
    'update_standard': {'method': 'PATCH', 'path': '/v1/standards/{standard_id}', 'path_params': ['standard_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'delete_standard': {'method': 'DELETE', 'path': '/v1/standards/{standard_id}', 'path_params': ['standard_id'], 'query': ['agent_id'], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_subaccounts_retired': {'method': 'GET', 'path': '/v1/subaccounts', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'get_test_analytics': {'method': 'GET', 'path': '/v1/test-analytics', 'path_params': [], 'query': ['agent_id', 'days', 'min_samples'], 'idempotent': False, 'body': None, 'response': 'json'},
    'run_testbed': {'method': 'POST', 'path': '/v1/testbed/runs', 'path_params': [], 'query': [], 'idempotent': True, 'body': None, 'response': 'json'},
    'get_testbed_run': {'method': 'GET', 'path': '/v1/testbed/runs/{run_id}', 'path_params': ['run_id'], 'query': ['agent_id'], 'idempotent': False, 'body': None, 'response': 'json'},
    'get_testbed_situation': {'method': 'GET', 'path': '/v1/testbed/situation', 'path_params': [], 'query': ['agent_id', 'conversation_id', 'turn', 'step'], 'idempotent': False, 'body': None, 'response': 'json'},
    'save_testbed_standard': {'method': 'POST', 'path': '/v1/testbed/standards', 'path_params': [], 'query': [], 'idempotent': True, 'body': None, 'response': 'json'},
    'list_tests': {'method': 'GET', 'path': '/v1/tests', 'path_params': [], 'query': ['agent_id', 'limit', 'cursor'], 'idempotent': False, 'body': None, 'response': 'json'},
    'run_tests': {'method': 'POST', 'path': '/v1/tests', 'path_params': [], 'query': [], 'idempotent': True, 'body': 'json', 'response': 'json'},
    'get_test': {'method': 'GET', 'path': '/v1/tests/{test_id}', 'path_params': ['test_id'], 'query': ['agent_id'], 'idempotent': False, 'body': None, 'response': 'json'},
    'start_text_assistant_link': {'method': 'POST', 'path': '/v1/text-assistant/link', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'unlink_text_assistant': {'method': 'DELETE', 'path': '/v1/text-assistant/link', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'confirm_text_assistant_link': {'method': 'POST', 'path': '/v1/text-assistant/link/confirm', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'get_text_assistant_settings': {'method': 'GET', 'path': '/v1/text-assistant/settings', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'update_text_assistant_settings': {'method': 'PATCH', 'path': '/v1/text-assistant/settings', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'get_text_assistant_thread': {'method': 'GET', 'path': '/v1/text-assistant/thread', 'path_params': [], 'query': ['before'], 'idempotent': False, 'body': None, 'response': 'json'},
    'list_tools': {'method': 'GET', 'path': '/v1/tools', 'path_params': [], 'query': ['status', 'limit', 'cursor'], 'idempotent': False, 'body': None, 'response': 'json'},
    'create_tool': {'method': 'POST', 'path': '/v1/tools', 'path_params': [], 'query': [], 'idempotent': True, 'body': 'json', 'response': 'json'},
    'get_tool': {'method': 'GET', 'path': '/v1/tools/{tool_id}', 'path_params': ['tool_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'update_tool': {'method': 'PATCH', 'path': '/v1/tools/{tool_id}', 'path_params': ['tool_id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'delete_tool': {'method': 'DELETE', 'path': '/v1/tools/{tool_id}', 'path_params': ['tool_id'], 'query': ['restore', 'revision'], 'idempotent': False, 'body': None, 'response': 'json'},
    'execute_tool': {'method': 'POST', 'path': '/v1/tools/{tool_id}/execute', 'path_params': ['tool_id'], 'query': [], 'idempotent': True, 'body': 'json', 'response': 'json'},
    'list_tool_executions': {'method': 'GET', 'path': '/v1/tools/{tool_id}/executions', 'path_params': ['tool_id'], 'query': ['limit', 'cursor'], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_list_transcript_reports': {'method': 'GET', 'path': '/v1/transcript-reports/call/{uuid}', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'get_translation_sessions': {'method': 'GET', 'path': '/v1/translation-sessions', 'path_params': [], 'query': ['agent_id'], 'idempotent': False, 'body': None, 'response': 'json'},
    'create_translation_session': {'method': 'POST', 'path': '/v1/translation-sessions', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'compat_list_triage_categories': {'method': 'GET', 'path': '/v1/triage/categories', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_list_triage_flag_types': {'method': 'GET', 'path': '/v1/triage/flag-types', 'path_params': [], 'query': ['limit', 'cursor'], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_list_triage_issues': {'method': 'GET', 'path': '/v1/triage/issues', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_create_triage_issue': {'method': 'POST', 'path': '/v1/triage/issues', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_get_triage_issue': {'method': 'GET', 'path': '/v1/triage/issues/{uuid}', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_update_triage_issue': {'method': 'PATCH', 'path': '/v1/triage/issues/{uuid}', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_list_triage_issue_activity': {'method': 'GET', 'path': '/v1/triage/issues/{uuid}/activity', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_list_triage_issue_affected': {'method': 'GET', 'path': '/v1/triage/issues/{uuid}/affected', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_link_triage_issue_call': {'method': 'PUT', 'path': '/v1/triage/issues/{uuid}/calls/{call_id}', 'path_params': ['uuid', 'call_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_create_triage_issue_comment': {'method': 'POST', 'path': '/v1/triage/issues/{uuid}/comments', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_list_triage_issue_flags': {'method': 'GET', 'path': '/v1/triage/issues/{uuid}/flags', 'path_params': ['uuid'], 'query': ['limit', 'cursor'], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_create_triage_issue_flag': {'method': 'POST', 'path': '/v1/triage/issues/{uuid}/flags', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_list_triage_issue_relations': {'method': 'GET', 'path': '/v1/triage/issues/{uuid}/relations', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_create_triage_issue_relation': {'method': 'POST', 'path': '/v1/triage/issues/{uuid}/relations', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'compat_delete_triage_issue_relation': {'method': 'DELETE', 'path': '/v1/triage/issues/{uuid}/relations/{relation_id}', 'path_params': ['uuid', 'relation_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'none'},
    'compat_list_triage_issue_resources': {'method': 'GET', 'path': '/v1/triage/issues/{uuid}/resources', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_attach_triage_file_resource': {'method': 'POST', 'path': '/v1/triage/issues/{uuid}/resources', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_mark_triage_issue_viewed': {'method': 'PUT', 'path': '/v1/triage/issues/{uuid}/view', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'list_voices': {'method': 'GET', 'path': '/v1/voices', 'path_params': [], 'query': ['engine', 'language', 'search', 'limit', 'cursor'], 'idempotent': False, 'body': None, 'response': 'json'},
    'list_voice_library': {'method': 'GET', 'path': '/v1/voices/library', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'add_voice_library': {'method': 'POST', 'path': '/v1/voices/library/add', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'get_shared_voice': {'method': 'GET', 'path': '/v1/voices/library/{entry_id}', 'path_params': ['entry_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'rate_voice': {'method': 'POST', 'path': '/v1/voices/library/{entry_id}/rate', 'path_params': ['entry_id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'sample_voice': {'method': 'GET', 'path': '/v1/voices/library/{entry_id}/sample', 'path_params': ['entry_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'text'},
    'share_voice': {'method': 'POST', 'path': '/v1/voices/library/{entry_id}/share', 'path_params': ['entry_id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'list_studio_clones': {'method': 'GET', 'path': '/v1/voices/studio', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'prepare_studio_clone': {'method': 'POST', 'path': '/v1/voices/studio', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'list_webhooks': {'method': 'GET', 'path': '/v1/webhooks', 'path_params': [], 'query': ['limit', 'cursor'], 'idempotent': False, 'body': None, 'response': 'json'},
    'create_webhook': {'method': 'POST', 'path': '/v1/webhooks', 'path_params': [], 'query': [], 'idempotent': True, 'body': 'json', 'response': 'json'},
    'get_webhook': {'method': 'GET', 'path': '/v1/webhooks/{webhook_id}', 'path_params': ['webhook_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'patch_webhook': {'method': 'PATCH', 'path': '/v1/webhooks/{webhook_id}', 'path_params': ['webhook_id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'delete_webhook': {'method': 'DELETE', 'path': '/v1/webhooks/{webhook_id}', 'path_params': ['webhook_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'list_webhook_deliveries': {'method': 'GET', 'path': '/v1/webhooks/{webhook_id}/deliveries', 'path_params': ['webhook_id'], 'query': ['limit', 'cursor'], 'idempotent': False, 'body': None, 'response': 'json'},
    'resend_webhook_delivery': {'method': 'POST', 'path': '/v1/webhooks/{webhook_id}/deliveries/{delivery_id}/resend', 'path_params': ['webhook_id', 'delivery_id'], 'query': [], 'idempotent': True, 'body': None, 'response': 'json'},
    'test_webhook': {'method': 'POST', 'path': '/v1/webhooks/{webhook_id}/test', 'path_params': ['webhook_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'list_widget_live_chats': {'method': 'GET', 'path': '/v1/widget-live-chats', 'path_params': [], 'query': ['agent_id'], 'idempotent': False, 'body': None, 'response': 'json'},
    'act_on_widget_live_chat': {'method': 'POST', 'path': '/v1/widget-live-chats/{chat_id}', 'path_params': ['chat_id'], 'query': ['agent_id'], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'list_widget_custom_components': {'method': 'GET', 'path': '/v1/widget/custom-components', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'create_widget_custom_component': {'method': 'POST', 'path': '/v1/widget/custom-components', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'update_widget_custom_component': {'method': 'PATCH', 'path': '/v1/widget/custom-components/{id}', 'path_params': ['id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'delete_widget_custom_component': {'method': 'DELETE', 'path': '/v1/widget/custom-components/{id}', 'path_params': ['id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'none'},
    'compat_list_widget_threads': {'method': 'GET', 'path': '/v1/widget/threads', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_list_widgets': {'method': 'GET', 'path': '/v1/widgets', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'list_workspaces': {'method': 'GET', 'path': '/v1/workspaces', 'path_params': [], 'query': ['limit', 'cursor'], 'idempotent': False, 'body': None, 'response': 'json'},
    'get_workspace': {'method': 'GET', 'path': '/v1/workspaces/{workspace_id}', 'path_params': ['workspace_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'patch_workspace': {'method': 'PATCH', 'path': '/v1/workspaces/{workspace_id}', 'path_params': ['workspace_id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'get_workspace_jwks': {'method': 'GET', 'path': '/v1/workspaces/{workspace_id}/.well-known/jwks.json', 'path_params': ['workspace_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_list_agents': {'method': 'GET', 'path': '/v2/agents', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_get_starter': {'method': 'GET', 'path': '/v2/agents/starter', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_create_starter': {'method': 'POST', 'path': '/v2/agents/starter', 'path_params': [], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'compat_v2_list_starter_templates': {'method': 'GET', 'path': '/v2/agents/starter-templates', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_get_agent': {'method': 'GET', 'path': '/v2/agents/{uuid}', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_list_branches': {'method': 'GET', 'path': '/v2/agents/{uuid}/branches', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_create_branch': {'method': 'POST', 'path': '/v2/agents/{uuid}/branches', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_delete_branch': {'method': 'DELETE', 'path': '/v2/agents/{uuid}/branches/{branch_id}', 'path_params': ['uuid', 'branch_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_merge_branch': {'method': 'POST', 'path': '/v2/agents/{uuid}/branches/{branch_id}/merge', 'path_params': ['uuid', 'branch_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_rebase_branch': {'method': 'POST', 'path': '/v2/agents/{uuid}/branches/{branch_id}/rebase', 'path_params': ['uuid', 'branch_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_preview_branch_rebase': {'method': 'POST', 'path': '/v2/agents/{uuid}/branches/{branch_id}/rebase-preview', 'path_params': ['uuid', 'branch_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_list_check_runs': {'method': 'GET', 'path': '/v2/agents/{uuid}/check-runs', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_list_deployments': {'method': 'GET', 'path': '/v2/agents/{uuid}/deployments', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_list_dispositions': {'method': 'GET', 'path': '/v2/agents/{uuid}/dispositions', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_create_disposition': {'method': 'POST', 'path': '/v2/agents/{uuid}/dispositions', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'compat_v2_get_disposition_extractor_catalog': {'method': 'GET', 'path': '/v2/agents/{uuid}/dispositions/extractor-catalog', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_list_disposition_extractors': {'method': 'GET', 'path': '/v2/agents/{uuid}/dispositions/extractors', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_create_disposition_extractor': {'method': 'POST', 'path': '/v2/agents/{uuid}/dispositions/extractors', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'compat_v2_get_disposition_extractor': {'method': 'GET', 'path': '/v2/agents/{uuid}/dispositions/extractors/{extractor_uuid}', 'path_params': ['uuid', 'extractor_uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_update_disposition_extractor_draft': {'method': 'PATCH', 'path': '/v2/agents/{uuid}/dispositions/extractors/{extractor_uuid}/draft', 'path_params': ['uuid', 'extractor_uuid'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'compat_v2_publish_disposition_extractor': {'method': 'POST', 'path': '/v2/agents/{uuid}/dispositions/extractors/{extractor_uuid}/publish', 'path_params': ['uuid', 'extractor_uuid'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'compat_v2_get_disposition_extractor_version': {'method': 'GET', 'path': '/v2/agents/{uuid}/dispositions/extractors/{extractor_uuid}/versions/{version_uuid}', 'path_params': ['uuid', 'extractor_uuid', 'version_uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_get_disposition_model_profile_catalog': {'method': 'GET', 'path': '/v2/agents/{uuid}/dispositions/model-profile-catalog', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_get_disposition_variable_catalog': {'method': 'GET', 'path': '/v2/agents/{uuid}/dispositions/variable-catalog', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_get_disposition': {'method': 'GET', 'path': '/v2/agents/{uuid}/dispositions/{disposition_uuid}', 'path_params': ['uuid', 'disposition_uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_delete_disposition': {'method': 'DELETE', 'path': '/v2/agents/{uuid}/dispositions/{disposition_uuid}', 'path_params': ['uuid', 'disposition_uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_disable_disposition': {'method': 'POST', 'path': '/v2/agents/{uuid}/dispositions/{disposition_uuid}/disable', 'path_params': ['uuid', 'disposition_uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_get_disposition_draft': {'method': 'GET', 'path': '/v2/agents/{uuid}/dispositions/{disposition_uuid}/draft', 'path_params': ['uuid', 'disposition_uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_update_disposition_draft': {'method': 'PATCH', 'path': '/v2/agents/{uuid}/dispositions/{disposition_uuid}/draft', 'path_params': ['uuid', 'disposition_uuid'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'compat_v2_estimate_disposition': {'method': 'POST', 'path': '/v2/agents/{uuid}/dispositions/{disposition_uuid}/estimates', 'path_params': ['uuid', 'disposition_uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_publish_disposition': {'method': 'POST', 'path': '/v2/agents/{uuid}/dispositions/{disposition_uuid}/publish', 'path_params': ['uuid', 'disposition_uuid'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'compat_v2_list_disposition_runs': {'method': 'GET', 'path': '/v2/agents/{uuid}/dispositions/{disposition_uuid}/runs', 'path_params': ['uuid', 'disposition_uuid'], 'query': ['limit'], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_create_disposition_run': {'method': 'POST', 'path': '/v2/agents/{uuid}/dispositions/{disposition_uuid}/runs', 'path_params': ['uuid', 'disposition_uuid'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'compat_v2_get_disposition_run': {'method': 'GET', 'path': '/v2/agents/{uuid}/dispositions/{disposition_uuid}/runs/{run_uuid}', 'path_params': ['uuid', 'disposition_uuid', 'run_uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_align_disposition_run': {'method': 'POST', 'path': '/v2/agents/{uuid}/dispositions/{disposition_uuid}/runs/{run_uuid}/align', 'path_params': ['uuid', 'disposition_uuid', 'run_uuid'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'compat_v2_list_disposition_run_annotations': {'method': 'GET', 'path': '/v2/agents/{uuid}/dispositions/{disposition_uuid}/runs/{run_uuid}/cases/{call_id}/annotations/{value_id}', 'path_params': ['uuid', 'disposition_uuid', 'run_uuid', 'call_id', 'value_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_put_disposition_run_annotation': {'method': 'PUT', 'path': '/v2/agents/{uuid}/dispositions/{disposition_uuid}/runs/{run_uuid}/cases/{call_id}/annotations/{value_id}', 'path_params': ['uuid', 'disposition_uuid', 'run_uuid', 'call_id', 'value_id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'compat_v2_export_disposition_run_csv': {'method': 'GET', 'path': '/v2/agents/{uuid}/dispositions/{disposition_uuid}/runs/{run_uuid}/export-csv', 'path_params': ['uuid', 'disposition_uuid', 'run_uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_list_disposition_run_rows': {'method': 'GET', 'path': '/v2/agents/{uuid}/dispositions/{disposition_uuid}/runs/{run_uuid}/rows', 'path_params': ['uuid', 'disposition_uuid', 'run_uuid'], 'query': ['limit', 'offset'], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_list_disposition_versions': {'method': 'GET', 'path': '/v2/agents/{uuid}/dispositions/{disposition_uuid}/versions', 'path_params': ['uuid', 'disposition_uuid'], 'query': ['beforeVersion'], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_get_disposition_version': {'method': 'GET', 'path': '/v2/agents/{uuid}/dispositions/{disposition_uuid}/versions/{version_uuid}', 'path_params': ['uuid', 'disposition_uuid', 'version_uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_list_environments': {'method': 'GET', 'path': '/v2/agents/{uuid}/environments', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_get_staging_checks': {'method': 'GET', 'path': '/v2/agents/{uuid}/environments/staging/checks', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_list_variables': {'method': 'GET', 'path': '/v2/agents/{uuid}/environments/{env}/variables', 'path_params': ['uuid', 'env'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_save_variable': {'method': 'POST', 'path': '/v2/agents/{uuid}/environments/{env}/variables', 'path_params': ['uuid', 'env'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'compat_v2_put_variable': {'method': 'PUT', 'path': '/v2/agents/{uuid}/environments/{env}/variables/{key}', 'path_params': ['uuid', 'env', 'key'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'compat_v2_delete_variable': {'method': 'DELETE', 'path': '/v2/agents/{uuid}/environments/{env}/variables/{key}', 'path_params': ['uuid', 'env', 'key'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_list_experiments': {'method': 'GET', 'path': '/v2/agents/{uuid}/experiments', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'create_experiment': {'method': 'POST', 'path': '/v2/agents/{uuid}/experiments', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'get_experiment': {'method': 'GET', 'path': '/v2/agents/{uuid}/experiments/{experiment_id}', 'path_params': ['uuid', 'experiment_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'update_experiment': {'method': 'PATCH', 'path': '/v2/agents/{uuid}/experiments/{experiment_id}', 'path_params': ['uuid', 'experiment_id'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'get_experiment_results': {'method': 'GET', 'path': '/v2/agents/{uuid}/experiments/{experiment_id}/results', 'path_params': ['uuid', 'experiment_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'stop_experiment': {'method': 'POST', 'path': '/v2/agents/{uuid}/experiments/{experiment_id}/stop', 'path_params': ['uuid', 'experiment_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_get_inbound': {'method': 'GET', 'path': '/v2/agents/{uuid}/inbound', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'organize_agent_pathways': {'method': 'POST', 'path': '/v2/agents/{uuid}/pathway-organization', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'list_agent_scenarios': {'method': 'GET', 'path': '/v2/agents/{uuid}/scenarios', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'create_agent_scenario': {'method': 'POST', 'path': '/v2/agents/{uuid}/scenarios', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'compat_v2_get_agent_scenario_history': {'method': 'GET', 'path': '/v2/agents/{uuid}/scenarios/agent/history', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'get_agent_scenario': {'method': 'GET', 'path': '/v2/agents/{uuid}/scenarios/{scenario_uuid}', 'path_params': ['uuid', 'scenario_uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'update_agent_scenario': {'method': 'POST', 'path': '/v2/agents/{uuid}/scenarios/{scenario_uuid}', 'path_params': ['uuid', 'scenario_uuid'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'delete_agent_scenario': {'method': 'DELETE', 'path': '/v2/agents/{uuid}/scenarios/{scenario_uuid}', 'path_params': ['uuid', 'scenario_uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'archive_agent_scenario': {'method': 'POST', 'path': '/v2/agents/{uuid}/scenarios/{scenario_uuid}/archive', 'path_params': ['uuid', 'scenario_uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'copy_agent_scenario': {'method': 'POST', 'path': '/v2/agents/{uuid}/scenarios/{scenario_uuid}/copy', 'path_params': ['uuid', 'scenario_uuid'], 'query': [], 'idempotent': False, 'body': 'json', 'response': 'json'},
    'compat_v2_get_scenario_history': {'method': 'GET', 'path': '/v2/agents/{uuid}/scenarios/{scenario_uuid}/history', 'path_params': ['uuid', 'scenario_uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'restore_agent_scenario': {'method': 'POST', 'path': '/v2/agents/{uuid}/scenarios/{scenario_uuid}/restore', 'path_params': ['uuid', 'scenario_uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_list_versions': {'method': 'GET', 'path': '/v2/agents/{uuid}/versions', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_get_latest_version': {'method': 'GET', 'path': '/v2/agents/{uuid}/versions/latest', 'path_params': ['uuid'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_get_analytics_overview': {'method': 'GET', 'path': '/v2/analytics/overview', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'create_batch': {'method': 'POST', 'path': '/v2/batches/create', 'path_params': [], 'query': [], 'idempotent': True, 'body': None, 'response': 'json'},
    'compat_v2_list_batches': {'method': 'GET', 'path': '/v2/batches/list', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'compat_v2_get_batch_file_schema': {'method': 'GET', 'path': '/v2/batches/schema/files', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'get_batch': {'method': 'GET', 'path': '/v2/batches/{batch_id}', 'path_params': ['batch_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'get_batch_logs': {'method': 'GET', 'path': '/v2/batches/{batch_id}/logs', 'path_params': ['batch_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'advance_batch': {'method': 'POST', 'path': '/v2/batches/{batch_id}/run', 'path_params': ['batch_id'], 'query': [], 'idempotent': True, 'body': None, 'response': 'json'},
    'stop_batch': {'method': 'POST', 'path': '/v2/batches/{batch_id}/stop', 'path_params': ['batch_id'], 'query': [], 'idempotent': True, 'body': None, 'response': 'json'},
    'list_models_v2_public': {'method': 'GET', 'path': '/v2/models', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'list_workspace_scenarios': {'method': 'GET', 'path': '/v2/scenarios', 'path_params': [], 'query': ['agent_id'], 'idempotent': False, 'body': None, 'response': 'json'},
    'list_tts_models_v2': {'method': 'GET', 'path': '/v2/tts/models', 'path_params': [], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
    'get_tts_model_v2': {'method': 'GET', 'path': '/v2/tts/models/{model_id}', 'path_params': ['model_id'], 'query': [], 'idempotent': False, 'body': None, 'response': 'json'},
}


class Operations(SemperaCore):
    """One method per operation in the OpenAPI document."""

    def get_doc_page(self, page: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """A developer guide page (Markdown) (GET /docs/{page})"""
        return self._call(
            OPERATIONS['get_doc_page'],
            {'page': page},
            None,
            None,
            request_options,
        )

    def get_llms_txt(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Retrieval map for coding agents (GET /llms.txt)"""
        return self._call(
            OPERATIONS['get_llms_txt'],
            {},
            None,
            None,
            request_options,
        )

    def get_open_api(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """OpenAPI 3.1 document (GET /openapi.json)"""
        return self._call(
            OPERATIONS['get_open_api'],
            {},
            None,
            None,
            request_options,
        )

    def get_robots_txt(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Robots policy for the API host (GET /robots.txt)"""
        return self._call(
            OPERATIONS['get_robots_txt'],
            {},
            None,
            None,
            request_options,
        )

    def get_root(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """API front door (GET /v1)"""
        return self._call(
            OPERATIONS['get_root'],
            {},
            None,
            None,
            request_options,
        )

    def compat_list_agent_testing_scenarios(self, *, limit: Any = None, cursor: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility scenario list (GET /v1/agent-testing/scenarios, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_list_agent_testing_scenarios'],
            {'limit': limit, 'cursor': cursor},
            None,
            None,
            request_options,
        )

    def compat_list_scenario_eval_agents(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """The judges that score a test scenario's calls (GET /v1/agent-testing/scenarios/{uuid}/eval-agents, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_list_scenario_eval_agents'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def start_tornado_run(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Run bounded concurrent synthetic graph scenarios (POST /v1/agent-testing/tornado, scope tests:write)"""
        return self._call(
            OPERATIONS['start_tornado_run'],
            {},
            None,
            None,
            request_options,
        )

    def get_tornado_run(self, run_id: str, *, agent_id: Any, request_options: dict[str, Any] | None = None) -> Any:
        """Read a synthetic graph run receipt (GET /v1/agent-testing/tornado/{run_id}, scope tests:read)"""
        return self._call(
            OPERATIONS['get_tornado_run'],
            {'run_id': run_id, 'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def list_agents(self, *, status: Any = None, limit: Any = None, cursor: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """List agents (GET /v1/agents, scope agents:read)"""
        return self._call(
            OPERATIONS['list_agents'],
            {'status': status, 'limit': limit, 'cursor': cursor},
            None,
            None,
            request_options,
        )

    def create_agent(self, body, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Create an agent (POST /v1/agents, scope agents:write)"""
        return self._call(
            OPERATIONS['create_agent'],
            {},
            body,
            idempotency_key,
            request_options,
        )

    def get_agent(self, agent_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Get an agent (GET /v1/agents/{agent_id}, scope agents:read)"""
        return self._call(
            OPERATIONS['get_agent'],
            {'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def delete_agent(self, agent_id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Delete an agent (irreversible) (DELETE /v1/agents/{agent_id}, scope agents:write)"""
        return self._call(
            OPERATIONS['delete_agent'],
            {'agent_id': agent_id},
            body,
            None,
            request_options,
        )

    def archive_agent(self, agent_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Archive (reversible) (POST /v1/agents/{agent_id}/archive, scope agents:write)"""
        return self._call(
            OPERATIONS['archive_agent'],
            {'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def get_api_chat_channel(self, agent_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Read API chat channel (GET /v1/agents/{agent_id}/channels/api-chat, scope agents:read)"""
        return self._call(
            OPERATIONS['get_api_chat_channel'],
            {'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def update_api_chat_channel(self, agent_id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Enable or disable API chat (PATCH /v1/agents/{agent_id}/channels/api-chat, scope agents:write)"""
        return self._call(
            OPERATIONS['update_api_chat_channel'],
            {'agent_id': agent_id},
            body,
            None,
            request_options,
        )

    def send_api_chat_message(self, agent_id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Send a message to the published agent (POST /v1/agents/{agent_id}/chat, scope sessions:write)"""
        return self._call(
            OPERATIONS['send_api_chat_message'],
            {'agent_id': agent_id},
            body,
            None,
            request_options,
        )

    def list_agent_deployments(self, agent_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Deployment ledger (GET /v1/agents/{agent_id}/deployments, scope agents:read)"""
        return self._call(
            OPERATIONS['list_agent_deployments'],
            {'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def list_dialing_pools(self, agent_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """List dialing pools and owned number readiness (GET /v1/agents/{agent_id}/dialing-pools, scope calls:read)"""
        return self._call(
            OPERATIONS['list_dialing_pools'],
            {'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def create_dialing_pool(self, agent_id: str, body, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Create an owned number pool (POST /v1/agents/{agent_id}/dialing-pools, scope calls:write)"""
        return self._call(
            OPERATIONS['create_dialing_pool'],
            {'agent_id': agent_id},
            body,
            idempotency_key,
            request_options,
        )

    def get_dialing_pool(self, agent_id: str, pool_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Read a dialing pool (GET /v1/agents/{agent_id}/dialing-pools/{pool_id}, scope calls:read)"""
        return self._call(
            OPERATIONS['get_dialing_pool'],
            {'agent_id': agent_id, 'pool_id': pool_id},
            None,
            None,
            request_options,
        )

    def preview_dialing_pool(self, agent_id: str, pool_id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Preview caller ID without dialing or reserving (POST /v1/agents/{agent_id}/dialing-pools/{pool_id}/preview, scope calls:write)"""
        return self._call(
            OPERATIONS['preview_dialing_pool'],
            {'agent_id': agent_id, 'pool_id': pool_id},
            body,
            None,
            request_options,
        )

    def update_dialing_pool(self, agent_id: str, pool_id: str, body, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Replace dialing pool settings (POST /v1/agents/{agent_id}/dialing-pools/{pool_id}/update, scope calls:write)"""
        return self._call(
            OPERATIONS['update_dialing_pool'],
            {'agent_id': agent_id, 'pool_id': pool_id},
            body,
            idempotency_key,
            request_options,
        )

    def get_agent_draft(self, agent_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Read the draft (GET /v1/agents/{agent_id}/draft, scope agents:read)"""
        return self._call(
            OPERATIONS['get_agent_draft'],
            {'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def patch_agent_draft(self, agent_id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Edit the draft (PATCH /v1/agents/{agent_id}/draft, scope agents:write)"""
        return self._call(
            OPERATIONS['patch_agent_draft'],
            {'agent_id': agent_id},
            body,
            None,
            request_options,
        )

    def discard_agent_draft(self, agent_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Discard the draft (DELETE /v1/agents/{agent_id}/draft, scope agents:write)"""
        return self._call(
            OPERATIONS['discard_agent_draft'],
            {'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def get_agent_identity(self, agent_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Read agent business identity (GET /v1/agents/{agent_id}/identity, scope agents:read)"""
        return self._call(
            OPERATIONS['get_agent_identity'],
            {'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def save_agent_identity(self, agent_id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Save agent contact card and business details (PUT /v1/agents/{agent_id}/identity, scope agents:write)"""
        return self._call(
            OPERATIONS['save_agent_identity'],
            {'agent_id': agent_id},
            body,
            None,
            request_options,
        )

    def test_agent_contact_card(self, agent_id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Check the contact card delivery boundary (POST /v1/agents/{agent_id}/identity/send-test, scope agents:write)"""
        return self._call(
            OPERATIONS['test_agent_contact_card'],
            {'agent_id': agent_id},
            body,
            None,
            request_options,
        )

    def download_agent_contact_card(self, agent_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Download agent contact card (GET /v1/agents/{agent_id}/identity/vcard, scope agents:read)"""
        return self._call(
            OPERATIONS['download_agent_contact_card'],
            {'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def request_agent_identity_review(self, agent_id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Record a business identity review request (POST /v1/agents/{agent_id}/identity/verification, scope agents:write)"""
        return self._call(
            OPERATIONS['request_agent_identity_review'],
            {'agent_id': agent_id},
            body,
            None,
            request_options,
        )

    def get_knowledge_retrieval_settings(self, agent_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Read version-bound knowledge retrieval settings (GET /v1/agents/{agent_id}/knowledge/retrieval-settings, scope knowledge:read)"""
        return self._call(
            OPERATIONS['get_knowledge_retrieval_settings'],
            {'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def save_knowledge_retrieval_settings(self, agent_id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Stage knowledge retrieval settings in the agent draft (PUT /v1/agents/{agent_id}/knowledge/retrieval-settings, scope knowledge:write)"""
        return self._call(
            OPERATIONS['save_knowledge_retrieval_settings'],
            {'agent_id': agent_id},
            body,
            None,
            request_options,
        )

    def enable_memory(self, agent_id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Enable or disable memory in the agent draft (PATCH /v1/agents/{agent_id}/memory, scope agents:write)"""
        return self._call(
            OPERATIONS['enable_memory'],
            {'agent_id': agent_id},
            body,
            None,
            request_options,
        )

    def get_agent_memory_schema(self, agent_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Inferred caller-memory schema (GET /v1/agents/{agent_id}/memory/schema, scope agents:read)"""
        return self._call(
            OPERATIONS['get_agent_memory_schema'],
            {'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def messaging_setup(self, agent_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Messaging channel setup (GET /v1/agents/{agent_id}/messaging, scope calls:read)"""
        return self._call(
            OPERATIONS['messaging_setup'],
            {'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def messaging_conversations(self, agent_id: str, channel: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """List channel conversations (GET /v1/agents/{agent_id}/messaging/{channel}/conversations, scope calls:read)"""
        return self._call(
            OPERATIONS['messaging_conversations'],
            {'agent_id': agent_id, 'channel': channel},
            None,
            None,
            request_options,
        )

    def messaging_conversation(self, agent_id: str, channel: str, conversation_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Read channel conversation (GET /v1/agents/{agent_id}/messaging/{channel}/conversations/{conversation_id}, scope calls:read)"""
        return self._call(
            OPERATIONS['messaging_conversation'],
            {'agent_id': agent_id, 'channel': channel, 'conversation_id': conversation_id},
            None,
            None,
            request_options,
        )

    def messaging_send_admission(self, agent_id: str, channel: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Check channel send admission (POST /v1/agents/{agent_id}/messaging/{channel}/messages, scope calls:write)"""
        return self._call(
            OPERATIONS['messaging_send_admission'],
            {'agent_id': agent_id, 'channel': channel},
            None,
            None,
            request_options,
        )

    def preview_agent(self, agent_id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Typed preview turn (POST /v1/agents/{agent_id}/preview, scope agents:write)"""
        return self._call(
            OPERATIONS['preview_agent'],
            {'agent_id': agent_id},
            body,
            None,
            request_options,
        )

    def publish_agent(self, agent_id: str, body, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Publish a new immutable version (POST /v1/agents/{agent_id}/publish, scope agents:publish)"""
        return self._call(
            OPERATIONS['publish_agent'],
            {'agent_id': agent_id},
            body,
            idempotency_key,
            request_options,
        )

    def rollback_agent(self, agent_id: str, body, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Roll back to a previous deployment (POST /v1/agents/{agent_id}/rollback, scope agents:publish)"""
        return self._call(
            OPERATIONS['rollback_agent'],
            {'agent_id': agent_id},
            body,
            idempotency_key,
            request_options,
        )

    def run_agent_simulations(self, agent_id: str, body, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Run an offline simulation set (POST /v1/agents/{agent_id}/simulations, scope tests:write)"""
        return self._call(
            OPERATIONS['run_agent_simulations'],
            {'agent_id': agent_id},
            body,
            idempotency_key,
            request_options,
        )

    def get_agent_simulation(self, agent_id: str, simulation_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Read an offline simulation set (GET /v1/agents/{agent_id}/simulations/{simulation_id}, scope tests:read)"""
        return self._call(
            OPERATIONS['get_agent_simulation'],
            {'agent_id': agent_id, 'simulation_id': simulation_id},
            None,
            None,
            request_options,
        )

    def unarchive_agent(self, agent_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Restore an archived agent (POST /v1/agents/{agent_id}/unarchive, scope agents:write)"""
        return self._call(
            OPERATIONS['unarchive_agent'],
            {'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def list_agent_versions(self, agent_id: str, *, limit: Any = None, cursor: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """List published versions (GET /v1/agents/{agent_id}/versions, scope agents:read)"""
        return self._call(
            OPERATIONS['list_agent_versions'],
            {'agent_id': agent_id, 'limit': limit, 'cursor': cursor},
            None,
            None,
            request_options,
        )

    def save_agent_version(self, agent_id: str, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Save a version of the approved agent specification (POST /v1/agents/{agent_id}/versions, scope agents:write)"""
        return self._call(
            OPERATIONS['save_agent_version'],
            {'agent_id': agent_id},
            None,
            idempotency_key,
            request_options,
        )

    def get_agent_version(self, agent_id: str, version_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Get a version (GET /v1/agents/{agent_id}/versions/{version_id}, scope agents:read)"""
        return self._call(
            OPERATIONS['get_agent_version'],
            {'agent_id': agent_id, 'version_id': version_id},
            None,
            None,
            request_options,
        )

    def compat_list_alerts(self, *, limit: Any = None, page: Any = None, sort: Any = None, direction: Any = None, agent_id: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """List this organization's metric alert rules (GET /v1/alerts, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_list_alerts'],
            {'limit': limit, 'page': page, 'sort': sort, 'direction': direction, 'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def create_alert(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Create a metric alert rule (POST /v1/alerts, scope agents:write)"""
        return self._call(
            OPERATIONS['create_alert'],
            {},
            body,
            None,
            request_options,
        )

    def list_alert_metrics(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Metrics and channels an alert rule may use (GET /v1/alerts/metrics, scope agents:read)"""
        return self._call(
            OPERATIONS['list_alert_metrics'],
            {},
            None,
            None,
            request_options,
        )

    def preview_alert(self, body, *, hours: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """Preview an alert without saving or notifying (POST /v1/alerts/preview, scope agents:write)"""
        return self._call(
            OPERATIONS['preview_alert'],
            {'hours': hours},
            body,
            None,
            request_options,
        )

    def get_alert(self, id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Get a metric alert rule and its trigger log (GET /v1/alerts/{id}, scope agents:read)"""
        return self._call(
            OPERATIONS['get_alert'],
            {'id': id},
            None,
            None,
            request_options,
        )

    def update_alert(self, id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Update a metric alert rule (PATCH /v1/alerts/{id}, scope agents:write)"""
        return self._call(
            OPERATIONS['update_alert'],
            {'id': id},
            body,
            None,
            request_options,
        )

    def delete_alert(self, id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Delete a metric alert rule (DELETE /v1/alerts/{id}, scope agents:write)"""
        return self._call(
            OPERATIONS['delete_alert'],
            {'id': id},
            None,
            None,
            request_options,
        )

    def evaluate_alert(self, id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Evaluate a metric alert rule now (POST /v1/alerts/{id}/evaluate, scope agents:write)"""
        return self._call(
            OPERATIONS['evaluate_alert'],
            {'id': id},
            None,
            None,
            request_options,
        )

    def list_api_keys(self, *, status: Any = None, limit: Any = None, cursor: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """List API keys (GET /v1/api-keys, scope api_keys:read)"""
        return self._call(
            OPERATIONS['list_api_keys'],
            {'status': status, 'limit': limit, 'cursor': cursor},
            None,
            None,
            request_options,
        )

    def create_api_key(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Create an API key (secret shown once) (POST /v1/api-keys, scope api_keys:write)"""
        return self._call(
            OPERATIONS['create_api_key'],
            {},
            body,
            None,
            request_options,
        )

    def get_api_key(self, key_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Get an API key (GET /v1/api-keys/{key_id}, scope api_keys:read)"""
        return self._call(
            OPERATIONS['get_api_key'],
            {'key_id': key_id},
            None,
            None,
            request_options,
        )

    def rename_api_key(self, key_id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Rename an API key (PATCH /v1/api-keys/{key_id}, scope api_keys:write)"""
        return self._call(
            OPERATIONS['rename_api_key'],
            {'key_id': key_id},
            body,
            None,
            request_options,
        )

    def revoke_api_key(self, key_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Revoke an API key (DELETE /v1/api-keys/{key_id}, scope api_keys:write)"""
        return self._call(
            OPERATIONS['revoke_api_key'],
            {'key_id': key_id},
            None,
            None,
            request_options,
        )

    def compat_list_automation_events(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Events a trigger can listen for (GET /v1/automation/events, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_list_automation_events'],
            {},
            None,
            None,
            request_options,
        )

    def list_automation_executions(self, *, limit: Any = None, offset: Any = None, status: Any = None, trigger_id: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """List trigger executions (GET /v1/automation/executions, scope agents:read)"""
        return self._call(
            OPERATIONS['list_automation_executions'],
            {'limit': limit, 'offset': offset, 'status': status, 'trigger_id': trigger_id},
            None,
            None,
            request_options,
        )

    def get_automation_execution(self, id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Get a trigger execution (GET /v1/automation/executions/{id}, scope agents:read)"""
        return self._call(
            OPERATIONS['get_automation_execution'],
            {'id': id},
            None,
            None,
            request_options,
        )

    def retry_automation_execution(self, id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Send a failed or stalled webhook or tool run again, once (POST /v1/automation/executions/{id}/retry, scope agents:write)"""
        return self._call(
            OPERATIONS['retry_automation_execution'],
            {'id': id},
            None,
            None,
            request_options,
        )

    def create_automation_pipeline(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Create a trigger (one record) (POST /v1/automation/pipelines, scope agents:write)"""
        return self._call(
            OPERATIONS['create_automation_pipeline'],
            {},
            body,
            None,
            request_options,
        )

    def compat_list_automation_triggers(self, *, limit: Any = None, offset: Any = None, sort: Any = None, agent_id: Any = None, event: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """List this organization's triggers (GET /v1/automation/triggers, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_list_automation_triggers'],
            {'limit': limit, 'offset': offset, 'sort': sort, 'agent_id': agent_id, 'event': event},
            None,
            None,
            request_options,
        )

    def create_automation_trigger(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Create a trigger (POST /v1/automation/triggers, scope agents:write)"""
        return self._call(
            OPERATIONS['create_automation_trigger'],
            {},
            body,
            None,
            request_options,
        )

    def get_automation_trigger(self, id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Get a trigger (GET /v1/automation/triggers/{id}, scope agents:read)"""
        return self._call(
            OPERATIONS['get_automation_trigger'],
            {'id': id},
            None,
            None,
            request_options,
        )

    def update_automation_trigger(self, id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Update, pause or resume a trigger (PATCH /v1/automation/triggers/{id}, scope agents:write)"""
        return self._call(
            OPERATIONS['update_automation_trigger'],
            {'id': id},
            body,
            None,
            request_options,
        )

    def delete_automation_trigger(self, id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Delete a trigger (DELETE /v1/automation/triggers/{id}, scope agents:write)"""
        return self._call(
            OPERATIONS['delete_automation_trigger'],
            {'id': id},
            None,
            None,
            request_options,
        )

    def list_automation_trigger_executions(self, id: str, *, limit: Any = None, offset: Any = None, status: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """A trigger's executions (GET /v1/automation/triggers/{id}/executions, scope agents:read)"""
        return self._call(
            OPERATIONS['list_automation_trigger_executions'],
            {'id': id, 'limit': limit, 'offset': offset, 'status': status},
            None,
            None,
            request_options,
        )

    def test_automation_trigger(self, id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Dry-run a trigger against a sample event (nothing is delivered) (POST /v1/automation/triggers/{id}/test, scope agents:write)"""
        return self._call(
            OPERATIONS['test_automation_trigger'],
            {'id': id},
            body,
            None,
            request_options,
        )

    def compat_check_byot(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility BYOT check (POST /v1/byot/manage/check, scope agents:write)"""
        return self._call(
            OPERATIONS['compat_check_byot'],
            {},
            None,
            None,
            request_options,
        )

    def list_calls(self, *, agent_id: Any, limit: Any = None, cursor: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """List phone calls for an agent (GET /v1/calls, scope calls:read)"""
        return self._call(
            OPERATIONS['list_calls'],
            {'agent_id': agent_id, 'limit': limit, 'cursor': cursor},
            None,
            None,
            request_options,
        )

    def create_call(self, body, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Create an outbound call (POST /v1/calls, scope calls:write)"""
        return self._call(
            OPERATIONS['create_call'],
            {},
            body,
            idempotency_key,
            request_options,
        )

    def compat_list_active_calls(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility active calls (GET /v1/calls/active, scope calls:read)"""
        return self._call(
            OPERATIONS['compat_list_active_calls'],
            {},
            None,
            None,
            request_options,
        )

    def stop_active_calls(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Stop all active phone calls in this credential's scope (POST /v1/calls/active/stop, scope calls:write)"""
        return self._call(
            OPERATIONS['stop_active_calls'],
            {},
            body,
            None,
            request_options,
        )

    def compat_stream_active_calls(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility active calls stream (GET /v1/calls/active/stream, scope calls:read)"""
        return self._call(
            OPERATIONS['compat_stream_active_calls'],
            {},
            None,
            None,
            request_options,
        )

    def transfer_active_call(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Transfer an active phone call (POST /v1/calls/active/transfer, scope calls:write)"""
        return self._call(
            OPERATIONS['transfer_active_call'],
            {},
            body,
            None,
            request_options,
        )

    def get_call(self, call_id: str, *, agent_id: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """Get a phone call (GET /v1/calls/{call_id}, scope calls:read)"""
        return self._call(
            OPERATIONS['get_call'],
            {'call_id': call_id, 'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def analyze_call(self, call_id: str, body, *, agent_id: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """Ask questions about a finished phone call (POST /v1/calls/{call_id}/analyze, scope calls:read)"""
        return self._call(
            OPERATIONS['analyze_call'],
            {'call_id': call_id, 'agent_id': agent_id},
            body,
            None,
            request_options,
        )

    def get_corrected_transcript(self, call_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Read a corrected transcript with speaker labels and turn confidence (GET /v1/calls/{call_id}/corrected-transcript, scope calls:read)"""
        return self._call(
            OPERATIONS['get_corrected_transcript'],
            {'call_id': call_id},
            None,
            None,
            request_options,
        )

    def import_corrected_transcript(self, call_id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Import a corrected transcript; it reads as an unverified owner import (POST /v1/calls/{call_id}/corrected-transcript, scope calls:write)"""
        return self._call(
            OPERATIONS['import_corrected_transcript'],
            {'call_id': call_id},
            body,
            None,
            request_options,
        )

    def stop_call(self, call_id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Stop one active phone call (POST /v1/calls/{call_id}/stop, scope calls:write)"""
        return self._call(
            OPERATIONS['stop_call'],
            {'call_id': call_id},
            body,
            None,
            request_options,
        )

    def list_citation_schemas(self, *, limit: Any = None, cursor: Any = None, agent_id: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """List citation schemas (GET /v1/citation_schemas, scope agents:read)"""
        return self._call(
            OPERATIONS['list_citation_schemas'],
            {'limit': limit, 'cursor': cursor, 'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def backfill_citation_schemas(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Score extraction quality over call history (POST /v1/citation_schemas/backfill, scope agents:write)"""
        return self._call(
            OPERATIONS['backfill_citation_schemas'],
            {},
            body,
            None,
            request_options,
        )

    def list_citation_schemas_list_path(self, *, limit: Any = None, cursor: Any = None, agent_id: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """List citation schemas (the /list path) (GET /v1/citation_schemas/list, scope agents:read)"""
        return self._call(
            OPERATIONS['list_citation_schemas_list_path'],
            {'limit': limit, 'cursor': cursor, 'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def list_client_grants(self, *, status: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """List connected clients (GET /v1/client-grants, scope api_keys:read)"""
        return self._call(
            OPERATIONS['list_client_grants'],
            {'status': status},
            None,
            None,
            request_options,
        )

    def create_client_rest_credential(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Create a scoped REST credential (secret shown once) (POST /v1/client-grants/rest, scope api_keys:write)"""
        return self._call(
            OPERATIONS['create_client_rest_credential'],
            {},
            body,
            None,
            request_options,
        )

    def revoke_client_grant(self, grant_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Disconnect one client (DELETE /v1/client-grants/{grant_id}, scope api_keys:write)"""
        return self._call(
            OPERATIONS['revoke_client_grant'],
            {'grant_id': grant_id},
            None,
            None,
            request_options,
        )

    def compat_app_list_analysis_presets(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Console compatibility analysis presets (GET /v1/compat/app/analysis_presets, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_app_list_analysis_presets'],
            {},
            None,
            None,
            request_options,
        )

    def compat_app_get_session(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Console compatibility session (GET /v1/compat/app/authorization/get-session, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_app_get_session'],
            {},
            None,
            None,
            request_options,
        )

    def compat_app_get_agent_phone_billing(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Console compatibility phone billing (GET /v1/compat/app/billing/agent_phone, scope organizations:read)"""
        return self._call(
            OPERATIONS['compat_app_get_agent_phone_billing'],
            {},
            None,
            None,
            request_options,
        )

    def compat_app_get_customer_billing(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Console compatibility customer billing (GET /v1/compat/app/billing/customer, scope organizations:read)"""
        return self._call(
            OPERATIONS['compat_app_get_customer_billing'],
            {},
            None,
            None,
            request_options,
        )

    def compat_app_list_byot(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Console compatibility BYOT list (GET /v1/compat/app/byot/get, scope phone_numbers:read)"""
        return self._call(
            OPERATIONS['compat_app_list_byot'],
            {},
            None,
            None,
            request_options,
        )

    def compat_app_read_call_config(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Console compatibility call configs (GET /v1/compat/app/call_config/read, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_app_read_call_config'],
            {},
            None,
            None,
            request_options,
        )

    def compat_app_list_dashboards(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Console compatibility dashboards (GET /v1/compat/app/dashboards/list, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_app_list_dashboards'],
            {},
            None,
            None,
            request_options,
        )

    def compat_app_list_inbound(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Console compatibility inbound numbers (GET /v1/compat/app/inbound/get_inbound, scope phone_numbers:read)"""
        return self._call(
            OPERATIONS['compat_app_list_inbound'],
            {},
            None,
            None,
            request_options,
        )

    def compat_app_list_keys(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Console compatibility key list (POST /v1/compat/app/keys/list, scope api_keys:write)"""
        return self._call(
            OPERATIONS['compat_app_list_keys'],
            {},
            body,
            None,
            request_options,
        )

    def compat_app_get_org_billing(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Console compatibility org billing (GET /v1/compat/app/orgs/{uuid}/billing, scope organizations:read)"""
        return self._call(
            OPERATIONS['compat_app_get_org_billing'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def compat_app_list_org_invites(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Console compatibility org invites (GET /v1/compat/app/orgs/{uuid}/invites, scope organizations:read)"""
        return self._call(
            OPERATIONS['compat_app_list_org_invites'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def compat_app_list_org_members(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Console compatibility org members (GET /v1/compat/app/orgs/{uuid}/members, scope organizations:read)"""
        return self._call(
            OPERATIONS['compat_app_list_org_members'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def compat_app_create_purchase(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Console compatibility purchases (POST /v1/compat/app/pay/purchases, scope workspaces:write)"""
        return self._call(
            OPERATIONS['compat_app_create_purchase'],
            {},
            body,
            None,
            request_options,
        )

    def compat_app_get_current_webhook(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Console compatibility webhook (GET /v1/compat/app/user/getCurrentWebhook, scope webhooks:read)"""
        return self._call(
            OPERATIONS['compat_app_get_current_webhook'],
            {},
            None,
            None,
            request_options,
        )

    def compat_app_list_user_logs(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Console compatibility call logs (GET /v1/compat/app/user/logs, scope calls:read)"""
        return self._call(
            OPERATIONS['compat_app_list_user_logs'],
            {},
            None,
            None,
            request_options,
        )

    def compat_app_get_user_log(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Console compatibility call log (GET /v1/compat/app/user/logs/{uuid}, scope calls:read)"""
        return self._call(
            OPERATIONS['compat_app_get_user_log'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def compat_app_get_user_log_enrich(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Console compatibility enriched call log (GET /v1/compat/app/user/logs/{uuid}/enrich, scope calls:read)"""
        return self._call(
            OPERATIONS['compat_app_get_user_log_enrich'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def compat_app_get_rate_limits(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Console compatibility rate limits (GET /v1/compat/app/user/rateLimits, scope organizations:read)"""
        return self._call(
            OPERATIONS['compat_app_get_rate_limits'],
            {},
            None,
            None,
            request_options,
        )

    def compat_app_get_user(self, id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Console compatibility missing user (GET /v1/compat/app/user/{id}, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_app_get_user'],
            {'id': id},
            None,
            None,
            request_options,
        )

    def compat_app_get_knowledge_asset(self, org_uuid: str, kb_uuid: str, asset_uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Console compatibility knowledge asset (GET /v1/compat/app/{org_uuid}/kb/{kb_uuid}/{asset_uuid}, scope knowledge:read)"""
        return self._call(
            OPERATIONS['compat_app_get_knowledge_asset'],
            {'org_uuid': org_uuid, 'kb_uuid': kb_uuid, 'asset_uuid': asset_uuid},
            None,
            None,
            request_options,
        )

    def compat_list_contacts(self, *, limit: Any = None, cursor: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility contacts (GET /v1/contacts, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_list_contacts'],
            {'limit': limit, 'cursor': cursor},
            None,
            None,
            request_options,
        )

    def merge_contacts(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Merge console contact profiles (POST /v1/contacts/merge, scope agents:write)"""
        return self._call(
            OPERATIONS['merge_contacts'],
            {},
            body,
            None,
            request_options,
        )

    def resolve_contact(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Resolve a workspace contact without guessing (POST /v1/contacts/resolve, scope agents:read)"""
        return self._call(
            OPERATIONS['resolve_contact'],
            {},
            body,
            None,
            request_options,
        )

    def get_contact_schema(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Read organisation contact schema (GET /v1/contacts/schema, scope agents:read)"""
        return self._call(
            OPERATIONS['get_contact_schema'],
            {},
            None,
            None,
            request_options,
        )

    def save_contact_schema(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Save organisation contact schema (PUT /v1/contacts/schema, scope agents:write)"""
        return self._call(
            OPERATIONS['save_contact_schema'],
            {},
            body,
            None,
            request_options,
        )

    def compat_get_contact(self, contact_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility contact detail (GET /v1/contacts/{contact_id}, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_get_contact'],
            {'contact_id': contact_id},
            None,
            None,
            request_options,
        )

    def compat_get_migration_split(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility migration flag (GET /v1/convo_pathway/migration_split/enabled, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_get_migration_split'],
            {},
            None,
            None,
            request_options,
        )

    def get_credit_balance(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Read the workspace's credit balance (GET /v1/credits, scope organizations:read)"""
        return self._call(
            OPERATIONS['get_credit_balance'],
            {},
            None,
            None,
            request_options,
        )

    def list_credit_history(self, *, limit: Any = None, before: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """List the workspace's credit history (GET /v1/credits/history, scope organizations:read)"""
        return self._call(
            OPERATIONS['list_credit_history'],
            {'limit': limit, 'before': before},
            None,
            None,
            request_options,
        )

    def compat_list_dispositions(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """List this workspace's dispositions (GET /v1/dispositions/, scope evals:read)"""
        return self._call(
            OPERATIONS['compat_list_dispositions'],
            {},
            None,
            None,
            request_options,
        )

    def list_evals(self, *, status: Any = None, limit: Any = None, cursor: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """List eval criteria (GET /v1/evals, scope evals:read)"""
        return self._call(
            OPERATIONS['list_evals'],
            {'status': status, 'limit': limit, 'cursor': cursor},
            None,
            None,
            request_options,
        )

    def create_eval(self, body, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Create an eval criterion (POST /v1/evals, scope evals:write)"""
        return self._call(
            OPERATIONS['create_eval'],
            {},
            body,
            idempotency_key,
            request_options,
        )

    def compat_list_eval_agent_templates(self, *, limit: Any = None, cursor: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """Judge templates Sempera ships (GET /v1/evals/agent-templates, scope evals:read)"""
        return self._call(
            OPERATIONS['compat_list_eval_agent_templates'],
            {'limit': limit, 'cursor': cursor},
            None,
            None,
            request_options,
        )

    def compat_list_eval_agents(self, *, limit: Any = None, cursor: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """This workspace's judges with their latest run (GET /v1/evals/agents, scope evals:read)"""
        return self._call(
            OPERATIONS['compat_list_eval_agents'],
            {'limit': limit, 'cursor': cursor},
            None,
            None,
            request_options,
        )

    def quick_run_eval_template(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Score one judge template against an agent's recent calls (not saved) (POST /v1/evals/quick-run, scope evals:write)"""
        return self._call(
            OPERATIONS['quick_run_eval_template'],
            {},
            None,
            None,
            request_options,
        )

    def get_eval_results(self, *, agent_id: Any, request_options: dict[str, Any] | None = None) -> Any:
        """Eval results for an agent (GET /v1/evals/results, scope evals:read)"""
        return self._call(
            OPERATIONS['get_eval_results'],
            {'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def run_evals(self, body, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Judge an agent's completed conversations (POST /v1/evals/run, scope evals:write)"""
        return self._call(
            OPERATIONS['run_evals'],
            {},
            body,
            idempotency_key,
            request_options,
        )

    def list_eval_runs(self, *, agent_id: Any = None, status: Any = None, since: Any = None, until: Any = None, limit: Any = None, cursor: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """Evaluation runs of this workspace's agents (GET /v1/evals/runs, scope evals:read)"""
        return self._call(
            OPERATIONS['list_eval_runs'],
            {'agent_id': agent_id, 'status': status, 'since': since, 'until': until, 'limit': limit, 'cursor': cursor},
            None,
            None,
            request_options,
        )

    def get_eval_run(self, run_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """One evaluation run with its results (GET /v1/evals/runs/{run_id}, scope evals:read)"""
        return self._call(
            OPERATIONS['get_eval_run'],
            {'run_id': run_id},
            None,
            None,
            request_options,
        )

    def list_eval_test_cases(self, *, agent_id: Any = None, limit: Any = None, cursor: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """Calls a judge can score, with their verdicts (GET /v1/evals/test-cases, scope evals:read)"""
        return self._call(
            OPERATIONS['list_eval_test_cases'],
            {'agent_id': agent_id, 'limit': limit, 'cursor': cursor},
            None,
            None,
            request_options,
        )

    def compat_list_eval_user_templates(self, *, limit: Any = None, cursor: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """Saved judge suites for this workspace (GET /v1/evals/user-templates, scope evals:read)"""
        return self._call(
            OPERATIONS['compat_list_eval_user_templates'],
            {'limit': limit, 'cursor': cursor},
            None,
            None,
            request_options,
        )

    def create_eval_user_template(self, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Save a judge suite (a named bundle of templates for one agent) (POST /v1/evals/user-templates, scope evals:write)"""
        return self._call(
            OPERATIONS['create_eval_user_template'],
            {},
            None,
            idempotency_key,
            request_options,
        )

    def get_eval(self, eval_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Get an eval criterion (GET /v1/evals/{eval_id}, scope evals:read)"""
        return self._call(
            OPERATIONS['get_eval'],
            {'eval_id': eval_id},
            None,
            None,
            request_options,
        )

    def update_eval(self, eval_id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Update an eval criterion (PATCH /v1/evals/{eval_id}, scope evals:write)"""
        return self._call(
            OPERATIONS['update_eval'],
            {'eval_id': eval_id},
            body,
            None,
            request_options,
        )

    def delete_eval(self, eval_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Archive an eval criterion (DELETE /v1/evals/{eval_id}, scope evals:write)"""
        return self._call(
            OPERATIONS['delete_eval'],
            {'eval_id': eval_id},
            None,
            None,
            request_options,
        )

    def align_judge(self, eval_id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Propose judge tuning from corrected production-call verdicts; save nothing (POST /v1/evals/{eval_id}/align, scope evals:write)"""
        return self._call(
            OPERATIONS['align_judge'],
            {'eval_id': eval_id},
            body,
            None,
            request_options,
        )

    def list_judge_production_calls(self, eval_id: str, *, agent_id: Any, request_options: dict[str, Any] | None = None) -> Any:
        """Recent completed production calls available to this judge (GET /v1/evals/{eval_id}/production-calls, scope evals:read)"""
        return self._call(
            OPERATIONS['list_judge_production_calls'],
            {'eval_id': eval_id, 'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def run_production_judge(self, eval_id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Evaluate selected stored production calls without saving a second copy (POST /v1/evals/{eval_id}/production-run, scope evals:write)"""
        return self._call(
            OPERATIONS['run_production_judge'],
            {'eval_id': eval_id},
            body,
            None,
            request_options,
        )

    def compat_list_files(self, *, limit: Any = None, cursor: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility files list (GET /v1/files/list, scope knowledge:read)"""
        return self._call(
            OPERATIONS['compat_list_files'],
            {'limit': limit, 'cursor': cursor},
            None,
            None,
            request_options,
        )

    def get_health(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Liveness (GET /v1/health)"""
        return self._call(
            OPERATIONS['get_health'],
            {},
            None,
            None,
            request_options,
        )

    def list_integrations(self, *, limit: Any = None, cursor: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """List integrations (GET /v1/integrations, scope integrations:read)"""
        return self._call(
            OPERATIONS['list_integrations'],
            {'limit': limit, 'cursor': cursor},
            None,
            None,
            request_options,
        )

    def create_integration(self, body, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Create an integration (POST /v1/integrations, scope integrations:write)"""
        return self._call(
            OPERATIONS['create_integration'],
            {},
            body,
            idempotency_key,
            request_options,
        )

    def get_integration(self, integration_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility integration detail (GET /v1/integrations/{integration_id}, scope integrations:read)"""
        return self._call(
            OPERATIONS['get_integration'],
            {'integration_id': integration_id},
            None,
            None,
            request_options,
        )

    def update_integration(self, integration_id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Update an integration (PATCH /v1/integrations/{integration_id}, scope integrations:write)"""
        return self._call(
            OPERATIONS['update_integration'],
            {'integration_id': integration_id},
            body,
            None,
            request_options,
        )

    def delete_integration(self, integration_id: str, *, restore: Any = None, revision: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """Disable an integration (DELETE /v1/integrations/{integration_id}, scope integrations:write)"""
        return self._call(
            OPERATIONS['delete_integration'],
            {'integration_id': integration_id, 'restore': restore, 'revision': revision},
            None,
            None,
            request_options,
        )

    def list_integration_actions(self, integration_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility integration actions (GET /v1/integrations/{integration_id}/actions, scope integrations:read)"""
        return self._call(
            OPERATIONS['list_integration_actions'],
            {'integration_id': integration_id},
            None,
            None,
            request_options,
        )

    def verify_integration(self, integration_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Verify an integration's connection (POST /v1/integrations/{integration_id}/verify, scope integrations:write)"""
        return self._call(
            OPERATIONS['verify_integration'],
            {'integration_id': integration_id},
            None,
            None,
            request_options,
        )

    def list_knowledge_sources(self, *, agent_id: Any, limit: Any = None, cursor: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """List an agent's knowledge sources (GET /v1/knowledge-sources, scope knowledge:read)"""
        return self._call(
            OPERATIONS['list_knowledge_sources'],
            {'agent_id': agent_id, 'limit': limit, 'cursor': cursor},
            None,
            None,
            request_options,
        )

    def create_knowledge_source(self, body, *, agent_id: Any, request_options: dict[str, Any] | None = None) -> Any:
        """Upload a document (multipart) (POST /v1/knowledge-sources, scope knowledge:write)"""
        return self._call(
            OPERATIONS['create_knowledge_source'],
            {'agent_id': agent_id},
            body,
            None,
            request_options,
        )

    def create_text_knowledge_source(self, body, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Create a plain-text knowledge source (POST /v1/knowledge-sources/text, scope knowledge:write)"""
        return self._call(
            OPERATIONS['create_text_knowledge_source'],
            {},
            body,
            idempotency_key,
            request_options,
        )

    def update_knowledge_source(self, source_id: str, body, *, agent_id: Any, request_options: dict[str, Any] | None = None) -> Any:
        """Update a text source without publishing the agent (PATCH /v1/knowledge-sources/{source_id}, scope knowledge:write)"""
        return self._call(
            OPERATIONS['update_knowledge_source'],
            {'source_id': source_id, 'agent_id': agent_id},
            body,
            None,
            request_options,
        )

    def get_knowledge_source(self, source_id: str, *, agent_id: Any, request_options: dict[str, Any] | None = None) -> Any:
        """Get a knowledge source (GET /v1/knowledge-sources/{source_id}, scope knowledge:read)"""
        return self._call(
            OPERATIONS['get_knowledge_source'],
            {'source_id': source_id, 'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def delete_knowledge_source(self, source_id: str, *, agent_id: Any, request_options: dict[str, Any] | None = None) -> Any:
        """Remove a knowledge source (DELETE /v1/knowledge-sources/{source_id}, scope knowledge:write)"""
        return self._call(
            OPERATIONS['delete_knowledge_source'],
            {'source_id': source_id, 'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def reparse_knowledge_source(self, source_id: str, *, agent_id: Any, request_options: dict[str, Any] | None = None) -> Any:
        """Re-process a source (POST /v1/knowledge-sources/{source_id}/reparse, scope knowledge:write)"""
        return self._call(
            OPERATIONS['reparse_knowledge_source'],
            {'source_id': source_id, 'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def chat_knowledge(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Ask knowledge using local retrieval, with cited passages (POST /v1/knowledge/chat, scope knowledge:write)"""
        return self._call(
            OPERATIONS['chat_knowledge'],
            {},
            body,
            None,
            request_options,
        )

    def crawl_knowledge(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Read one public page or refresh a previously read page (POST /v1/knowledge/crawl, scope knowledge:write)"""
        return self._call(
            OPERATIONS['crawl_knowledge'],
            {},
            body,
            None,
            request_options,
        )

    def compat_get_knowledge_map(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility knowledge map (GET /v1/knowledge/map, scope knowledge:read)"""
        return self._call(
            OPERATIONS['compat_get_knowledge_map'],
            {},
            None,
            None,
            request_options,
        )

    def compat_list_knowledge_queries(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility knowledge queries (GET /v1/knowledge/queries, scope knowledge:read)"""
        return self._call(
            OPERATIONS['compat_list_knowledge_queries'],
            {},
            None,
            None,
            request_options,
        )

    def change_knowledge_question(self, question_id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Link, delete or dismiss a recorded knowledge question (PATCH /v1/knowledge/questions/{question_id}, scope knowledge:write)"""
        return self._call(
            OPERATIONS['change_knowledge_question'],
            {'question_id': question_id},
            body,
            None,
            request_options,
        )

    def answer_knowledge_question(self, question_id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Ingest an answer and resolve a recorded question (PUT /v1/knowledge/questions/{question_id}/answer, scope knowledge:write)"""
        return self._call(
            OPERATIONS['answer_knowledge_question'],
            {'question_id': question_id},
            body,
            None,
            request_options,
        )

    def compat_list_knowledge_sources(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility knowledge sources (GET /v1/knowledge/sources, scope knowledge:read)"""
        return self._call(
            OPERATIONS['compat_list_knowledge_sources'],
            {},
            None,
            None,
            request_options,
        )

    def compat_list_knowledge_sources_picker(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility knowledge picker (GET /v1/knowledge/sources/picker, scope knowledge:read)"""
        return self._call(
            OPERATIONS['compat_list_knowledge_sources_picker'],
            {},
            None,
            None,
            request_options,
        )

    def test_knowledge_sources(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Test local retrieval against selected or published knowledge (POST /v1/knowledge/test, scope knowledge:write)"""
        return self._call(
            OPERATIONS['test_knowledge_sources'],
            {},
            body,
            None,
            request_options,
        )

    def get_knowledge_testing_context(self, *, agent_id: Any, request_options: dict[str, Any] | None = None) -> Any:
        """List source testing choices and pathway nodes (GET /v1/knowledge/testing-context, scope knowledge:read)"""
        return self._call(
            OPERATIONS['get_knowledge_testing_context'],
            {'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def compat_get_knowledge(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility knowledge item (GET /v1/knowledge/{uuid}, scope knowledge:read)"""
        return self._call(
            OPERATIONS['compat_get_knowledge'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def compat_get_knowledge_content(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility knowledge content (GET /v1/knowledge/{uuid}/content, scope knowledge:read)"""
        return self._call(
            OPERATIONS['compat_get_knowledge_content'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def compat_update_knowledge_content(self, uuid: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Rewrite a plain-text knowledge source in place (keeps the prior version) (PATCH /v1/knowledge/{uuid}/content, scope knowledge:write)"""
        return self._call(
            OPERATIONS['compat_update_knowledge_content'],
            {'uuid': uuid},
            body,
            None,
            request_options,
        )

    def compat_list_knowledge_versions(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility knowledge versions (GET /v1/knowledge/{uuid}/versions, scope knowledge:read)"""
        return self._call(
            OPERATIONS['compat_list_knowledge_versions'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def stream_live_calls(self, *, agent_id: Any, request_options: dict[str, Any] | None = None) -> Any:
        """SSE snapshot of live calls (GET /v1/live-calls/stream, scope calls:read)"""
        return self._call(
            OPERATIONS['stream_live_calls'],
            {'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def stream_live_transcript(self, *, agent_id: Any, room: Any, request_options: dict[str, Any] | None = None) -> Any:
        """SSE snapshot of a live transcript (GET /v1/live-calls/transcript/stream, scope calls:read)"""
        return self._call(
            OPERATIONS['stream_live_transcript'],
            {'agent_id': agent_id, 'room': room},
            None,
            None,
            request_options,
        )

    def mcp_json_rpc(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """MCP JSON-RPC over HTTP (POST /v1/mcp, scope agents:read)"""
        return self._call(
            OPERATIONS['mcp_json_rpc'],
            {},
            body,
            None,
            request_options,
        )

    def get_mcp_client_setup(self, client: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Setup guidance for connecting one coding-agent client (GET /v1/mcp/clients/{client}, scope agents:read)"""
        return self._call(
            OPERATIONS['get_mcp_client_setup'],
            {'client': client},
            None,
            None,
            request_options,
        )

    def list_mcp_connections(self, *, status: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """List connected AI clients (GET /v1/mcp/connections, scope api_keys:read)"""
        return self._call(
            OPERATIONS['list_mcp_connections'],
            {'status': status},
            None,
            None,
            request_options,
        )

    def create_mcp_connection(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Connect an AI client (secret shown once) (POST /v1/mcp/connections, scope api_keys:write)"""
        return self._call(
            OPERATIONS['create_mcp_connection'],
            {},
            body,
            None,
            request_options,
        )

    def revoke_mcp_connection(self, connection_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Disconnect an AI client (DELETE /v1/mcp/connections/{connection_id}, scope api_keys:write)"""
        return self._call(
            OPERATIONS['revoke_mcp_connection'],
            {'connection_id': connection_id},
            None,
            None,
            request_options,
        )

    def get_me(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Describe the calling credential (GET /v1/me)"""
        return self._call(
            OPERATIONS['get_me'],
            {},
            None,
            None,
            request_options,
        )

    def create_memory(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Create a caller fact or summary (POST /v1/memory, scope agents:write)"""
        return self._call(
            OPERATIONS['create_memory'],
            {},
            body,
            None,
            request_options,
        )

    def compat_list_memory_changes(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility memory changes (GET /v1/memory/changes, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_list_memory_changes'],
            {},
            None,
            None,
            request_options,
        )

    def reset_memory(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Forget one caller line for one agent (POST /v1/memory/reset, scope agents:write)"""
        return self._call(
            OPERATIONS['reset_memory'],
            {},
            body,
            None,
            request_options,
        )

    def update_memory(self, memory_id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Correct a caller fact or summary (PATCH /v1/memory/{memory_id}, scope agents:write)"""
        return self._call(
            OPERATIONS['update_memory'],
            {'memory_id': memory_id},
            body,
            None,
            request_options,
        )

    def list_models_v1(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """List Sempera's published TTS models and their capabilities (GET /v1/models, scope models:read)"""
        return self._call(
            OPERATIONS['list_models_v1'],
            {},
            None,
            None,
            request_options,
        )

    def get_service_version(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Read the organization's Sempera service pin (GET /v1/org/service-version, scope workspaces:read)"""
        return self._call(
            OPERATIONS['get_service_version'],
            {},
            None,
            None,
            request_options,
        )

    def update_service_version(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Pin new sessions to an installed Sempera release (PUT /v1/org/service-version, scope workspaces:write)"""
        return self._call(
            OPERATIONS['update_service_version'],
            {},
            body,
            None,
            request_options,
        )

    def list_service_versions(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """List installed Sempera service versions (GET /v1/org/service-versions, scope workspaces:read)"""
        return self._call(
            OPERATIONS['list_service_versions'],
            {},
            None,
            None,
            request_options,
        )

    def list_organizations(self, *, limit: Any = None, cursor: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """List organizations (GET /v1/organizations, scope organizations:read)"""
        return self._call(
            OPERATIONS['list_organizations'],
            {'limit': limit, 'cursor': cursor},
            None,
            None,
            request_options,
        )

    def organizations_create(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Create a reseller-funded child organisation (POST /v1/organizations, scope organizations:write)"""
        return self._call(
            OPERATIONS['organizations_create'],
            {},
            body,
            None,
            request_options,
        )

    def get_organization(self, organization_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Get an organization (GET /v1/organizations/{organization_id}, scope organizations:read)"""
        return self._call(
            OPERATIONS['get_organization'],
            {'organization_id': organization_id},
            None,
            None,
            request_options,
        )

    def compat_list_pathways(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility pathways (GET /v1/pathway, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_list_pathways'],
            {},
            None,
            None,
            request_options,
        )

    def list_personas(self, *, page: Any = None, limit: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """List compiled personas (GET /v1/personas, scope agents:read)"""
        return self._call(
            OPERATIONS['list_personas'],
            {'page': page, 'limit': limit},
            None,
            None,
            request_options,
        )

    def get_persona(self, persona_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Get a compiled persona (GET /v1/personas/{persona_id}, scope agents:read)"""
        return self._call(
            OPERATIONS['get_persona'],
            {'persona_id': persona_id},
            None,
            None,
            request_options,
        )

    def create_phone_message(self, body, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Send an approved text (POST /v1/phone-messages, scope phone:text)"""
        return self._call(
            OPERATIONS['create_phone_message'],
            {},
            body,
            idempotency_key,
            request_options,
        )

    def preview_phone_message(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Preview a text and get its owner approval link (POST /v1/phone-messages/preview, scope phone:text)"""
        return self._call(
            OPERATIONS['preview_phone_message'],
            {},
            body,
            None,
            request_options,
        )

    def list_phone_numbers(self, *, agent_id: Any, limit: Any = None, cursor: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """List phone numbers bound to an agent (GET /v1/phone-numbers, scope phone_numbers:read)"""
        return self._call(
            OPERATIONS['list_phone_numbers'],
            {'agent_id': agent_id, 'limit': limit, 'cursor': cursor},
            None,
            None,
            request_options,
        )

    def bind_phone_number(self, body, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Bind a phone number to an agent (POST /v1/phone-numbers, scope phone_numbers:write)"""
        return self._call(
            OPERATIONS['bind_phone_number'],
            {},
            body,
            idempotency_key,
            request_options,
        )

    def poll_phone_onboarding(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Poll a phone signup (POST /v1/phone-onboarding/poll)"""
        return self._call(
            OPERATIONS['poll_phone_onboarding'],
            {},
            None,
            None,
            request_options,
        )

    def start_phone_onboarding(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Start an owner-approved phone signup (POST /v1/phone-onboarding/start)"""
        return self._call(
            OPERATIONS['start_phone_onboarding'],
            {},
            None,
            None,
            request_options,
        )

    def get_phone_profile(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Read the phone line, plan and allowance (GET /v1/phone-profile, scope phone:read)"""
        return self._call(
            OPERATIONS['get_phone_profile'],
            {},
            None,
            None,
            request_options,
        )

    def create_phone_task(self, body, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Start an approved call (POST /v1/phone-tasks, scope phone:call)"""
        return self._call(
            OPERATIONS['create_phone_task'],
            {},
            body,
            idempotency_key,
            request_options,
        )

    def preview_phone_task(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Preview a call and get its owner approval link (POST /v1/phone-tasks/preview, scope phone:call)"""
        return self._call(
            OPERATIONS['preview_phone_task'],
            {},
            body,
            None,
            request_options,
        )

    def get_phone_task(self, task_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Read a phone task and its result (GET /v1/phone-tasks/{task_id}, scope phone:read)"""
        return self._call(
            OPERATIONS['get_phone_task'],
            {'task_id': task_id},
            None,
            None,
            request_options,
        )

    def cancel_phone_task(self, task_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Cancel a phone task (POST /v1/phone-tasks/{task_id}/cancel, scope phone:call)"""
        return self._call(
            OPERATIONS['cancel_phone_task'],
            {'task_id': task_id},
            None,
            None,
            request_options,
        )

    def get_phone_thread(self, thread_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Read a text thread on the plan's number (GET /v1/phone-threads/{thread_id}, scope phone:text)"""
        return self._call(
            OPERATIONS['get_phone_thread'],
            {'thread_id': thread_id},
            None,
            None,
            request_options,
        )

    def get_platform(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Deployment identity and capacity (CI/certification) (GET /v1/platform, scope deploy:read)"""
        return self._call(
            OPERATIONS['get_platform'],
            {},
            None,
            None,
            request_options,
        )

    def list_prompts(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """List this workspace's saved prompts (GET /v1/prompts, scope prompts:read)"""
        return self._call(
            OPERATIONS['list_prompts'],
            {},
            None,
            None,
            request_options,
        )

    def create_prompt(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Save a prompt for future use (POST /v1/prompts, scope prompts:write)"""
        return self._call(
            OPERATIONS['create_prompt'],
            {},
            body,
            None,
            request_options,
        )

    def get_prompt(self, prompt_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Get a saved prompt (GET /v1/prompts/{prompt_id}, scope prompts:read)"""
        return self._call(
            OPERATIONS['get_prompt'],
            {'prompt_id': prompt_id},
            None,
            None,
            request_options,
        )

    def get_recording(self, recording_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Signed download URL for a call recording (GET /v1/recordings/{recording_id}, scope calls:read)"""
        return self._call(
            OPERATIONS['get_recording'],
            {'recording_id': recording_id},
            None,
            None,
            request_options,
        )

    def list_release_deployments(self, *, limit: Any = None, cursor: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """Every agent version put on an environment in this workspace (GET /v1/release-deployments, scope deploy:read)"""
        return self._call(
            OPERATIONS['list_release_deployments'],
            {'limit': limit, 'cursor': cursor},
            None,
            None,
            request_options,
        )

    def compat_list_releases(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility releases placeholder (GET /v1/releases, scope deploy:read)"""
        return self._call(
            OPERATIONS['compat_list_releases'],
            {},
            None,
            None,
            request_options,
        )

    def compat_get_current_deployment(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility current deployment placeholder (GET /v1/releases/deployments/current, scope deploy:read)"""
        return self._call(
            OPERATIONS['compat_get_current_deployment'],
            {},
            None,
            None,
            request_options,
        )

    def compat_list_deployment_history(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility deployment history placeholder (GET /v1/releases/deployments/history, scope deploy:read)"""
        return self._call(
            OPERATIONS['compat_list_deployment_history'],
            {},
            None,
            None,
            request_options,
        )

    def compat_list_resources(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility resources (GET /v1/resources, scope tools:read)"""
        return self._call(
            OPERATIONS['compat_list_resources'],
            {},
            None,
            None,
            request_options,
        )

    def compat_list_secrets(self, *, q: Any = None, type: Any = None, status: Any = None, sort: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility secret references (GET /v1/secrets, scope tools:read)"""
        return self._call(
            OPERATIONS['compat_list_secrets'],
            {'q': q, 'type': type, 'status': status, 'sort': sort},
            None,
            None,
            request_options,
        )

    def create_secret(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Add a workspace secret (the value is never returned) (POST /v1/secrets, scope tools:write)"""
        return self._call(
            OPERATIONS['create_secret'],
            {},
            body,
            None,
            request_options,
        )

    def update_secret(self, id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Rename a workspace secret, replace a Static value, or pause and resume it (PATCH /v1/secrets/{id}, scope tools:write)"""
        return self._call(
            OPERATIONS['update_secret'],
            {'id': id},
            body,
            None,
            request_options,
        )

    def delete_secret(self, id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Delete a workspace secret (DELETE /v1/secrets/{id}, scope tools:write)"""
        return self._call(
            OPERATIONS['delete_secret'],
            {'id': id},
            None,
            None,
            request_options,
        )

    def refresh_secret(self, id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Fetch a Refresh secret's value now (the value is never returned) (POST /v1/secrets/{id}/refresh, scope tools:write)"""
        return self._call(
            OPERATIONS['refresh_secret'],
            {'id': id},
            None,
            None,
            request_options,
        )

    def list_sessions(self, *, agent_id: Any, channel: Any = None, limit: Any = None, cursor: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """List sessions for an agent (GET /v1/sessions, scope sessions:read)"""
        return self._call(
            OPERATIONS['list_sessions'],
            {'agent_id': agent_id, 'channel': channel, 'limit': limit, 'cursor': cursor},
            None,
            None,
            request_options,
        )

    def create_session(self, body, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Create a Web voice or simulator session (POST /v1/sessions, scope sessions:write)"""
        return self._call(
            OPERATIONS['create_session'],
            {},
            body,
            idempotency_key,
            request_options,
        )

    def get_session(self, session_id: str, *, agent_id: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """Get a session (GET /v1/sessions/{session_id}, scope sessions:read)"""
        return self._call(
            OPERATIONS['get_session'],
            {'session_id': session_id, 'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def get_request_signing(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """JWT request signing settings and keys (GET /v1/signing, scope webhooks:read)"""
        return self._call(
            OPERATIONS['get_request_signing'],
            {},
            None,
            None,
            request_options,
        )

    def patch_request_signing(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Update JWT request signing (PATCH /v1/signing, scope webhooks:write)"""
        return self._call(
            OPERATIONS['patch_request_signing'],
            {},
            body,
            None,
            request_options,
        )

    def generate_signing_key(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Generate or rotate the signing key (POST /v1/signing/keys, scope webhooks:write)"""
        return self._call(
            OPERATIONS['generate_signing_key'],
            {},
            None,
            None,
            request_options,
        )

    def revoke_previous_signing_keys(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Withdraw every signing key but the active one (POST /v1/signing/keys/revoke-previous, scope webhooks:write)"""
        return self._call(
            OPERATIONS['revoke_previous_signing_keys'],
            {},
            None,
            None,
            request_options,
        )

    def batch_sms(self, body, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Send a bounded SMS batch (POST /v1/sms/batch, scope calls:write)"""
        return self._call(
            OPERATIONS['batch_sms'],
            {},
            body,
            idempotency_key,
            request_options,
        )

    def compat_list_sms_conversations(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility SMS conversations (GET /v1/sms/conversations, scope calls:read)"""
        return self._call(
            OPERATIONS['compat_list_sms_conversations'],
            {},
            None,
            None,
            request_options,
        )

    def get_sms_conversation(self, conversation_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Get SMS conversation (GET /v1/sms/conversations/{conversation_id}, scope calls:read)"""
        return self._call(
            OPERATIONS['get_sms_conversation'],
            {'conversation_id': conversation_id},
            None,
            None,
            request_options,
        )

    def end_sms_conversation(self, conversation_id: str, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """end SMS conversation (POST /v1/sms/conversations/{conversation_id}/end, scope calls:write)"""
        return self._call(
            OPERATIONS['end_sms_conversation'],
            {'conversation_id': conversation_id},
            None,
            idempotency_key,
            request_options,
        )

    def handoff_sms_conversation(self, conversation_id: str, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """handoff SMS conversation (POST /v1/sms/conversations/{conversation_id}/handoff, scope calls:write)"""
        return self._call(
            OPERATIONS['handoff_sms_conversation'],
            {'conversation_id': conversation_id},
            None,
            idempotency_key,
            request_options,
        )

    def list_sms_messages(self, conversation_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """List SMS messages (GET /v1/sms/conversations/{conversation_id}/messages, scope calls:read)"""
        return self._call(
            OPERATIONS['list_sms_messages'],
            {'conversation_id': conversation_id},
            None,
            None,
            request_options,
        )

    def reply_sms(self, conversation_id: str, body, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Send conversation message (POST /v1/sms/conversations/{conversation_id}/messages, scope calls:write)"""
        return self._call(
            OPERATIONS['reply_sms'],
            {'conversation_id': conversation_id},
            body,
            idempotency_key,
            request_options,
        )

    def opt_out_sms_conversation(self, conversation_id: str, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Record an SMS opt-out without sending (POST /v1/sms/conversations/{conversation_id}/opt-out, scope calls:write)"""
        return self._call(
            OPERATIONS['opt_out_sms_conversation'],
            {'conversation_id': conversation_id},
            None,
            idempotency_key,
            request_options,
        )

    def get_sms_policy(self, conversation_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Read SMS consent and sending policy (GET /v1/sms/conversations/{conversation_id}/policy, scope calls:read)"""
        return self._call(
            OPERATIONS['get_sms_policy'],
            {'conversation_id': conversation_id},
            None,
            None,
            request_options,
        )

    def resume_sms_conversation(self, conversation_id: str, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """resume SMS conversation (POST /v1/sms/conversations/{conversation_id}/resume, scope calls:write)"""
        return self._call(
            OPERATIONS['resume_sms_conversation'],
            {'conversation_id': conversation_id},
            None,
            idempotency_key,
            request_options,
        )

    def compat_list_sms_numbers(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility SMS numbers (GET /v1/sms/numbers, scope phone_numbers:read)"""
        return self._call(
            OPERATIONS['compat_list_sms_numbers'],
            {},
            None,
            None,
            request_options,
        )

    def send_sms(self, body, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Send SMS (POST /v1/sms/send, scope calls:write)"""
        return self._call(
            OPERATIONS['send_sms'],
            {},
            body,
            idempotency_key,
            request_options,
        )

    def list_snippets(self, *, status: Any = None, limit: Any = None, cursor: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """List code snippets (GET /v1/snippets, scope tools:read)"""
        return self._call(
            OPERATIONS['list_snippets'],
            {'status': status, 'limit': limit, 'cursor': cursor},
            None,
            None,
            request_options,
        )

    def create_snippet(self, body, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Create a code snippet (its first draft) (POST /v1/snippets, scope tools:write)"""
        return self._call(
            OPERATIONS['create_snippet'],
            {},
            body,
            idempotency_key,
            request_options,
        )

    def get_snippet(self, snippet_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Get a code snippet and its versions (GET /v1/snippets/{snippet_id}, scope tools:read)"""
        return self._call(
            OPERATIONS['get_snippet'],
            {'snippet_id': snippet_id},
            None,
            None,
            request_options,
        )

    def update_snippet(self, snippet_id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Edit the draft (opens a new draft after the highest version when none is open) (PATCH /v1/snippets/{snippet_id}, scope tools:write)"""
        return self._call(
            OPERATIONS['update_snippet'],
            {'snippet_id': snippet_id},
            body,
            None,
            request_options,
        )

    def delete_snippet(self, snippet_id: str, *, restore: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """Archive (or restore) a code snippet (DELETE /v1/snippets/{snippet_id}, scope tools:write)"""
        return self._call(
            OPERATIONS['delete_snippet'],
            {'snippet_id': snippet_id, 'restore': restore},
            None,
            None,
            request_options,
        )

    def publish_snippet(self, snippet_id: str, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Publish the draft as an immutable version (POST /v1/snippets/{snippet_id}/publish, scope tools:write)"""
        return self._call(
            OPERATIONS['publish_snippet'],
            {'snippet_id': snippet_id},
            None,
            idempotency_key,
            request_options,
        )

    def test_snippet(self, snippet_id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Run a version (or the draft) on sample input in the sandbox (POST /v1/snippets/{snippet_id}/test, scope tools:write)"""
        return self._call(
            OPERATIONS['test_snippet'],
            {'snippet_id': snippet_id},
            body,
            None,
            request_options,
        )

    def get_snippet_version(self, snippet_id: str, version: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Get one version of a code snippet (GET /v1/snippets/{snippet_id}/versions/{version}, scope tools:read)"""
        return self._call(
            OPERATIONS['get_snippet_version'],
            {'snippet_id': snippet_id, 'version': version},
            None,
            None,
            request_options,
        )

    def list_standards(self, *, agent_id: Any, request_options: dict[str, Any] | None = None) -> Any:
        """List an agent's standards with their latest result (GET /v1/standards, scope tests:read)"""
        return self._call(
            OPERATIONS['list_standards'],
            {'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def create_standard(self, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Save a node-level standard (a step, a fixed situation, what the step must do) (POST /v1/standards, scope tests:write)"""
        return self._call(
            OPERATIONS['create_standard'],
            {},
            None,
            idempotency_key,
            request_options,
        )

    def run_standards(self, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Run standards against the agent's current version (background job) (POST /v1/standards/run, scope tests:write)"""
        return self._call(
            OPERATIONS['run_standards'],
            {},
            None,
            idempotency_key,
            request_options,
        )

    def list_standards_runs(self, *, agent_id: Any, request_options: dict[str, Any] | None = None) -> Any:
        """Standards runs, newest first (GET /v1/standards/runs, scope tests:read)"""
        return self._call(
            OPERATIONS['list_standards_runs'],
            {'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def update_standard(self, standard_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Change a standard (PATCH /v1/standards/{standard_id}, scope tests:write)"""
        return self._call(
            OPERATIONS['update_standard'],
            {'standard_id': standard_id},
            None,
            None,
            request_options,
        )

    def delete_standard(self, standard_id: str, *, agent_id: Any, request_options: dict[str, Any] | None = None) -> Any:
        """Delete a standard (DELETE /v1/standards/{standard_id}, scope tests:write)"""
        return self._call(
            OPERATIONS['delete_standard'],
            {'standard_id': standard_id, 'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def compat_subaccounts_retired(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Subaccounts (retired, answers as the reference does) (GET /v1/subaccounts, scope organizations:read)"""
        return self._call(
            OPERATIONS['compat_subaccounts_retired'],
            {},
            None,
            None,
            request_options,
        )

    def get_test_analytics(self, *, agent_id: Any, days: Any = None, min_samples: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """Failures per graph node over a window, and the weakest link (GET /v1/test-analytics, scope tests:read)"""
        return self._call(
            OPERATIONS['get_test_analytics'],
            {'agent_id': agent_id, 'days': days, 'min_samples': min_samples},
            None,
            None,
            request_options,
        )

    def run_testbed(self, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Run a turn's situation against the step's current and a candidate instruction (nothing is saved) (POST /v1/testbed/runs, scope tests:write)"""
        return self._call(
            OPERATIONS['run_testbed'],
            {},
            None,
            idempotency_key,
            request_options,
        )

    def get_testbed_run(self, run_id: str, *, agent_id: Any, request_options: dict[str, Any] | None = None) -> Any:
        """A Testbed run and its per-situation comparison (GET /v1/testbed/runs/{run_id}, scope tests:read)"""
        return self._call(
            OPERATIONS['get_testbed_run'],
            {'run_id': run_id, 'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def get_testbed_situation(self, *, agent_id: Any, conversation_id: Any, turn: Any, step: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """The situation at one turn of a stored conversation: the step, its instruction, the original reply (GET /v1/testbed/situation, scope tests:read)"""
        return self._call(
            OPERATIONS['get_testbed_situation'],
            {'agent_id': agent_id, 'conversation_id': conversation_id, 'turn': turn, 'step': step},
            None,
            None,
            request_options,
        )

    def save_testbed_standard(self, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Save a Testbed situation and expectations as a standard (POST /v1/testbed/standards, scope tests:write)"""
        return self._call(
            OPERATIONS['save_testbed_standard'],
            {},
            None,
            idempotency_key,
            request_options,
        )

    def list_tests(self, *, agent_id: Any, limit: Any = None, cursor: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """List test runs for an agent (GET /v1/tests, scope tests:read)"""
        return self._call(
            OPERATIONS['list_tests'],
            {'agent_id': agent_id, 'limit': limit, 'cursor': cursor},
            None,
            None,
            request_options,
        )

    def run_tests(self, body, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Run the test battery (background job) (POST /v1/tests, scope tests:write)"""
        return self._call(
            OPERATIONS['run_tests'],
            {},
            body,
            idempotency_key,
            request_options,
        )

    def get_test(self, test_id: str, *, agent_id: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """Get a test run (GET /v1/tests/{test_id}, scope tests:read)"""
        return self._call(
            OPERATIONS['get_test'],
            {'test_id': test_id, 'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def start_text_assistant_link(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Send a mobile linking code (POST /v1/text-assistant/link, scope workspaces:write)"""
        return self._call(
            OPERATIONS['start_text_assistant_link'],
            {},
            body,
            None,
            request_options,
        )

    def unlink_text_assistant(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Unlink your mobile number (DELETE /v1/text-assistant/link, scope workspaces:write)"""
        return self._call(
            OPERATIONS['unlink_text_assistant'],
            {},
            None,
            None,
            request_options,
        )

    def confirm_text_assistant_link(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Confirm your mobile linking code (POST /v1/text-assistant/link/confirm, scope workspaces:write)"""
        return self._call(
            OPERATIONS['confirm_text_assistant_link'],
            {},
            body,
            None,
            request_options,
        )

    def get_text_assistant_settings(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Read text Assistant settings (GET /v1/text-assistant/settings, scope workspaces:read)"""
        return self._call(
            OPERATIONS['get_text_assistant_settings'],
            {},
            None,
            None,
            request_options,
        )

    def update_text_assistant_settings(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Enable or disable the text Assistant (PATCH /v1/text-assistant/settings, scope workspaces:write)"""
        return self._call(
            OPERATIONS['update_text_assistant_settings'],
            {},
            body,
            None,
            request_options,
        )

    def get_text_assistant_thread(self, *, before: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """Read your text Assistant thread (GET /v1/text-assistant/thread, scope workspaces:read)"""
        return self._call(
            OPERATIONS['get_text_assistant_thread'],
            {'before': before},
            None,
            None,
            request_options,
        )

    def list_tools(self, *, status: Any = None, limit: Any = None, cursor: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """List tools (GET /v1/tools, scope tools:read)"""
        return self._call(
            OPERATIONS['list_tools'],
            {'status': status, 'limit': limit, 'cursor': cursor},
            None,
            None,
            request_options,
        )

    def create_tool(self, body, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Create a tool (POST /v1/tools, scope tools:write)"""
        return self._call(
            OPERATIONS['create_tool'],
            {},
            body,
            idempotency_key,
            request_options,
        )

    def get_tool(self, tool_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Get a tool (GET /v1/tools/{tool_id}, scope tools:read)"""
        return self._call(
            OPERATIONS['get_tool'],
            {'tool_id': tool_id},
            None,
            None,
            request_options,
        )

    def update_tool(self, tool_id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Update a tool (PATCH /v1/tools/{tool_id}, scope tools:write)"""
        return self._call(
            OPERATIONS['update_tool'],
            {'tool_id': tool_id},
            body,
            None,
            request_options,
        )

    def delete_tool(self, tool_id: str, *, restore: Any = None, revision: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """Disable (archive) a tool (DELETE /v1/tools/{tool_id}, scope tools:write)"""
        return self._call(
            OPERATIONS['delete_tool'],
            {'tool_id': tool_id, 'restore': restore, 'revision': revision},
            None,
            None,
            request_options,
        )

    def execute_tool(self, tool_id: str, body, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Execute a tool in test mode (POST /v1/tools/{tool_id}/execute, scope tools:execute)"""
        return self._call(
            OPERATIONS['execute_tool'],
            {'tool_id': tool_id},
            body,
            idempotency_key,
            request_options,
        )

    def list_tool_executions(self, tool_id: str, *, limit: Any = None, cursor: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """Recent executions of a tool (GET /v1/tools/{tool_id}/executions, scope tools:read)"""
        return self._call(
            OPERATIONS['list_tool_executions'],
            {'tool_id': tool_id, 'limit': limit, 'cursor': cursor},
            None,
            None,
            request_options,
        )

    def compat_list_transcript_reports(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility transcript reports (GET /v1/transcript-reports/call/{uuid}, scope calls:read)"""
        return self._call(
            OPERATIONS['compat_list_transcript_reports'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def get_translation_sessions(self, *, agent_id: Any, request_options: dict[str, Any] | None = None) -> Any:
        """Read live translation availability and recent sessions (GET /v1/translation-sessions, scope sessions:read)"""
        return self._call(
            OPERATIONS['get_translation_sessions'],
            {'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def create_translation_session(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Start a Sempera live translation session (POST /v1/translation-sessions, scope sessions:write)"""
        return self._call(
            OPERATIONS['create_translation_session'],
            {},
            body,
            None,
            request_options,
        )

    def compat_list_triage_categories(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility triage categories (GET /v1/triage/categories, scope evals:read)"""
        return self._call(
            OPERATIONS['compat_list_triage_categories'],
            {},
            None,
            None,
            request_options,
        )

    def compat_list_triage_flag_types(self, *, limit: Any = None, cursor: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility triage flag types (GET /v1/triage/flag-types, scope evals:read)"""
        return self._call(
            OPERATIONS['compat_list_triage_flag_types'],
            {'limit': limit, 'cursor': cursor},
            None,
            None,
            request_options,
        )

    def compat_list_triage_issues(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility triage issues (GET /v1/triage/issues, scope evals:read)"""
        return self._call(
            OPERATIONS['compat_list_triage_issues'],
            {},
            None,
            None,
            request_options,
        )

    def compat_create_triage_issue(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Create triage issue (POST /v1/triage/issues, scope evals:write)"""
        return self._call(
            OPERATIONS['compat_create_triage_issue'],
            {},
            None,
            None,
            request_options,
        )

    def compat_get_triage_issue(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility triage issue (GET /v1/triage/issues/{uuid}, scope evals:read)"""
        return self._call(
            OPERATIONS['compat_get_triage_issue'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def compat_update_triage_issue(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Update triage issue (PATCH /v1/triage/issues/{uuid}, scope evals:write)"""
        return self._call(
            OPERATIONS['compat_update_triage_issue'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def compat_list_triage_issue_activity(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility triage activity (GET /v1/triage/issues/{uuid}/activity, scope evals:read)"""
        return self._call(
            OPERATIONS['compat_list_triage_issue_activity'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def compat_list_triage_issue_affected(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility triage affected surfaces (GET /v1/triage/issues/{uuid}/affected, scope evals:read)"""
        return self._call(
            OPERATIONS['compat_list_triage_issue_affected'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def compat_link_triage_issue_call(self, uuid: str, call_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Link a call to a triage issue (PUT /v1/triage/issues/{uuid}/calls/{call_id}, scope evals:write)"""
        return self._call(
            OPERATIONS['compat_link_triage_issue_call'],
            {'uuid': uuid, 'call_id': call_id},
            None,
            None,
            request_options,
        )

    def compat_create_triage_issue_comment(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Create triage comment (POST /v1/triage/issues/{uuid}/comments, scope evals:write)"""
        return self._call(
            OPERATIONS['compat_create_triage_issue_comment'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def compat_list_triage_issue_flags(self, uuid: str, *, limit: Any = None, cursor: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """Calls flagged onto a triage issue (GET /v1/triage/issues/{uuid}/flags, scope evals:read)"""
        return self._call(
            OPERATIONS['compat_list_triage_issue_flags'],
            {'uuid': uuid, 'limit': limit, 'cursor': cursor},
            None,
            None,
            request_options,
        )

    def compat_create_triage_issue_flag(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Flag a call onto a triage issue (POST /v1/triage/issues/{uuid}/flags, scope evals:write)"""
        return self._call(
            OPERATIONS['compat_create_triage_issue_flag'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def compat_list_triage_issue_relations(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """List the links to and from a triage issue (GET /v1/triage/issues/{uuid}/relations, scope evals:read)"""
        return self._call(
            OPERATIONS['compat_list_triage_issue_relations'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def compat_create_triage_issue_relation(self, uuid: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Link a triage issue to another one (POST /v1/triage/issues/{uuid}/relations, scope evals:write)"""
        return self._call(
            OPERATIONS['compat_create_triage_issue_relation'],
            {'uuid': uuid},
            body,
            None,
            request_options,
        )

    def compat_delete_triage_issue_relation(self, uuid: str, relation_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Remove a link between two triage issues (DELETE /v1/triage/issues/{uuid}/relations/{relation_id}, scope evals:write)"""
        return self._call(
            OPERATIONS['compat_delete_triage_issue_relation'],
            {'uuid': uuid, 'relation_id': relation_id},
            None,
            None,
            request_options,
        )

    def compat_list_triage_issue_resources(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility triage resources (GET /v1/triage/issues/{uuid}/resources, scope evals:read)"""
        return self._call(
            OPERATIONS['compat_list_triage_issue_resources'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def compat_attach_triage_file_resource(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Attach triage file resource (POST /v1/triage/issues/{uuid}/resources, scope evals:write)"""
        return self._call(
            OPERATIONS['compat_attach_triage_file_resource'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def compat_mark_triage_issue_viewed(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility triage viewed marker (PUT /v1/triage/issues/{uuid}/view, scope evals:write)"""
        return self._call(
            OPERATIONS['compat_mark_triage_issue_viewed'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def list_voices(self, *, engine: Any = None, language: Any = None, search: Any = None, limit: Any = None, cursor: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """List the voices a session or draft may name (GET /v1/voices, scope agents:read)"""
        return self._call(
            OPERATIONS['list_voices'],
            {'engine': engine, 'language': language, 'search': search, 'limit': limit, 'cursor': cursor},
            None,
            None,
            request_options,
        )

    def list_voice_library(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """List workspace voice collection (GET /v1/voices/library, scope agents:read)"""
        return self._call(
            OPERATIONS['list_voice_library'],
            {},
            None,
            None,
            request_options,
        )

    def add_voice_library(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Add a cleared voice to the workspace library (POST /v1/voices/library/add, scope agents:write)"""
        return self._call(
            OPERATIONS['add_voice_library'],
            {},
            body,
            None,
            request_options,
        )

    def get_shared_voice(self, entry_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Read a voice shared with this workspace (GET /v1/voices/library/{entry_id}, scope agents:read)"""
        return self._call(
            OPERATIONS['get_shared_voice'],
            {'entry_id': entry_id},
            None,
            None,
            request_options,
        )

    def rate_voice(self, entry_id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Set the workspace rating for a saved voice (POST /v1/voices/library/{entry_id}/rate, scope agents:write)"""
        return self._call(
            OPERATIONS['rate_voice'],
            {'entry_id': entry_id},
            body,
            None,
            request_options,
        )

    def sample_voice(self, entry_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Play a saved voice with the workspace sample text (GET /v1/voices/library/{entry_id}/sample, scope agents:write)"""
        return self._call(
            OPERATIONS['sample_voice'],
            {'entry_id': entry_id},
            None,
            None,
            request_options,
        )

    def share_voice(self, entry_id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Enable or revoke authenticated team sharing (POST /v1/voices/library/{entry_id}/share, scope agents:write)"""
        return self._call(
            OPERATIONS['share_voice'],
            {'entry_id': entry_id},
            body,
            None,
            request_options,
        )

    def list_studio_clones(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """List professional clone preparations (GET /v1/voices/studio, scope agents:read)"""
        return self._call(
            OPERATIONS['list_studio_clones'],
            {},
            None,
            None,
            request_options,
        )

    def prepare_studio_clone(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Prepare a professional clone without uploading or training (POST /v1/voices/studio, scope agents:write)"""
        return self._call(
            OPERATIONS['prepare_studio_clone'],
            {},
            body,
            None,
            request_options,
        )

    def list_webhooks(self, *, limit: Any = None, cursor: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """List webhook endpoints (GET /v1/webhooks, scope webhooks:read)"""
        return self._call(
            OPERATIONS['list_webhooks'],
            {'limit': limit, 'cursor': cursor},
            None,
            None,
            request_options,
        )

    def create_webhook(self, body, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Create a webhook endpoint (POST /v1/webhooks, scope webhooks:write)"""
        return self._call(
            OPERATIONS['create_webhook'],
            {},
            body,
            idempotency_key,
            request_options,
        )

    def get_webhook(self, webhook_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Get a webhook endpoint (GET /v1/webhooks/{webhook_id}, scope webhooks:read)"""
        return self._call(
            OPERATIONS['get_webhook'],
            {'webhook_id': webhook_id},
            None,
            None,
            request_options,
        )

    def patch_webhook(self, webhook_id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Update a webhook endpoint (PATCH /v1/webhooks/{webhook_id}, scope webhooks:write)"""
        return self._call(
            OPERATIONS['patch_webhook'],
            {'webhook_id': webhook_id},
            body,
            None,
            request_options,
        )

    def delete_webhook(self, webhook_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Delete a webhook endpoint (DELETE /v1/webhooks/{webhook_id}, scope webhooks:write)"""
        return self._call(
            OPERATIONS['delete_webhook'],
            {'webhook_id': webhook_id},
            None,
            None,
            request_options,
        )

    def list_webhook_deliveries(self, webhook_id: str, *, limit: Any = None, cursor: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """Delivery attempts (GET /v1/webhooks/{webhook_id}/deliveries, scope webhooks:read)"""
        return self._call(
            OPERATIONS['list_webhook_deliveries'],
            {'webhook_id': webhook_id, 'limit': limit, 'cursor': cursor},
            None,
            None,
            request_options,
        )

    def resend_webhook_delivery(self, webhook_id: str, delivery_id: str, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Resend a recorded webhook delivery (POST /v1/webhooks/{webhook_id}/deliveries/{delivery_id}/resend, scope webhooks:write)"""
        return self._call(
            OPERATIONS['resend_webhook_delivery'],
            {'webhook_id': webhook_id, 'delivery_id': delivery_id},
            None,
            idempotency_key,
            request_options,
        )

    def test_webhook(self, webhook_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Send a signed test event (POST /v1/webhooks/{webhook_id}/test, scope webhooks:write)"""
        return self._call(
            OPERATIONS['test_webhook'],
            {'webhook_id': webhook_id},
            None,
            None,
            request_options,
        )

    def list_widget_live_chats(self, *, agent_id: Any, request_options: dict[str, Any] | None = None) -> Any:
        """Read this agent's waiting and operator-held widget chats (GET /v1/widget-live-chats, scope sessions:write)"""
        return self._call(
            OPERATIONS['list_widget_live_chats'],
            {'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def act_on_widget_live_chat(self, chat_id: str, body, *, agent_id: Any, request_options: dict[str, Any] | None = None) -> Any:
        """Claim, take over or reply to a widget chat, or return it to the agent (POST /v1/widget-live-chats/{chat_id}, scope sessions:write)"""
        return self._call(
            OPERATIONS['act_on_widget_live_chat'],
            {'chat_id': chat_id, 'agent_id': agent_id},
            body,
            None,
            request_options,
        )

    def list_widget_custom_components(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Widget custom components on this workspace's agents (GET /v1/widget/custom-components, scope sessions:read)"""
        return self._call(
            OPERATIONS['list_widget_custom_components'],
            {},
            None,
            None,
            request_options,
        )

    def create_widget_custom_component(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Attach a custom component to a node of a widget's agent (POST /v1/widget/custom-components, scope agents:write)"""
        return self._call(
            OPERATIONS['create_widget_custom_component'],
            {},
            body,
            None,
            request_options,
        )

    def update_widget_custom_component(self, id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Update a widget custom component (PATCH /v1/widget/custom-components/{id}, scope agents:write)"""
        return self._call(
            OPERATIONS['update_widget_custom_component'],
            {'id': id},
            body,
            None,
            request_options,
        )

    def delete_widget_custom_component(self, id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Remove a widget custom component (DELETE /v1/widget/custom-components/{id}, scope agents:write)"""
        return self._call(
            OPERATIONS['delete_widget_custom_component'],
            {'id': id},
            None,
            None,
            request_options,
        )

    def compat_list_widget_threads(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility widget threads (GET /v1/widget/threads, scope sessions:read)"""
        return self._call(
            OPERATIONS['compat_list_widget_threads'],
            {},
            None,
            None,
            request_options,
        )

    def compat_list_widgets(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility widgets (GET /v1/widgets, scope sessions:read)"""
        return self._call(
            OPERATIONS['compat_list_widgets'],
            {},
            None,
            None,
            request_options,
        )

    def list_workspaces(self, *, limit: Any = None, cursor: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """List workspaces (GET /v1/workspaces, scope workspaces:read)"""
        return self._call(
            OPERATIONS['list_workspaces'],
            {'limit': limit, 'cursor': cursor},
            None,
            None,
            request_options,
        )

    def get_workspace(self, workspace_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Get a workspace (GET /v1/workspaces/{workspace_id}, scope workspaces:read)"""
        return self._call(
            OPERATIONS['get_workspace'],
            {'workspace_id': workspace_id},
            None,
            None,
            request_options,
        )

    def patch_workspace(self, workspace_id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Rename a workspace (PATCH /v1/workspaces/{workspace_id}, scope workspaces:write)"""
        return self._call(
            OPERATIONS['patch_workspace'],
            {'workspace_id': workspace_id},
            body,
            None,
            request_options,
        )

    def get_workspace_jwks(self, workspace_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """A workspace's public signing keys (JWKS) (GET /v1/workspaces/{workspace_id}/.well-known/jwks.json)"""
        return self._call(
            OPERATIONS['get_workspace_jwks'],
            {'workspace_id': workspace_id},
            None,
            None,
            request_options,
        )

    def compat_v2_list_agents(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility v2 agents (GET /v2/agents, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_v2_list_agents'],
            {},
            None,
            None,
            request_options,
        )

    def compat_v2_get_starter(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """The workspace's starter agent (GET /v2/agents/starter, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_v2_get_starter'],
            {},
            None,
            None,
            request_options,
        )

    def compat_v2_create_starter(self, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Create the workspace's starter agent once (POST /v2/agents/starter, scope agents:write)"""
        return self._call(
            OPERATIONS['compat_v2_create_starter'],
            {},
            body,
            None,
            request_options,
        )

    def compat_v2_list_starter_templates(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Job templates a new agent can start from (GET /v2/agents/starter-templates, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_v2_list_starter_templates'],
            {},
            None,
            None,
            request_options,
        )

    def compat_v2_get_agent(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility v2 agent (GET /v2/agents/{uuid}, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_v2_get_agent'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def compat_v2_list_branches(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """List v2 agent branches (GET /v2/agents/{uuid}/branches, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_v2_list_branches'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def compat_v2_create_branch(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Create v2 agent branch (POST /v2/agents/{uuid}/branches, scope agents:write)"""
        return self._call(
            OPERATIONS['compat_v2_create_branch'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def compat_v2_delete_branch(self, uuid: str, branch_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Delete v2 agent branch (DELETE /v2/agents/{uuid}/branches/{branch_id}, scope agents:write)"""
        return self._call(
            OPERATIONS['compat_v2_delete_branch'],
            {'uuid': uuid, 'branch_id': branch_id},
            None,
            None,
            request_options,
        )

    def compat_v2_merge_branch(self, uuid: str, branch_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Merge v2 agent branch (POST /v2/agents/{uuid}/branches/{branch_id}/merge, scope agents:write)"""
        return self._call(
            OPERATIONS['compat_v2_merge_branch'],
            {'uuid': uuid, 'branch_id': branch_id},
            None,
            None,
            request_options,
        )

    def compat_v2_rebase_branch(self, uuid: str, branch_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Rebase v2 agent branch (POST /v2/agents/{uuid}/branches/{branch_id}/rebase, scope agents:write)"""
        return self._call(
            OPERATIONS['compat_v2_rebase_branch'],
            {'uuid': uuid, 'branch_id': branch_id},
            None,
            None,
            request_options,
        )

    def compat_v2_preview_branch_rebase(self, uuid: str, branch_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Preview v2 agent branch rebase (POST /v2/agents/{uuid}/branches/{branch_id}/rebase-preview, scope agents:write)"""
        return self._call(
            OPERATIONS['compat_v2_preview_branch_rebase'],
            {'uuid': uuid, 'branch_id': branch_id},
            None,
            None,
            request_options,
        )

    def compat_v2_list_check_runs(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility v2 check runs (GET /v2/agents/{uuid}/check-runs, scope evals:read)"""
        return self._call(
            OPERATIONS['compat_v2_list_check_runs'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def compat_v2_list_deployments(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility v2 deployments (GET /v2/agents/{uuid}/deployments, scope deploy:read)"""
        return self._call(
            OPERATIONS['compat_v2_list_deployments'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def compat_v2_list_dispositions(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """List v2 agent dispositions (GET /v2/agents/{uuid}/dispositions, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_v2_list_dispositions'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def compat_v2_create_disposition(self, uuid: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Create v2 agent disposition (POST /v2/agents/{uuid}/dispositions, scope agents:write)"""
        return self._call(
            OPERATIONS['compat_v2_create_disposition'],
            {'uuid': uuid},
            body,
            None,
            request_options,
        )

    def compat_v2_get_disposition_extractor_catalog(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """List v2 published disposition extractors (GET /v2/agents/{uuid}/dispositions/extractor-catalog, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_v2_get_disposition_extractor_catalog'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def compat_v2_list_disposition_extractors(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """List v2 disposition extractors (GET /v2/agents/{uuid}/dispositions/extractors, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_v2_list_disposition_extractors'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def compat_v2_create_disposition_extractor(self, uuid: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Create v2 disposition extractor (POST /v2/agents/{uuid}/dispositions/extractors, scope agents:write)"""
        return self._call(
            OPERATIONS['compat_v2_create_disposition_extractor'],
            {'uuid': uuid},
            body,
            None,
            request_options,
        )

    def compat_v2_get_disposition_extractor(self, uuid: str, extractor_uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Get v2 disposition extractor (GET /v2/agents/{uuid}/dispositions/extractors/{extractor_uuid}, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_v2_get_disposition_extractor'],
            {'uuid': uuid, 'extractor_uuid': extractor_uuid},
            None,
            None,
            request_options,
        )

    def compat_v2_update_disposition_extractor_draft(self, uuid: str, extractor_uuid: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Update v2 disposition extractor draft (PATCH /v2/agents/{uuid}/dispositions/extractors/{extractor_uuid}/draft, scope agents:write)"""
        return self._call(
            OPERATIONS['compat_v2_update_disposition_extractor_draft'],
            {'uuid': uuid, 'extractor_uuid': extractor_uuid},
            body,
            None,
            request_options,
        )

    def compat_v2_publish_disposition_extractor(self, uuid: str, extractor_uuid: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Publish v2 disposition extractor (POST /v2/agents/{uuid}/dispositions/extractors/{extractor_uuid}/publish, scope agents:write)"""
        return self._call(
            OPERATIONS['compat_v2_publish_disposition_extractor'],
            {'uuid': uuid, 'extractor_uuid': extractor_uuid},
            body,
            None,
            request_options,
        )

    def compat_v2_get_disposition_extractor_version(self, uuid: str, extractor_uuid: str, version_uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Get v2 disposition extractor version (GET /v2/agents/{uuid}/dispositions/extractors/{extractor_uuid}/versions/{version_uuid}, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_v2_get_disposition_extractor_version'],
            {'uuid': uuid, 'extractor_uuid': extractor_uuid, 'version_uuid': version_uuid},
            None,
            None,
            request_options,
        )

    def compat_v2_get_disposition_model_profile_catalog(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """List v2 disposition extractor model profiles (GET /v2/agents/{uuid}/dispositions/model-profile-catalog, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_v2_get_disposition_model_profile_catalog'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def compat_v2_get_disposition_variable_catalog(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """List v2 disposition variable catalog (GET /v2/agents/{uuid}/dispositions/variable-catalog, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_v2_get_disposition_variable_catalog'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def compat_v2_get_disposition(self, uuid: str, disposition_uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Get v2 agent disposition (GET /v2/agents/{uuid}/dispositions/{disposition_uuid}, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_v2_get_disposition'],
            {'uuid': uuid, 'disposition_uuid': disposition_uuid},
            None,
            None,
            request_options,
        )

    def compat_v2_delete_disposition(self, uuid: str, disposition_uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Delete v2 agent disposition (DELETE /v2/agents/{uuid}/dispositions/{disposition_uuid}, scope agents:write)"""
        return self._call(
            OPERATIONS['compat_v2_delete_disposition'],
            {'uuid': uuid, 'disposition_uuid': disposition_uuid},
            None,
            None,
            request_options,
        )

    def compat_v2_disable_disposition(self, uuid: str, disposition_uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Disable v2 disposition (POST /v2/agents/{uuid}/dispositions/{disposition_uuid}/disable, scope agents:write)"""
        return self._call(
            OPERATIONS['compat_v2_disable_disposition'],
            {'uuid': uuid, 'disposition_uuid': disposition_uuid},
            None,
            None,
            request_options,
        )

    def compat_v2_get_disposition_draft(self, uuid: str, disposition_uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Get v2 disposition draft (GET /v2/agents/{uuid}/dispositions/{disposition_uuid}/draft, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_v2_get_disposition_draft'],
            {'uuid': uuid, 'disposition_uuid': disposition_uuid},
            None,
            None,
            request_options,
        )

    def compat_v2_update_disposition_draft(self, uuid: str, disposition_uuid: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Replace v2 disposition draft (PATCH /v2/agents/{uuid}/dispositions/{disposition_uuid}/draft, scope agents:write)"""
        return self._call(
            OPERATIONS['compat_v2_update_disposition_draft'],
            {'uuid': uuid, 'disposition_uuid': disposition_uuid},
            body,
            None,
            request_options,
        )

    def compat_v2_estimate_disposition(self, uuid: str, disposition_uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Estimate v2 disposition cost (POST /v2/agents/{uuid}/dispositions/{disposition_uuid}/estimates, scope agents:write)"""
        return self._call(
            OPERATIONS['compat_v2_estimate_disposition'],
            {'uuid': uuid, 'disposition_uuid': disposition_uuid},
            None,
            None,
            request_options,
        )

    def compat_v2_publish_disposition(self, uuid: str, disposition_uuid: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Publish v2 disposition (POST /v2/agents/{uuid}/dispositions/{disposition_uuid}/publish, scope agents:write)"""
        return self._call(
            OPERATIONS['compat_v2_publish_disposition'],
            {'uuid': uuid, 'disposition_uuid': disposition_uuid},
            body,
            None,
            request_options,
        )

    def compat_v2_list_disposition_runs(self, uuid: str, disposition_uuid: str, *, limit: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """List v2 disposition test runs (GET /v2/agents/{uuid}/dispositions/{disposition_uuid}/runs, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_v2_list_disposition_runs'],
            {'uuid': uuid, 'disposition_uuid': disposition_uuid, 'limit': limit},
            None,
            None,
            request_options,
        )

    def compat_v2_create_disposition_run(self, uuid: str, disposition_uuid: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Start v2 disposition test run (POST /v2/agents/{uuid}/dispositions/{disposition_uuid}/runs, scope agents:write)"""
        return self._call(
            OPERATIONS['compat_v2_create_disposition_run'],
            {'uuid': uuid, 'disposition_uuid': disposition_uuid},
            body,
            None,
            request_options,
        )

    def compat_v2_get_disposition_run(self, uuid: str, disposition_uuid: str, run_uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Get v2 disposition test run (GET /v2/agents/{uuid}/dispositions/{disposition_uuid}/runs/{run_uuid}, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_v2_get_disposition_run'],
            {'uuid': uuid, 'disposition_uuid': disposition_uuid, 'run_uuid': run_uuid},
            None,
            None,
            request_options,
        )

    def compat_v2_align_disposition_run(self, uuid: str, disposition_uuid: str, run_uuid: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Align v2 disposition test run (POST /v2/agents/{uuid}/dispositions/{disposition_uuid}/runs/{run_uuid}/align, scope agents:write)"""
        return self._call(
            OPERATIONS['compat_v2_align_disposition_run'],
            {'uuid': uuid, 'disposition_uuid': disposition_uuid, 'run_uuid': run_uuid},
            body,
            None,
            request_options,
        )

    def compat_v2_list_disposition_run_annotations(self, uuid: str, disposition_uuid: str, run_uuid: str, call_id: str, value_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """List v2 disposition test run corrections (GET /v2/agents/{uuid}/dispositions/{disposition_uuid}/runs/{run_uuid}/cases/{call_id}/annotations/{value_id}, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_v2_list_disposition_run_annotations'],
            {'uuid': uuid, 'disposition_uuid': disposition_uuid, 'run_uuid': run_uuid, 'call_id': call_id, 'value_id': value_id},
            None,
            None,
            request_options,
        )

    def compat_v2_put_disposition_run_annotation(self, uuid: str, disposition_uuid: str, run_uuid: str, call_id: str, value_id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Correct v2 disposition test run value (PUT /v2/agents/{uuid}/dispositions/{disposition_uuid}/runs/{run_uuid}/cases/{call_id}/annotations/{value_id}, scope agents:write)"""
        return self._call(
            OPERATIONS['compat_v2_put_disposition_run_annotation'],
            {'uuid': uuid, 'disposition_uuid': disposition_uuid, 'run_uuid': run_uuid, 'call_id': call_id, 'value_id': value_id},
            body,
            None,
            request_options,
        )

    def compat_v2_export_disposition_run_csv(self, uuid: str, disposition_uuid: str, run_uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Export v2 disposition test run CSV (GET /v2/agents/{uuid}/dispositions/{disposition_uuid}/runs/{run_uuid}/export-csv, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_v2_export_disposition_run_csv'],
            {'uuid': uuid, 'disposition_uuid': disposition_uuid, 'run_uuid': run_uuid},
            None,
            None,
            request_options,
        )

    def compat_v2_list_disposition_run_rows(self, uuid: str, disposition_uuid: str, run_uuid: str, *, limit: Any = None, offset: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """List v2 disposition test run rows (GET /v2/agents/{uuid}/dispositions/{disposition_uuid}/runs/{run_uuid}/rows, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_v2_list_disposition_run_rows'],
            {'uuid': uuid, 'disposition_uuid': disposition_uuid, 'run_uuid': run_uuid, 'limit': limit, 'offset': offset},
            None,
            None,
            request_options,
        )

    def compat_v2_list_disposition_versions(self, uuid: str, disposition_uuid: str, *, beforeVersion: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """List v2 disposition versions (GET /v2/agents/{uuid}/dispositions/{disposition_uuid}/versions, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_v2_list_disposition_versions'],
            {'uuid': uuid, 'disposition_uuid': disposition_uuid, 'beforeVersion': beforeVersion},
            None,
            None,
            request_options,
        )

    def compat_v2_get_disposition_version(self, uuid: str, disposition_uuid: str, version_uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Get v2 disposition version (GET /v2/agents/{uuid}/dispositions/{disposition_uuid}/versions/{version_uuid}, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_v2_get_disposition_version'],
            {'uuid': uuid, 'disposition_uuid': disposition_uuid, 'version_uuid': version_uuid},
            None,
            None,
            request_options,
        )

    def compat_v2_list_environments(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility v2 environments (GET /v2/agents/{uuid}/environments, scope deploy:read)"""
        return self._call(
            OPERATIONS['compat_v2_list_environments'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def compat_v2_get_staging_checks(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility v2 staging checks (GET /v2/agents/{uuid}/environments/staging/checks, scope deploy:read)"""
        return self._call(
            OPERATIONS['compat_v2_get_staging_checks'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def compat_v2_list_variables(self, uuid: str, env: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """List v2 agent environment variables (GET /v2/agents/{uuid}/environments/{env}/variables, scope deploy:read)"""
        return self._call(
            OPERATIONS['compat_v2_list_variables'],
            {'uuid': uuid, 'env': env},
            None,
            None,
            request_options,
        )

    def compat_v2_save_variable(self, uuid: str, env: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Create or replace a v2 agent environment variable (POST /v2/agents/{uuid}/environments/{env}/variables, scope agents:write)"""
        return self._call(
            OPERATIONS['compat_v2_save_variable'],
            {'uuid': uuid, 'env': env},
            body,
            None,
            request_options,
        )

    def compat_v2_put_variable(self, uuid: str, env: str, key: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Set a v2 agent environment variable (PUT /v2/agents/{uuid}/environments/{env}/variables/{key}, scope agents:write)"""
        return self._call(
            OPERATIONS['compat_v2_put_variable'],
            {'uuid': uuid, 'env': env, 'key': key},
            body,
            None,
            request_options,
        )

    def compat_v2_delete_variable(self, uuid: str, env: str, key: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Delete a v2 agent environment variable (DELETE /v2/agents/{uuid}/environments/{env}/variables/{key}, scope agents:write)"""
        return self._call(
            OPERATIONS['compat_v2_delete_variable'],
            {'uuid': uuid, 'env': env, 'key': key},
            None,
            None,
            request_options,
        )

    def compat_v2_list_experiments(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """List experiments (GET /v2/agents/{uuid}/experiments, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_v2_list_experiments'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def create_experiment(self, uuid: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Create and start experiment (POST /v2/agents/{uuid}/experiments, scope agents:write)"""
        return self._call(
            OPERATIONS['create_experiment'],
            {'uuid': uuid},
            body,
            None,
            request_options,
        )

    def get_experiment(self, uuid: str, experiment_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Get experiment (GET /v2/agents/{uuid}/experiments/{experiment_id}, scope agents:read)"""
        return self._call(
            OPERATIONS['get_experiment'],
            {'uuid': uuid, 'experiment_id': experiment_id},
            None,
            None,
            request_options,
        )

    def update_experiment(self, uuid: str, experiment_id: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Update experiment (PATCH /v2/agents/{uuid}/experiments/{experiment_id}, scope agents:write)"""
        return self._call(
            OPERATIONS['update_experiment'],
            {'uuid': uuid, 'experiment_id': experiment_id},
            body,
            None,
            request_options,
        )

    def get_experiment_results(self, uuid: str, experiment_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Get observed experiment results (GET /v2/agents/{uuid}/experiments/{experiment_id}/results, scope agents:read)"""
        return self._call(
            OPERATIONS['get_experiment_results'],
            {'uuid': uuid, 'experiment_id': experiment_id},
            None,
            None,
            request_options,
        )

    def stop_experiment(self, uuid: str, experiment_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Stop experiment (POST /v2/agents/{uuid}/experiments/{experiment_id}/stop, scope agents:write)"""
        return self._call(
            OPERATIONS['stop_experiment'],
            {'uuid': uuid, 'experiment_id': experiment_id},
            None,
            None,
            request_options,
        )

    def compat_v2_get_inbound(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility v2 inbound (GET /v2/agents/{uuid}/inbound, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_v2_get_inbound'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def organize_agent_pathways(self, uuid: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Create pathway folders, move pathways and save their order (POST /v2/agents/{uuid}/pathway-organization, scope agents:write)"""
        return self._call(
            OPERATIONS['organize_agent_pathways'],
            {'uuid': uuid},
            body,
            None,
            request_options,
        )

    def list_agent_scenarios(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """List an agent's scenarios (GET /v2/agents/{uuid}/scenarios, scope agents:read)"""
        return self._call(
            OPERATIONS['list_agent_scenarios'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def create_agent_scenario(self, uuid: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Add a scenario to an agent's draft (POST /v2/agents/{uuid}/scenarios, scope agents:write)"""
        return self._call(
            OPERATIONS['create_agent_scenario'],
            {'uuid': uuid},
            body,
            None,
            request_options,
        )

    def compat_v2_get_agent_scenario_history(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """The agent's own words per published version (GET /v2/agents/{uuid}/scenarios/agent/history, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_v2_get_agent_scenario_history'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def get_agent_scenario(self, uuid: str, scenario_uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """One scenario (GET /v2/agents/{uuid}/scenarios/{scenario_uuid}, scope agents:read)"""
        return self._call(
            OPERATIONS['get_agent_scenario'],
            {'uuid': uuid, 'scenario_uuid': scenario_uuid},
            None,
            None,
            request_options,
        )

    def update_agent_scenario(self, uuid: str, scenario_uuid: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Update a pathway in the agent's draft (POST /v2/agents/{uuid}/scenarios/{scenario_uuid}, scope agents:write)"""
        return self._call(
            OPERATIONS['update_agent_scenario'],
            {'uuid': uuid, 'scenario_uuid': scenario_uuid},
            body,
            None,
            request_options,
        )

    def delete_agent_scenario(self, uuid: str, scenario_uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Delete a scenario (from the draft, or from the archive) (DELETE /v2/agents/{uuid}/scenarios/{scenario_uuid}, scope agents:write)"""
        return self._call(
            OPERATIONS['delete_agent_scenario'],
            {'uuid': uuid, 'scenario_uuid': scenario_uuid},
            None,
            None,
            request_options,
        )

    def archive_agent_scenario(self, uuid: str, scenario_uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Archive a scenario (out of the draft, restorable) (POST /v2/agents/{uuid}/scenarios/{scenario_uuid}/archive, scope agents:write)"""
        return self._call(
            OPERATIONS['archive_agent_scenario'],
            {'uuid': uuid, 'scenario_uuid': scenario_uuid},
            None,
            None,
            request_options,
        )

    def copy_agent_scenario(self, uuid: str, scenario_uuid: str, body, *, request_options: dict[str, Any] | None = None) -> Any:
        """Copy a scenario to another agent of this workspace (POST /v2/agents/{uuid}/scenarios/{scenario_uuid}/copy, scope agents:write)"""
        return self._call(
            OPERATIONS['copy_agent_scenario'],
            {'uuid': uuid, 'scenario_uuid': scenario_uuid},
            body,
            None,
            request_options,
        )

    def compat_v2_get_scenario_history(self, uuid: str, scenario_uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """One scenario per published version (GET /v2/agents/{uuid}/scenarios/{scenario_uuid}/history, scope agents:read)"""
        return self._call(
            OPERATIONS['compat_v2_get_scenario_history'],
            {'uuid': uuid, 'scenario_uuid': scenario_uuid},
            None,
            None,
            request_options,
        )

    def restore_agent_scenario(self, uuid: str, scenario_uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Restore an archived scenario into the draft (POST /v2/agents/{uuid}/scenarios/{scenario_uuid}/restore, scope agents:write)"""
        return self._call(
            OPERATIONS['restore_agent_scenario'],
            {'uuid': uuid, 'scenario_uuid': scenario_uuid},
            None,
            None,
            request_options,
        )

    def compat_v2_list_versions(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility v2 versions (GET /v2/agents/{uuid}/versions, scope deploy:read)"""
        return self._call(
            OPERATIONS['compat_v2_list_versions'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def compat_v2_get_latest_version(self, uuid: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility v2 latest version (GET /v2/agents/{uuid}/versions/latest, scope deploy:read)"""
        return self._call(
            OPERATIONS['compat_v2_get_latest_version'],
            {'uuid': uuid},
            None,
            None,
            request_options,
        )

    def compat_v2_get_analytics_overview(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility v2 analytics overview (GET /v2/analytics/overview, scope calls:read)"""
        return self._call(
            OPERATIONS['compat_v2_get_analytics_overview'],
            {},
            None,
            None,
            request_options,
        )

    def create_batch(self, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Create and start a call batch (POST /v2/batches/create, scope calls:write)"""
        return self._call(
            OPERATIONS['create_batch'],
            {},
            None,
            idempotency_key,
            request_options,
        )

    def compat_v2_list_batches(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility v2 batches (GET /v2/batches/list, scope calls:read)"""
        return self._call(
            OPERATIONS['compat_v2_list_batches'],
            {},
            None,
            None,
            request_options,
        )

    def compat_v2_get_batch_file_schema(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Compatibility v2 batch file schema (GET /v2/batches/schema/files, scope calls:read)"""
        return self._call(
            OPERATIONS['compat_v2_get_batch_file_schema'],
            {},
            None,
            None,
            request_options,
        )

    def get_batch(self, batch_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Get batch (GET /v2/batches/{batch_id}, scope calls:read)"""
        return self._call(
            OPERATIONS['get_batch'],
            {'batch_id': batch_id},
            None,
            None,
            request_options,
        )

    def get_batch_logs(self, batch_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """Get batch attempts (GET /v2/batches/{batch_id}/logs, scope calls:read)"""
        return self._call(
            OPERATIONS['get_batch_logs'],
            {'batch_id': batch_id},
            None,
            None,
            request_options,
        )

    def advance_batch(self, batch_id: str, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Advance due batch recipients (POST /v2/batches/{batch_id}/run, scope calls:write)"""
        return self._call(
            OPERATIONS['advance_batch'],
            {'batch_id': batch_id},
            None,
            idempotency_key,
            request_options,
        )

    def stop_batch(self, batch_id: str, *, idempotency_key: str | None = None, request_options: dict[str, Any] | None = None) -> Any:
        """Stop queued batch recipients (POST /v2/batches/{batch_id}/stop, scope calls:write)"""
        return self._call(
            OPERATIONS['stop_batch'],
            {'batch_id': batch_id},
            None,
            idempotency_key,
            request_options,
        )

    def list_models_v2_public(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """Public, unauthenticated model discovery (GET /v2/models)"""
        return self._call(
            OPERATIONS['list_models_v2_public'],
            {},
            None,
            None,
            request_options,
        )

    def list_workspace_scenarios(self, *, agent_id: Any = None, request_options: dict[str, Any] | None = None) -> Any:
        """Every agent's scenarios in this workspace (GET /v2/scenarios, scope agents:read)"""
        return self._call(
            OPERATIONS['list_workspace_scenarios'],
            {'agent_id': agent_id},
            None,
            None,
            request_options,
        )

    def list_tts_models_v2(self, *, request_options: dict[str, Any] | None = None) -> Any:
        """List what each Sempera TTS model supports (GET /v2/tts/models, scope models:read)"""
        return self._call(
            OPERATIONS['list_tts_models_v2'],
            {},
            None,
            None,
            request_options,
        )

    def get_tts_model_v2(self, model_id: str, *, request_options: dict[str, Any] | None = None) -> Any:
        """What one Sempera TTS model supports (GET /v2/tts/models/{model_id}, scope models:read)"""
        return self._call(
            OPERATIONS['get_tts_model_v2'],
            {'model_id': model_id},
            None,
            None,
            request_options,
        )
