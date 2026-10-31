# STATUS — AI Summarization Handbook

## What was built

A beginner manual + static HTML site on summarizing articles, meeting notes, documents, and emails with **free AI** (cloud free tiers + local LLMs). Written in plain English, step by step, never condescending. Credits Asdale Dynamics, LLC throughout.

**Contents**
- `docs/` — 11 Markdown chapters (single source of truth):
  - `introduction.md` — welcome & overview
  - `free-tools.md` — cloud free tiers + local LLMs (Ollama, LM Studio, AnythingLLM)
  - `safety.md` — paste safely, never IDs or financial data, sanitize with placeholders
  - `articles.md` / `meeting-notes.md` / `documents.md` / `emails.md` — per-type walkthroughs
  - `prompt-templates.md` — copy-and-paste prompt library
  - `local-vs-cloud.md` — which to use when
  - `length-tone.md` — length & tone controls
  - `cheatsheet.md` — printable cheat sheet source
- `static/style.css` + `static/print.css` — shared styles, print-ready cheat sheet
- `build.py` — converts `docs/*.md` -> `site/*.html` with nav + CSS; validates links
- `verify.py` — HTML well-formedness, internal-link resolution, secret scan
- `site/` — generated static HTML site (11 pages, open `site/index.html` locally, no server)
- `site/cheatsheet.html` — one-page printable cheat sheet (Ctrl+P / Print)
- `LICENSE` — MIT, copyright line exactly `Copyright (c) 2026 Asdale Dynamics, LLC`
- `README.md` — credits Asdale Dynamics, LLC
- `AGENTS.md` — project layout, commit policy, commands
- `.markdownlint.json` — lint config for the manual source

## How to run

```bash
# Build the static site from Markdown (also runs link validation)
python3 build.py

# Open the site locally in any browser (no server needed)
#   file:///<path>/ai-summarization-handbook/site/index.html

# Re-run all verification checks standalone
python3 verify.py

# Lint the Markdown source
markdownlint docs/
```

## Verification results

- `python3 build.py` — PASS: built 11 pages into `site/`; CSS assets copied
- `python3 verify.py` — PASS: all HTML well-formed, all internal links resolve, no secrets/API keys/personal-data patterns detected
- `markdownlint docs/` — PASS: no lint errors

No `.github/workflows` files present. No remote repository created. Nothing pushed.

## Known gaps

- Cheat sheet is printable via browser (Ctrl+P / Print); no generated PDF artifact.
- No built-in site search (static HTML, small enough to navigate by nav menu).
- Examples use placeholder text (`[PATIENT]`, `[AMOUNT]`, etc.) by design — no live AI integration, no API keys, no secrets.
- Healthcare/legal/finance sections note that this is education only, never medical or legal advice; a qualified professional should review binding documents.
