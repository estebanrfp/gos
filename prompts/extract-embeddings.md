Extract the searchable facts from a memory.

Output JSON ONLY. No prose, no markdown fences, no explanations.

Each fact becomes an embedding pointing at this memory — they are never
stored as text and never shown to anyone.

Create one short, self-contained sentence per distinct fact worth later
retrieval, not per topic. Include the entity, action or attribute, key
details, date, specs, reason and purpose when relevant. Merge details
about the same thing; split only facts likely searched separately. Most
memories yield 3-8 facts; up to 20 only if truly dense — more usually
means over-splitting.

- Same language as the source.
- State facts, never the conversation: no "explored", "discussed", "analyzed".
- No inference, no invention. A single-fact memory returns one.

{"embeddings":["...","..."]}
