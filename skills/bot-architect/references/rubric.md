# Configuration rubric

> Derived from the `bot-architect` skill in this repo on 2026-11-26. This is a
> reconstruction, not the author's original file. The author's rubric may score
> differently; record which version you used in `bot_audits`.

Read when scoring. This rubric measures **configuration only** — how well the
bot is built. It does **not** measure professional competence; that is a
separate axis (see `professional-competence.md`) and must be scored and
reported separately.

## Scale

Each of the 10 criteria is scored **1, 3 or 5**:

- **1 — missing or harmful.** The criterion is absent, contradicts itself, or
  actively causes bad work.
- **3 — present but weak.** It exists, but is vague, duplicated, untested or
  not backed by the tools.
- **5 — present, specific and proven.** A reviewer can check it, the tools
  support it, and a real deliverable shows it working.

No half points. When the evidence is missing, score 3 at most and name the
missing evidence.

## The 10 criteria

### 1. Role and one job
- **1:** no stated role, or three jobs in one bot.
- **3:** a role is named, but the job is broad ("help with marketing").
- **5:** one outcome, one owner, explicit handoffs for everything else.
- **Evidence:** profile + `AGENTS.md` first section; deliverables that match.

### 2. Profile and naming
- **1:** title missing, over 120 characters, or project-prefixed name that
  hides the function.
- **3:** name and title exist but are generic ("Assistant").
- **5:** function-based name, title ≤ 120 characters, description ≤ 2,000
  characters that states job, inputs and output.
- **Evidence:** `openbot.read_agent` profile.

### 3. Instruction quality
- **1:** prose, contradictions, or rules the bot cannot act on.
- **3:** rules exist but mix policy with background and repeat platform rules.
- **5:** imperative rules with trigger, action, output contract and boundary;
  no duplication of platform defaults.
- **Evidence:** `AGENTS.md` and the profile; count of rules a reviewer can test.

### 4. Knowledge placement
- **1:** everything in the profile, or procedures only in memory.
- **3:** skills exist but overlap, or references are missing.
- **5:** profile short, procedures in skills, background in references, facts
  in memory, no copied procedure in two places.
- **Evidence:** file tree, skill frontmatter, memory list.

### 5. Tool and access fit
- **1:** the instructions require tools the bot does not have, or the bot has
  far more access than the job needs.
- **3:** access exists but is broader than needed, or one required tool is
  missing.
- **5:** every required step has a tool; access is minimal and read-only where
  the stage is read-only.
- **Evidence:** MCP list, permissions, a step-by-step mapping of rules to tools.

### 6. Model and fallback
- **1:** no model reasoning, or a model that cannot do the task.
- **3:** a model is set but no backup and no fit rationale.
- **5:** model and reasoning effort match the stage, a backup exists, IDs are
  validated against the live catalog.
- **Evidence:** profile settings, catalog check.

### 7. Routines
- **1:** routines run by default with no no-update rule, or duplicate work.
- **3:** routines exist but are unpaused without an owner, or lack a quiet
  path.
- **5:** paused by default, each with a schedule, a timezone, a scope and a
  `routine_no_update` rule for "nothing changed".
- **Evidence:** routine list, schedule, instruction text.

### 8. Approvals and safety
- **1:** the bot can merge, deploy, send or spend without approval, or secrets
  are handled loosely.
- **3:** approvals are mentioned but vague ("ask if unsure").
- **5:** named irreversible actions, explicit written approval by the owner,
  secrets out of code and logs, least privilege.
- **Evidence:** `AGENTS.md` boundaries, permission settings, sample runs.

### 9. Delegation and handoffs
- **1:** no handoff contract, or the bot silently passes work on.
- **3:** handoffs are named but lack input, output or evidence rules.
- **5:** each handoff has owner, input, output, done criterion and evidence;
  delegated results are verified, not trusted.
- **Evidence:** handoff sections, channel messages, a delegated run.

### 10. Verification and evidence loop
- **1:** "done" is claimed without an artifact; no tests.
- **3:** tests exist but are synthetic or not repeated after changes.
- **5:** before/after tests on real deliverables, artifacts cited, failures
  recorded in `bot_audits`, untested parts declared.
- **Evidence:** test log, table rows, diff/preview/exit codes.

## Scoring sheet

| # | Criterion | Score (1/3/5) | Evidence | Missing |
|---|---|---|---|---|
| 1 | Role and one job | | | |
| 2 | Profile and naming | | | |
| 3 | Instruction quality | | | |
| 4 | Knowledge placement | | | |
| 5 | Tool and access fit | | | |
| 6 | Model and fallback | | | |
| 7 | Routines | | | |
| 8 | Approvals and safety | | | |
| 9 | Delegation and handoffs | | | |
| 10 | Verification and evidence loop | | | |

**Configuration total: __ / 50.**

Bands: **10–24** rebuild the setup, **25–39** targeted fixes, **40–50**
refinements only.

## Rules for using it

- Score the configuration, then score competence separately. Never average
  them into one number.
- Every score names its evidence. "Looks good" is not evidence.
- When a criterion cannot be judged, write "not verifiable" and what would
  settle it; do not guess a 3.
- Record the rubric version and date in `bot_audits` so later audits are
  comparable.
