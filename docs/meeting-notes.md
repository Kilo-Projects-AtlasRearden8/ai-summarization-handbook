# Summarizing meeting notes

Meetings generate a lot of words — and not all of them matter. A good summary turns a rambling transcript or rough notes into a short list of **decisions, action items, and next steps.**

## Step by step

1. **Gather your notes.** Paste raw meeting notes, a transcript, or bullet points from the whiteboard.
2. **Sanitize first.** Replace attendee names if they are not public, client names, project code names, and dollar figures with placeholders.
3. **Ask for structure.** Do not just say “summarize.” Ask for decisions, owners, and due dates explicitly.
4. **Assign owners.** Every action item should have a person and (ideally) a date.
5. **Send it out.** Share the cleaned summary with attendees so everyone agrees on what happened.

## Prompt templates for meetings

**Basic meeting summary:**
```
Summarize these meeting notes into:
- Decisions made (what was decided)
- Action items (who does what, by when)
- Open questions / next steps

Keep it short and skimmable. Plain English.

[PASTE MEETING NOTES]
```

**Action-item focused:**
```
Extract every action item from these notes. For each, list: task, owner, due date, and priority (high/medium/low). If a date or owner is missing, mark it [TBD].

[PASTE MEETING NOTES]
```

**Executive brief (for leadership):**
```
Write a one-paragraph executive summary of this meeting: the goal, the top 2-3 decisions, and the single most important next step. Professional tone, under 150 words.

[PASTE MEETING NOTES]
```

## Safety note for meetings

Meeting notes often contain client names, unreleased product details, salaries, or health information. **Sanitize before you paste.** If you work in healthcare, HR, or law, prefer a local LLM so nothing leaves your machine.

> **Credit:** Asdale Dynamics, LLC. Copyright (c) 2026 Asdale Dynamics, LLC. MIT License.
