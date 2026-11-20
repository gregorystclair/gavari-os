# Architecture

One operator. Every function is a system with three parts: a **skill** (the
written procedure an agent follows), a **schedule** (when it runs without
being asked), and an **evidence trail** (the artifact that proves it ran).

```
                ┌────────────────────────────────────────────┐
                │              OPERATOR (human)              │
                │   approves sends · talks to partners ·     │
                │   handles exceptions · makes the calls     │
                └───────────────▲───────────────▲────────────┘
                                │ reports        │ approvals
        ┌───────────────────────┴───┐   ┌────────┴───────────────────┐
        │        SELF-AUDIT         │   │         DASHBOARDS         │
        │  morning_send_audit.py    │   │  what sent · who joined ·  │
        │  reads logs, flags misses │   │  who produced · what's due │
        └───────────────▲───────────┘   └────────▲───────────────────┘
                        │ logs                   │ reads
   ┌────────────┬───────┴──────┬──────────────┬──┴─────────────┐
   │   RADAR    │    AUDIT     │   OUTREACH   │   VOICE        │
   │  sourcing  │  engine Q&A  │  4 channels  │   AGENTS       │
   │  + scoring │  + reports   │  on schedule │   phone lines  │
   └────────────┴──────────────┴──────────────┴────────────────┘
                        │
              skills · connectors · MCP
              (the agent's hands)
```

## Data rules

- Prospect and client records live outside this repo, in the operating
  workspace. This repo holds *procedures and public-signal tooling only*.
- Every scored record carries an `evidence` field: the URL or artifact the
  score came from. A score without evidence is deleted, not debated.
- Send logs are append-only. The self-audit compares the log against the
  schedule; a gap is a same-day incident, not a statistic.
