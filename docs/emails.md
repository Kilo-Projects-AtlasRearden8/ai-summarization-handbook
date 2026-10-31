# Summarizing emails

Email is where summarization saves the most time day to day — long threads, invoice chases, meeting requests, and newsletters all shrink into a few lines.

## Step by step

1. **Copy the thread.** Paste the full email chain, or the most recent message plus context.
2. **Sanitize.** Replace sender/recipient names (if private), invoice numbers, amounts, account numbers, and addresses with placeholders.
3. **Ask for the “so what.”** Decisions, requests, and deadlines matter more than pleasantries.
4. **Draft the reply.** Use the summary to write a short, clear response.

## Prompt templates for emails

**Thread summary:**
```
Summarize this email thread into:
- What each person wants
- Decisions made
- Action items and deadlines
- Any open questions

Keep it under 100 words, plain English.

[PASTE EMAIL THREAD]
```

**Invoice / payment chase:**
```
This is an email about an invoice. Extract: invoice number, amount due, due date, payee, and any payment instructions. Flag anything missing. Plain English.

[PASTE EMAIL]
```

**Meeting request:**
```
Someone is asking me to meet. Extract: proposed date/time, meeting purpose, who is requesting, and how long they want. Draft a short, polite reply accepting or proposing a new time.

[PASTE EMAIL]
```

**Inbox triage:**
```
I have 20 emails. For each, give me a one-line summary: who it is from, what they want, and whether it needs action today. Plain English.

[PASTE EMAIL LIST]
```

## Safety note for email

Email often contains invoices, account numbers, personal data, and confidential business info. **Sanitize before you paste.** For sensitive correspondence, use a local LLM.

> **Credit:** Asdale Dynamics, LLC. Copyright (c) 2026 Asdale Dynamics, LLC. MIT License.
