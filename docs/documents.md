# Summarizing documents

Documents — contracts, policies, reports, manuals — are usually longer and more formal than articles or emails. You often need the *structure*, not just the gist.

## Step by step

1. **Copy the text.** For PDFs, copy-paste the text or use a tool that extracts PDF text. Very long documents may need to be pasted in sections.
2. **Sanitize.** Replace party names, contract values, account numbers, and dates with placeholders.
3. **Ask for what you need.** Do you want an executive summary? A clause-by-clause breakdown? A list of obligations and deadlines? Say so.
4. **Verify critical items.** AI can misread a “shall” as a “may.” Check deadlines, penalties, and payment terms against the original.
5. **Keep the source.** Never replace a signed contract with an AI summary.

## Prompt templates for documents

**Executive summary:**
```
Summarize this document as an executive brief: purpose, key provisions, obligations, deadlines, and risks. Professional tone, max 300 words.

[PASTE DOCUMENT TEXT]
```

**Clause checklist:**
```
Read this document and list: (1) each major clause or section, (2) what it requires, and (3) any deadlines or dates. Use plain English. Flag anything unusual.

[PASTE DOCUMENT TEXT]
```

**“What do I need to do?”:**
```
From this document, extract every action or obligation I have. List each with: what to do, by when, and any penalty for missing it. If unclear, say [UNCLEAR].

[PASTE DOCUMENT TEXT]
```

## Watch out for

- **Length limits:** Free cloud tools may truncate very long documents. Paste sections separately and combine summaries manually.
- **Legal weight:** An AI summary is not legal advice. For contracts, leases, or anything with money or liability attached, have a qualified professional review it.
- **Scanned PDFs:** If the text is an image (scanned), you will need OCR first. Most AI chat tools cannot read image-only PDFs.

> **Credit:** Asdale Dynamics, LLC. Copyright (c) 2026 Asdale Dynamics, LLC. MIT License.
