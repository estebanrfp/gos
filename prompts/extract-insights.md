Extract durable knowledge from a memory record.

Output JSON ONLY. No prose, no markdown fences, no explanations.

[INPUT]
content (ignore headers like [Session | date])
context (eventType, participants, date)

[RULE]
- identify main topic
- if single coherent topic → ONE insight
- split ONLY if clearly distinct topics
- prefer cohesion (lists under same subject = one)
- no inference or invention

[SKIP]
- greetings, small talk, status checks
- ephemeral Q&A, tool outputs, confirmations
- system/memory/meta references

[STYLE]
- preserve tone/vocabulary (no embellishment)
- resolve pronouns → explicit names when clear
- use absolute dates when known
- self-contained, readable long-term

[FORMAT]
content: 1–4 sentences (same language)
summary: 1 keyword-rich sentence (same language)

[LANG]
output language = source language, no translation
preserve names, numbers, dates, technical terms verbatim

[OUTPUT]
{"insights":[{"content":"...","summary":"..."}]}

If nothing durable qualifies: {"insights":[]}
