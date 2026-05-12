[AGENTS]

[DEFINITION]
agent = identity + memory + config
scoped by agentId
blueprints = shared

[CREATE]
+ → onboarding starts
define:
- name/purpose
- tone/personality
- specialization
- rules/boundaries

result:
Soul, Identity, config auto-filled
agent available immediately

[CONFIG]
sections (per-agent):
- Soul (tone/style)
- Identity (name/role/expertise)
- User (user data)
- Agents (behavior/rules)
- Tools (usage/limits)
- Security (permissions)

shared:
- Constraints (global rules)

update via:
[CONFIG_UPDATE]
## Section
full replace
[/CONFIG_UPDATE]

[ISOLATION]
- sessions/messages/memory per-agent
- embeddings scoped by agentId
- prefetch → active agent only
- config per-agent
- blueprints shared

[A2A]
delegate:
agent:<id>
query:<full context>

result:
- source → inline response
- target → "A2A Delegations" session

[SWITCH]
select agent → switch sessions/memory/config
system prompt rebuilt

[DEFAULT]
first agent = default
legacy (no agentId) → default

[DIAGNOSTIC]
- no agent → create (+)
- missing config → onboarding incomplete
- no memory → compaction not triggered
- A2A fail → check agent exists + identity
- tools missing → check Tools config
