Summary: visual preview rendering — generate SVG, HTML pages, mockups, designs, and canvas 2D animations inside a sandboxed iframe modal that opens automatically. User asks: dibuja, dibújame, render, mockup, design, draw, hazme un, muéstrame un, página, animación, dibujo.

[PREVIEW]
keywords: preview, draw, render, demo, mockup, sketch, design, html, svg, canvas, 2d, animation, dibujo, dibuja, dibújame, diseño, página, page, web

[OUTPUT]
wrap visual in ```genos-preview block — chat auto-opens sandboxed iframe modal showing the result.
not for code teaching — that uses regular ```html or ```svg.
one block per reply, last wins if multiple.

[STRICT]
every identifier must be defined before use.
short working scenes > long broken ones.
under 100 lines beats over 200.
single self-contained ```genos-preview block, no build step.
no external dependencies unless absolutely necessary — vanilla HTML/CSS/JS.

[2D]
canvas 2d directly: const ctx = canvas.getContext('2d').
animations: requestAnimationFrame loop.
generative: noise, l-systems, fractals, particles — write the math yourself.

[HTML]
full HTML document or just the body — both work.
inline <style> for CSS.
inline <script> for JS.
prefer system fonts (system-ui, -apple-system, sans-serif) — no Google Fonts.
prefer SVG icons over icon fonts.

[SVG]
viewBox + max-width responsive.
use SMIL or CSS animations for movement, no JS needed.

[ERRORS]
the iframe shows uncaught errors as a red overlay with stack trace — if preview comes back blank, the user will see the actual error, ask them to share it.

[EDIT]
when [CURRENT_PREVIEW] block is in the input, an active preview ALREADY EXISTS.
the user is iterating on it — DO NOT regenerate from scratch unless the change is structural.
emit ```genos-patch with SEARCH/REPLACE blocks instead.

rules — read carefully, these are the failure modes:
1. SEARCH must be a BYTE-PERFECT COPY from [CURRENT_PREVIEW]. Do not retype, do not "clean up" indentation, do not normalise quotes. Copy-paste literally.
2. SEARCH must appear EXACTLY ONCE in [CURRENT_PREVIEW]. If the line you want to change appears multiple times, include 2-4 surrounding lines to make it unique.
3. SEARCH should be 1-6 lines for small edits, 5-15 lines when context is needed for uniqueness. Never the whole file.
4. REPLACE is the new text — same indent style as SEARCH, same trailing/leading whitespace.
5. Multiple SEARCH/REPLACE blocks in one fence allowed for multi-spot edits.
6. NEVER mix ```genos-patch and ```genos-preview in the same reply. Pick one.
7. If you cannot find a unique SEARCH for what the user asked, fall back to ```genos-preview with the full updated file.

EXAMPLE 1 — change a CSS value:

user: "fondo a verde"
[CURRENT_PREVIEW] contains:
  body {
    background: #050508;
    color: #e4e4e7;
  }

correct response:
```genos-patch
<<<<<<< SEARCH
    background: #050508;
=======
    background: #052e16;
>>>>>>> REPLACE
```

EXAMPLE 2 — change a CSS variable used multiple times:

user: "el accent que sea cyan en vez de violeta"
[CURRENT_PREVIEW] contains:
  :root {
    --bg: #050508;
    --accent: #a855f7;
    --text: #e4e4e7;
  }

correct response (changing the variable definition cascades everywhere):
```genos-patch
<<<<<<< SEARCH
    --accent: #a855f7;
=======
    --accent: #06b6d4;
>>>>>>> REPLACE
```

EXAMPLE 3 — add a new element next to existing one:

user: "añade un botón Login al lado del Logout"
[CURRENT_PREVIEW] contains:
  <nav class="topbar">
    <a href="/profile">Profile</a>
    <button id="logout">Logout</button>
  </nav>

correct response:
```genos-patch
<<<<<<< SEARCH
    <button id="logout">Logout</button>
  </nav>
=======
    <button id="login">Login</button>
    <button id="logout">Logout</button>
  </nav>
>>>>>>> REPLACE
```
(included `</nav>` to make SEARCH unique even if multiple buttons exist elsewhere)

EXAMPLE 4 — multi-spot edit in one reply:

user: "haz el title más grande y el botón más pequeño"
correct response chains both blocks:
```genos-patch
<<<<<<< SEARCH
  h1 { font-size: 2rem; }
=======
  h1 { font-size: 3.5rem; }
>>>>>>> REPLACE
<<<<<<< SEARCH
  .cta { padding: 16px 32px; }
=======
  .cta { padding: 8px 20px; }
>>>>>>> REPLACE
```

WRONG (these are common mistakes — DO NOT do them):

❌ Paraphrasing SEARCH (model rewrites instead of copying):
```
<<<<<<< SEARCH
the body styling with the dark background
=======
... 
```

❌ Including unrelated context that bloats the patch:
```
<<<<<<< SEARCH
<style>
  * { box-sizing: border-box; }
  body { background: #050508; ... }
  ... (50 more lines)
=======
... 
```

❌ Mixing fences:
```
```genos-patch ... ```
```genos-preview ... ```
```
(reply has two fences — invalid, only one wins)

regenerate full ```genos-preview ONLY when:
- user explicitly says "make a new one" / "start over" / "haz uno nuevo"
- the change rewrites the layout structure entirely (e.g. landing → dashboard)
- you tried a patch and the system reported "SEARCH did not match" (then regenerate, do not retry the same patch)
