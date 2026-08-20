# Prompts

All system prompts for GenosOS in TOON format. Editable without code changes — modify any `.md` file and restart the server (`loadPrompt` caches in RAM).

All prompts are optimized for minimal token usage while preserving full functionality. Format: compact TOON `[SECTION]` headers understood natively by modern LLMs (Qwen, Gemma, etc.).

## Chat & Channels

| File | Used by | Purpose |
|------|---------|---------|
| `system-prompts.md` | Chat, WhatsApp, Telegram, Discord, Slack, iMessage | Main system prompt — role, memory doctrine, tools, delegation, [CONFIG] sections list |
| `security.md` | Chat, WhatsApp, Telegram, Discord, Slack, iMessage | Adversarial defenses — anti-injection, scope of trust, credentials, action permissions, channel restrictions. **System tier** — universal across all agents, audit-friendly, only changeable via code commit. See CLAUDE.md Architecture Invariant 13. |
| `init.md` | First message with a new agent | Onboarding conversation flow |
| `onboarding-extract.md` | After onboarding completes | Extracts 4 config buckets (Soul, Identity, User, Rules) from conversation |

## Voice

| File | Used by | Purpose |
|------|---------|---------|
| `system-prompts-voice.md` | Talk Local, Voice SIP | Voice preamble + rules, tone, style |
| `stall-phrases.md` | Voice SIP | Cold-start filler phrases (one per line) |
| `call-purpose.md` | Voice SIP (dispatched calls) | Purpose injection for outbound calls |
| `post-call.md` | Voice SIP | Post-call transcript processing (tool actions only — memory already saved) |

## Memory — capture & compaction

| File | Used by | Purpose |
|------|---------|---------|
| `compact-structured.md` | Session compaction (primary path) | One-pass JSON extraction: `sessionSummary` + topics |
| `compact-label.md` | Every memory write path | Compact headline (40–80 chars) for graph labels and edge annotations. Polarity-preserving |

## Memory — knowledge graph

| File | Used by | Purpose |
|------|---------|---------|
| `extract-insights.md` | Brain (`analyzeMemoryWithBrain`) | Distills durable knowledge from an episodic record into insights |
| `merge-similar.md` | Runtime enrichment (`decideSimilar`) | Merges an incoming note into a stored one, or `UNRELATED`. NEIGHBOR is the newer note and wins on conflicting values |
| `classify-source.md` | Brain pre-check | `SINGLE_TOPIC` vs `MULTI_TOPIC` — decides whether a source gets fragmented |
| `classify-topic.md` | Global Consolidate path | `SAME_TOPIC` vs `UNRELATED` — classification only; the server concatenates literally (Principle 6) |
| `consolidate-memories.md` | Auto-link (`linkNewMemory`) | Finds meaningful edges between memories. JSON-only output |
| `patch-json.md` | JSON memory enrichment | Updates a JSON fragment with new data |

## Memory — embeddings

| File | Used by | Purpose |
|------|---------|---------|
| `summarize-for-embed.md` | Long text (>500 chars) | Topic summaries for semantic embedding |
| `summarize-json-for-embed.md` | JSON documents | JSON interpretation for searchable embedding |
| `embed-summary-compression.md` | `cavemanCompressed` (manual, per record) | Record-level compression preserving facts and polarity |

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
| `{{SOURCE_NAME}}`, `{{SOURCE_ID}}` | `agent-to-agent.md` | Sender agent name and ID |
| `{{TARGET_NAME}}`, `{{TARGET_ID}}` | `agent-to-agent.md` | Receiver agent name and ID |
| `{{PARTICIPANT_NAME}}` | `room-mode.md` | Agent name in the room |

Prompts with `{placeholder}` (single braces) are filled by `String.replace` at the call site: `{text}`, `{current_text}`, `{neighbor_text}`, `{text_a}`, `{text_b}`.

## Author

Esteban Fuster Pozzi (@estebanrfp) — Full Stack JavaScript Developer
