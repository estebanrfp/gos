[SESSIONS]

[DEFINITION]
sessions = per-agent conversation history
stored as graph nodes (GenosDB)
scoped by agentId

[CREATE]
+ → new session
auto title (timestamp)
linked to active agent

[STRUCTURE]
- session_node (encrypted): title, agentId, createdAt
- session_index (public): ref, title, agentId, createdAt
- messages → linked via sessionId

[FLOW]
1 user → encrypted node + msg_index
2 agent → encrypted node + msg_index
3 accumulate → compaction threshold

[COMPACTION]
trigger: enough messages

process:
- send uncompacted → LLM
- generate TOON (9 categories):
  People, Decisions, Preferences, Projects,
  Context, Constraints, Moments, Content, Open Questions
- per-category embeddings
- mark messages compacted (not deleted)
- update single TOON node (overwrite)

[CONTEXT_PIPELINE]
input to LLM:
1 session TOON
2 recent (uncompacted → inline TOON)
3 prefetch (cross-session search)
4 new message

no raw chat history

[SWITCH]
select session → load msg_index
TOON provides continuity

[DELETE]
remove session_node + msg_index
embeddings persist

[A2A]
delegation → "A2A Delegations" session
flag: a2a=true

[ISOLATION]
- filter by agentId
- new sessions tagged with agentId
- switching agent → filtered view
- legacy (no agentId) → default agent

[DIAGNOSTIC]
- no sessions → check active agent
- no memory → compaction not triggered
- stale context → check recent + TOON update
- missing A2A → verify agent + delegation
