# Safety & data hygiene — paste safely

This is the most important chapter. **AI summarization is useful, but you control what you paste.** Treat every prompt like a postcard, not a sealed letter — assume it could be seen by the service provider unless you are using a trusted local model you run yourself.

## Never paste

Never paste these into any AI tool (cloud or otherwise), even “just to test”:

- **IDs:** Social Security numbers, driver's license numbers, passport numbers, employee IDs, patient IDs, account numbers
- **Financial data:** credit card numbers, bank account numbers, routing numbers, tax IDs, pay stubs, invoices with amounts
- **Credentials:** passwords, API keys, secret tokens, sign-in codes
- **Private personal data:** home addresses, phone numbers, birthdays, medical diagnoses, medication lists
- **Other people's private data:** client lists, patient charts, employee records

If it would not belong on a public bulletin board, do not paste it into a cloud AI tool.

## Before you paste — sanitize

Replace real values with placeholders:

| Real value | Replace with |
|---|---|
| Patient name | `[PATIENT]` or `Patient A` |
| Account number | `[ACCOUNT #]` |
| Dollar amount | `[AMOUNT]` |
| Email address | `[EMAIL]` |
| Phone number | `[PHONE]` |
| Date of birth | `[DOB]` |
| Company/client name | `[CLIENT]` |

**Example — unsafe:**
> "Summarize this invoice from Acme Corp for patient John Doe, account 4488-9921, amount $1,240.00, dated 03/14/2026."

**Example — safe:**
> "Summarize this invoice from `[CLIENT]` for `[PATIENT]`, account `[ACCOUNT #]`, amount `[AMOUNT]`, dated `[DATE]`."

## Extra safety habits

- Use **local LLMs** (Ollama, LM Studio) for anything sensitive — nothing leaves your computer
- Turn off “train on my data” / history where the cloud tool offers it
- Do not paste credentials or secrets “just to see if the AI can fix them”
- When in doubt, **sanitize first, then paste**

## A note for healthcare workers

This handbook is **education only, never medical advice.** Do not paste real patient information. Use de-identified, fictional examples when practicing. AI summaries are not a substitute for clinical judgment.

> **Credit:** Asdale Dynamics, LLC. Copyright (c) 2026 Asdale Dynamics, LLC. MIT License.
