# Prompt template library

Copy and paste these into your AI tool. Replace `[BRACKETED]` text with your own (sanitized) content.

## Articles

### TL;DR (one paragraph)

```
Summarize this article in one short paragraph. Main point and why it matters, plain English.

[ARTICLE TEXT]
```

### 5 bullet points

```
Summarize this article in 5 short bullets: what happened, who it affects, what comes next. Plain English, no jargon.

[ARTICLE TEXT]
```

### Explain like I’m 12

```
Explain this article like I am 12. Simple words, short sentences, one analogy. No jargon.

[ARTICLE TEXT]
```

## Meeting notes

### Decisions + actions

```
Summarize these meeting notes into: decisions made, action items (owner + due date), open questions. Skimmable, plain English.

[MEETING NOTES]
```

### Action items only

```
Extract every action item: task, owner, due date, priority (high/medium/low). Mark missing info as [TBD].

[MEETING NOTES]
```

## Documents

### Executive brief

```
Summarize this document: purpose, key provisions, obligations, deadlines, risks. Professional tone, max 300 words.

[DOCUMENT TEXT]
```

### What do I need to do?

```
List every action or obligation in this document: what to do, by when, penalty for missing. Mark unclear items as [UNCLEAR].

[DOCUMENT TEXT]
```

## Emails

### Thread summary

```
Summarize this email thread: what each person wants, decisions, action items and deadlines, open questions. Under 100 words.

[EMAIL THREAD]
```

### Invoice extraction

```
Extract: invoice number, amount due, due date, payee, payment instructions. Flag anything missing.

[EMAIL]
```

## Length & tone controls

Add one of these to any prompt:

| Goal | Add this phrase |
|---|---|
| Short | “Keep it under 100 words” / “one paragraph” |
| Longer / detailed | “Be thorough” / “include key details” |
| Professional | “Professional tone, executive style” |
| Casual / friendly | “Friendly, casual tone” |
| Simple | “Explain like I’m new to this” / “plain English” |
| Bullet list | “Use bullet points” |
| Table | “Present as a table” |

### Combined example

```
Summarize this article in 4 bullet points, friendly tone, plain English. Under 120 words.

[ARTICLE TEXT]
```

> **Credit:** Asdale Dynamics, LLC. Copyright (c) 2026 Asdale Dynamics, LLC. MIT License.
