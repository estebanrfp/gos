# Prompts

All system prompts for GenosOS in TOON format. Editable without code changes — modify any `.md` file and restart the server.

All prompts are optimized for minimal token usage while preserving full functionality. Format: compact TOON `[SECTION]` headers understood natively by modern LLMs (Qwen, Gemma, etc.).

## Chat & Channels

| File | Used by | Purpose |
|------|---------|---------|
| `system-prompts.md` | Chat, WhatsApp, Telegram, Discord, Slack, iMessage | Main system prompt (TOON, ~330 tokens) — role, memory format, tools, delegation, [CONFIG] sections list |
| `security.md` | Chat, WhatsApp, Telegram, Discord, Slack, iMessage | Adversarial defenses (TOON, ~430 tokens) — anti-injection, scope of trust, credentials, action permissions, channel restrictions. **System tier** — universal across all agents, audit-friendly, only changeable via code commit. See CLAUDE.md Architecture Invariant 13. |
| `init.md` | First message with a new agent | Onboarding conversation flow |
| `onboarding-extract.md` | After onboarding completes | Extracts 4 config buckets (Soul, Identity, User, Rules) from conversation |

## Voice

| File | Used by | Purpose |
|------|---------|---------|
| `system-prompts-voice.md` | Talk Local, Voice SIP | Voice preamble + rules, tone, style (TOON, ~190 tokens) |
| `stall-phrases.md` | Voice SIP | Cold-start filler phrases (one per line) |
| `call-purpose.md` | Voice SIP (dispatched calls) | Purpose injection for outbound calls |
| `post-call.md` | Voice SIP | Post-call transcript processing |
| `talk-local-summary.md` | Talk Local (browser mic) | Post-session transcript processing |

## Memory

| File | Used by | Purpose |
|------|---------|---------|
| `compaction.md` | Session compaction | Durable vs ephemeral memory criteria |
| `summarize-for-embed.md` | Long text (>500 chars) | Topic summaries for semantic embedding |
| `summarize-json-for-embed.md` | JSON documents | JSON interpretation for searchable embedding |
| `merge-memory.md` | Memory enrichment | Merge two entries preserving all facts |
| `patch-json.md` | JSON memory enrichment | Update JSON fragment with new data |
| `transform-memory.md` | Memory transformation | Raw data → first-person experiences |

## Multi-Agent

| File | Used by | Purpose |
|------|---------|---------|
| `agent-to-agent.md` | A2A delegation | Context for inter-agent communication |
| `room-mode.md` | Multiagent rooms | Behavior rules for group conversations |

## Template Variables

Some prompts use `{{VARIABLE}}` placeholders replaced at runtime:

| Variable | Used in | Replaced with |
|----------|---------|---------------|
| `{{PURPOSE}}` | `call-purpose.md` | The dispatched call instruction |
| `{{TRANSCRIPT}}` | `post-call.md` | Phone call transcript |
| `{{AGENT_NAME}}` | `transform-memory.md` | Agent display name |
| `{{SOURCE_NAME}}`, `{{SOURCE_ID}}` | `agent-to-agent.md` | Sender agent name and ID |
| `{{TARGET_NAME}}`, `{{TARGET_ID}}` | `agent-to-agent.md` | Receiver agent name and ID |
| `{{PARTICIPANT_NAME}}` | `room-mode.md` | Agent name in the room |

## Author

Esteban Fuster Pozzi (@estebanrfp) — Full Stack JavaScript Developer
