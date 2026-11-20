# Skill: AI Visibility Audit

**Purpose.** Produce a finished audit for one business: what the major AI
engines say about it when a customer asks, whether its front door actually
responds, and what to fix first. Deliverables are a narrated video report
and a PDF. Target: minutes, not days.

## Rules that do not bend

1. **Ask the engines. Never search.** Engine answers come from ChatGPT,
   Perplexity, and Gemini in their own interfaces, asked the way a customer
   asks ("best [trade] in [city]"). Search results are not engine answers.
2. **Evidence is a build gate.** The audit does not ship until the raw
   engine answers are filed in the run folder (`evidence/engine-answers.json`)
   — verbatim, with the question, engine, and timestamp for each.
3. **Test the front door for real.** Submit the business's actual contact
   form / call the actual number. Record response time from the test, not
   from the business's claims about itself.
4. **Cross-reference the business.** Website + Facebook + Instagram +
   third-party mentions before writing a single finding. Watch for name
   collisions with same-named businesses in other states.

## Procedure

1. Intake: business name, trade, city, website, phone. Confirm the listing
   identity (address + phone) against the live Google listing.
2. Engine pass: ask each engine the buyer questions for that trade and
   city. File every answer verbatim in the evidence folder.
3. Front-door test: submit/call, start a stopwatch, log first real human
   or system response time.
4. Findings: name the cause of each leak, with the measured number
   attached. No finding ships without a measurement or a filed answer
   behind it.
5. Build: narrated video (findings) + PDF (findings + improvement steps).
   Verify the narration by transcribing the final audio and diffing it
   against the script before delivery.
6. Deliver and log: link sent, timestamp, evidence folder path.

## Output contract

- `evidence/engine-answers.json` — verbatim answers, per engine
- `report.mp4` — narrated findings video, transcription-verified
- `report.pdf` — findings + prioritized fixes
- Run log line: business, started, delivered, elapsed
