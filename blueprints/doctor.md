[DOCTOR]

[DEFINITION]
system health check (server, auth, memory, agents, tools)

[AREAS]

[SERVER]
- GET /health
- WS connected (console logs)
- port 4400 (lsof)

[AUTH]
- SM initialized (logs)
- WebAuthn active
- credentials in genosconfig

[MEMORY]
- embeddings → local Qwen3 loaded
- compaction → mem_index
- subscriptions → logs

[AGENTS]
- agent exists (agent_index)
- onboarded (Soul/Identity)
- sessions exist (session_index)

[TOOLS]
- WS connected
- exec works (ls .)
- command validation active

[CHECK_FLOW]
1 exec → curl /health
2 exec → lsof :4400
3 ls .
4 read package.json

[OUTPUT]
- start: "N issues" / "all good"
- explain issues + suggest fixes
- no raw dumps
- order: critical → warnings → info
