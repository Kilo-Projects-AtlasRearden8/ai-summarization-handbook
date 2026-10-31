# Project: AI Summarization Handbook

A beginner manual + static site on summarizing articles, meeting notes, documents,
and emails with free AI (cloud free tiers + local LLMs).

## Identity

- Git identity (used for all commits): `Dylan Asdale <dylanasdale@users.noreply.github.com>`
- Project authored by Asdale Dynamics, LLC.
- License: MIT (Copyright (c) 2026 Asdale Dynamics, LLC).

## Layout

- `docs/`            — Markdown source chapters (single source of truth)
- `static/`          — shared CSS (style.css, print.css) consumed by the build
- `build.py`         — converts `docs/*.md` -> `site/*.html` with nav + styling; runs sanity checks
- `verify.py`        — re-runs validation (HTML well-formedness, internal links, secret scan)
- `site/`            — generated static site (gitignored at source level but committed here as built output)
- `STATUS.md`        — what was built, how to run, verification results, known gaps

## Commit policy

- Plain, human-readable commit messages.
- No `Co-authored-by:` trailers.
- No remote creation, no push.
- No secrets, API keys, or personal data in any file.
- No `.github/workflows` files.

## Commands

```bash
python3 build.py      # build site + validate
python3 verify.py     # standalone verification
```
