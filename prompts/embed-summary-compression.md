Compress text → fewer tokens, same meaning.

OUTPUT RULES (strict):
- Output ONLY the compressed text, nothing else
- No preamble ("Here is...", "Compressed:", etc)
- No explanation, no alternatives, no commentary
- Same language as input
- Must be SHORTER than input

Keep:
- names, numbers, dates, facts
- negations (no, never)
- key relations (with, from, to)
- main verbs

Remove:
- articles (the, el, la)
- weak verbs (is, was, es)
- redundant pronouns
- intensifiers (very, muy)

Rules:
- DO NOT change meaning
- DO NOT lose facts
- DO NOT flip polarity
- keep grammar simple but readable
- combine sentences when possible

TEXT TO COMPRESS:
{text}
