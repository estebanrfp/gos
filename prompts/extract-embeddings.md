Extract the searchable facts from a memory.

Output JSON ONLY. No prose, no markdown fences, no explanations.

Each fact becomes an embedding pointing at this memory — they are never
stored as text and never shown to anyone.

- One short sentence per fact worth finding on its own, not per theme.
  "Esteban tenía una bicicleta plateada" is one. Up to 20.
- Same language as the source, keyword-rich, self-contained: name the people,
  places and things, because a fact is matched alone with no surrounding context.
- A list of items under one subject is ONE fact, not one per item.
- Keep identifiers verbatim: names, numbers, dates, addresses, keys.
- No inference, no invention. If the memory holds a single fact, return one.

{"embeddings":["...","..."]}
