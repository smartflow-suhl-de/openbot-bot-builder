---
name: sdd-technical-delivery
description: Plan, implement and validate software with Spec-Driven Development (SDD), linking requirements, UX specs, technical tasks, code and evidence. Use when the Dev receives a specified initiative or must assess whether a delivery meets the spec.
example-prompt: Implement this SDD spec with a technical plan, traceability and end-to-end validation.
---

# Technical delivery in SDD

Outcome: the smallest implementation that meets the specified requirements and experience, with reproducible evidence. The Dev answers **how to build and prove it**; it does not silently redefine product or UX.

## 1. Read and delimit

Read `01-requirements.md`, `02-experience.md` when present, related documents and the affected code. Before editing:
- identify the version/date of the specs and the authorized slice;
- extract requirements, rules, criteria and states;
- verify current behavior and reproduce bugs when applicable;
- list files, data, APIs, dependencies and risks;
- separate product, UX and technology questions.

An ambiguity of intent or acceptance goes back to the PM; a visual or interaction ambiguity goes to the Designer. A strictly technical decision can be made with the simplest option and an explicit assumption.

## 2. Write the technical plan

For blog projects, create `~/OpenBot/Shared/blog-tech-ia-content/specs/<slug>/03-technical-plan.md`.

Include:
1. chosen architecture and approach, with alternatives only when they affect the decision;
2. affected files/components/services;
3. data contracts, APIs, states and integrations;
4. applicable compatibility, security, privacy, performance and accessibility;
5. migration, feature flag or rollback when there is risk;
6. small, ordered tasks;
7. validation strategy and expected evidence;
8. assumptions, blockers and what will not be done.

Do not add a dependency, abstraction or infrastructure without a demonstrated need. Confirm the project's real tools and scripts before using them.

## 3. Create traceability

Keep a matrix in the plan and update it on delivery:

| Requirement/criterion | Task or change | Validation | Evidence | Status |
|---|---|---|---|---|

Every essential requirement of the slice must end up covered, blocked with a reason, or explicitly out of the delivery. No item may disappear between spec and implementation.

## 4. Implement in verifiable slices

- Make the smallest change consistent with existing patterns.
- Implement one functional slice at a time, preserving behavior outside the scope.
- Do not create new requirements from technical preferences.
- Do not change a criterion to fit the result to the code.
- Review the diff and remove accidental changes.
- If a gap in the spec appears, record it and forward it to the owner before assuming a relevant change.

## 5. Validate real behavior

Run the applicable checks:
1. build and static checks of the project;
2. existing tests related to the change, without presuming a framework or creating unrequested infrastructure;
3. preview and full flow, not just opening the page;
4. success, error, empty, limits and permissions as specified;
5. desktop, mobile, keyboard, focus, contrast and visual stability when there is UI;
6. real API calls, persistence or integration when they are part of acceptance;
7. regression of the affected areas.

For each failure: reproduce, locate the cause, fix and repeat the check. An approved build does not replace evidence of behavior.

## 6. Record the delivery

Create or update `04-validation.md` in the same folder as the spec with:
- version of the code and of the specs used;
- commands and flows executed;
- observed results and evidence;
- updated traceability matrix;
- unverified items, remaining defects and limitations;
- rollback instructions when relevant.

Give the PM the status of the requirements and the Designer the UX points for review. Publication and deploy follow the approvals in AGENTS.md; after an authorized action, also verify the published environment.

## Check

Do not declare done while an essential requirement lacks evidence, a criterion is failing, or a relevant validation has not been run. State precisely what was implemented, what was proven and what remains pending.
