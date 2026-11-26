---
name: sdd-product-requirements
description: Elicit product requirements for Spec-Driven Development (SDD), with scope, rules, acceptance criteria, priorities and traceability. Use when turning an idea or problem into a specification that Designer and Dev can execute without guessing intent.
example-prompt: Turn this idea into an SDD requirements spec, with scope and acceptance criteria for the team.
---

# Product requirements in SDD

Outcome: a clear, prioritized and verifiable product specification. The PM answers **why, for whom and what**; it does not define the visual solution or the technical implementation.

## 1. Establish the initiative contract

For blog projects, create `~/OpenBot/Shared/blog-tech-ia-content/specs/<slug>/01-requirements.md`. In other projects, use the existing specs folder.

Before writing:
- read the roadmap, the user request, related documents and the real state of the product;
- identify the problem and the expected result, without starting from a preferred solution;
- separate observed facts, decisions already made, assumptions and open questions;
- do not invent research, metrics, user needs or approvals.

## 2. Gather context and scope

Document concisely:
1. problem, audience and context of use;
2. goal and success indicator, or the required source when the metric is unavailable;
3. main scenarios and known edge cases;
4. constraints on deadline, budget, technology, content, privacy or operations;
5. dependencies, risks and what is explicitly out of scope.

Distinguish "required in this delivery" from "possible later evolution". Do not turn every idea into a requirement.

## 3. Write testable requirements

Use stable identifiers:
- `REQ-###` for functional behavior or capability;
- `NFR-###` for performance, accessibility, security, compatibility and other qualities;
- `AC-###` for acceptance criteria.

Each requirement must contain:
- a single, unambiguous statement;
- a reason or value linked to the goal;
- priority: essential, important or later;
- origin: request, evidence or decision;
- associated acceptance criteria;
- dependencies and uncertainties, when they exist.

Write "the user can…" or "the system must…" with observable behavior. Avoid "fast", "intuitive", "modern" or "robust" without a measure or verification condition.

## 4. Define acceptance and scenarios

For each essential requirement:
- specify precondition, action and observable result;
- use Given/When/Then when that improves precision;
- include success, error, empty, permission and limits when applicable;
- state which evidence proves acceptance: executed flow, content, API response, build, preview or another artifact.

Do not write acceptance that merely repeats the requirement. A criterion must let another person decide objectively between pass and fail.

## 5. Prepare the handoff

Deliver to the Product Designer and the Dev:
- the path of `01-requirements.md`;
- the version or date of the spec;
- the essential requirements of the cycle;
- decisions and open questions;
- dependencies between UX and technology.

The Designer details the experience in `02-experience.md`; the Dev records approach and tasks in `03-technical-plan.md`. Do not duplicate those sections in the product spec.

## 6. Control changes

- Keep requirement IDs; do not renumber to fill gaps.
- Record a requirement change, the reason, the date and the impact on the criteria.
- A relevant change of goal or scope follows the approval defined in AGENTS.md.
- Designer or Dev may flag ambiguity and infeasibility, but must not silently change intent or acceptance.

## Check

The spec is ready only when:
- every essential requirement has a priority and verifiable acceptance;
- scope and exclusions are explicit;
- assumptions and open questions are not disguised as facts;
- no visual or technical solution is imposed without need;
- Designer and Dev receive the path, version and exact slice of work.
