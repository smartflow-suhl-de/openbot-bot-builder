# Professional competence

> Derived from the `bot-architect` skill in this repo on 2026-11-26. This is a
> reconstruction, not the author's original file. Treat the criteria as a
> starting point and adjust them to the profession you are auditing.

Read this before every audit or creation. The goal is to judge a bot against
the **real profession**, not against the bot's own instructions. A bot can
follow its instructions perfectly and still be bad at the job.

## 1. Define the role before judging it

Write down, in five lines:

- **Role name** as the profession calls it, not as the bot calls itself.
- **One job**: the single outcome this role owns. If you need "and" to describe
  it, it is probably two roles.
- **Deliverables**: what the role hands over, in what format, to whom.
- **Stakeholders**: who consumes the deliverable and what they do with it.
- **Standard of excellence**: what a good deliverable looks like, named by a
  property (complete, sourced, reproducible), not by an adjective (great,
  professional).

If a line cannot be filled from a source, mark it **[assumption]** and confirm
with the user before scoring.

## 2. Sources, in this order

1. **The user's own material**: job description, existing deliverables, style
   guide, feedback from past work, contracts.
2. **Professional bodies and standards**: associations, certification bodies,
   published codes of practice for the field.
3. **Occupational databases**: O*NET (<https://www.onetonline.org>) and ESCO
   (<https://esco.ec.europa.eu>) for tasks, skills and responsibilities.
4. **Hiring material**: 5–10 current job ads for the same role, used only for
   recurring tasks and expectations, never for a single company's quirks.
5. **Practitioner writing**: books, postmortems, portfolios, conference talks.

Record source, date and what it supports. A source older than three years is
flagged when the field moves fast (software, marketing, regulation).

## 3. Competency matrix

For the role, list 5–10 competencies. For each:

| Competency | What good looks like | Evidence in a deliverable | Weight |
|---|---|---|---|

Weights: **core** (the role fails without it), **important** (visible quality
gap), **nice** (differentiator). Score only core and important for the audit
verdict.

Examples of competencies by family:

- **Engineering**: correctness, tests and evidence, review quality, incident
  response, security defaults, technical writing.
- **Content**: accuracy and sourcing, structure, voice match, SEO/search
  intent, editing discipline.
- **Operations/support**: triage, policy compliance, escalation judgement,
  customer tone, record keeping.
- **Product/design**: problem framing, scope discipline, acceptance criteria,
  UX states, accessibility, handoff completeness.

## 4. Judge the bot against the role

For each competency, ask three questions:

1. **Does the instruction require it?** Look for a rule, a checklist or a
   skill step, not a vague aspiration.
2. **Can the bot do it with its tools?** A rule without the file access, API
   or shell command is a wish.
3. **Is there evidence it happened?** Look at real deliverables, tables,
   commits, previews. A self-report is not evidence.

Score each competency 0–2:

- **0 — absent**: no rule, no tool, no evidence.
- **1 — claimed**: rule exists, evidence missing or unverified.
- **2 — demonstrated**: rule exists, tool exists, a real deliverable proves it.

## 5. Common failure patterns

- **Instruction theatre**: long instructions that restate the platform
  (approvals, secrets, browser) and say nothing about the actual work.
- **Competence by adjective**: "world-class", "expert" with no deliverable
  criteria.
- **Tool gap**: the bot is told to verify a preview but has no browser access.
- **Report gap**: the bot is told to deliver evidence but returns prose.
- **Role creep**: one bot owns three jobs, so none is done well.
- **Frozen knowledge**: the profession changed, the instructions did not.

## 6. Output of this step

A short section in the audit with:

- role definition and sources (with dates);
- the competency matrix and weights;
- per-competency score with the evidence that supports it;
- what could not be judged, and what evidence would settle it.

Keep configuration scoring separate. A bot can score high on configuration and
low here, and that is the finding worth reporting.
