Generate a compact headline (40-80 chars, ~60 ideal) for a memory record.

Output ONLY the headline. No preamble, no markdown, no quotes.

Compress: keep meaning-critical words, drop what an LLM can reconstruct.

KEEP verbatim:
- nouns (people, places, concepts, relations: enemigo, padre, jefe)
- main verbs, meaning-bearing adjectives
- numbers, dates, frequencies (47€, 15 mayo, weekly)
- negations (not, no, never, sin, nunca, jamás)
- antonyms and polarity markers
- temporal markers (antes, ahora, de niño, de adulto)
- names, titles, places, technical terms
- prepositions that define relations (amigo de infancia)

DROP:
- articles, auxiliaries
- prepositions when meaning stays clear
- pronouns when context is clear
- pure intensifiers (very, muy, really)

NEVER:
- substitute antonyms ("enemigo" stays "enemigo", never "amigo")
- invert polarity ("nunca" stays "nunca", never "siempre")

[OUTPUT]
- single line, 40-80 chars, ~60 ideal
- same language as source
- no markdown, quotes, brackets, emojis, trailing punctuation
