# AI Summarization Handbook

A beginner-friendly, **free AI** handbook for summarizing articles, meeting notes, documents, and emails. Written in plain English, step by step, never condescending.

Created by **Asdale Dynamics, LLC** — founded by Dylan Asdale (registered nurse turned AI author) to teach AI "like a friend would."

## What you get

- **`docs/`** — the full written manual (Markdown), chapter by chapter
- **`site/`** — a polished, self-contained static HTML site you can open locally
- **`site/cheatsheet.html`** — a single-page printable cheat sheet (Ctrl+P / Print)
- Prompt templates, a local-vs-cloud checklist, length & tone controls, and a data-hygiene primer

## How to read

- Open `site/index.html` in any browser — no server needed
- Or read the plain-text chapters in `docs/`
- Hit the **Cheat Sheet** page and print it for your desk

## Free AI this covers

**Cloud (free tiers):** ChatGPT (Free/Plus), Claude.ai (Free), Google Gemini, Microsoft Copilot, Hugging Face Chat
**Local (100 % free):** Ollama with Llama 3 / Gemma / Phi-3 / Qwen; AnythingLLM; LM Studio

> No paid subscriptions required. No API keys collected. This repo ships **no code that makes outbound requests** — you paste from your own free accounts.

## Building the site from source

The HTML site is generated from the Markdown in `docs/` by a small Python build script:

```bash
python3 build.py
```

This produces/refreshes everything under `site/`. It also runs link validation and secret-scanning checks and fails loudly if anything is broken.

## Verify everything works

```bash
python3 build.py            # builds site + runs checks
python3 verify.py           # re-runs all verification checks
```

## Copyright & license

Copyright (c) 2026 Asdale Dynamics, LLC. Licensed under the MIT License — see [LICENSE](LICENSE).

Credit: Asdale Dynamics, LLC.
