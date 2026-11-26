---
name: sdd-ux-specification
description: Turn SDD requirements into implementable UI/UX specifications with flows, states, responsiveness, accessibility and traceable criteria. Use when the Product Designer must specify or review an experience defined by requirements.
example-prompt: Read the SDD requirements and produce the complete experience spec for the Dev to implement.
---

# Experience specification in SDD

Outcome: a UI/UX spec that covers the approved requirements and lets someone implement and review it without guessing behavior. The Designer answers **how the experience works and appears**; it does not change requirements or implement code.

## 1. Validate the input

Read `01-requirements.md`, the design system, related specs and the current experience. Check:
- requirements and criteria for the slice;
- users, context, constraints and exclusions;
- product questions separated from UX decisions;
- existing components and tokens.

If intent, audience or product acceptance is missing, return the concrete point to the PM. If it is a visual or interaction decision within scope, choose the simplest alternative consistent with the design system and record the reason.

## 2. Produce the experience spec

For blog projects, create `~/OpenBot/Shared/blog-tech-ia-content/specs/<slug>/02-experience.md`.

Include only what is needed to implement:
1. goal of the experience and requirements covered;
2. main flow, inputs, outputs and decisions;
3. information architecture, hierarchy and content;
4. reused or proposed components and tokens;
5. behavior per viewport and orientation when relevant;
6. loading, empty, error, success, focus, hover and disabled states when applicable;
7. keyboard navigation, screen readers, contrast, zoom and touch targets;
8. perceived performance, visual stability and a no-JavaScript fallback when applicable;
9. UX acceptance criteria and how to verify them;
10. out of scope, decisions, assumptions and open questions.

Describe observable behavior, not just static appearance. Do not require a new component when an existing one fits.

## 3. Keep traceability

Create a lean matrix:

| Requirement | Flow/component | State or behavior | UX criterion | How to verify |
|---|---|---|---|---|

Every essential requirement with an impact on the experience must appear. A requirement with no interface can be marked "no visual impact", with a short justification.

Use UX acceptance IDs (`UX-###`) when they help the review, preserving the PM's `REQ-###`, `NFR-###` and `AC-###` references.

## 4. Deliver to the Dev

- Send the path of `02-experience.md`, the version/date and the requirements of the slice.
- Highlight decisions that affect structure, data, performance or compatibility.
- State which criteria require a preview, interaction, keyboard or a specific screen.
- Update the design system when a reusable pattern emerges; do not copy permanent rules into every spec.

## 5. Review the implementation

1. Get the real preview and the implemented version.
2. Compare each criterion with the spec and the matrix.
3. Test applicable flows, states, viewports and accessibility.
4. Record each divergence with requirement/criterion, location, expected, observed, evidence and priority.
5. Without a preview or enough evidence, mark it as not verified; never approve or reject by assumption.

A requirement divergence goes back to the PM; a visual or interaction divergence goes back to the Dev with an objective criterion.

## 6. Control changes

- Preserve IDs and record revisions that change behavior.
- Do not expand scope or change product intent during design.
- When a technical constraint makes the experience infeasible, propose an alternative and align with PM and Dev before changing acceptance.

## Check

The spec is ready when it covers the requirements of the slice, defines states and behavior, reuses the design system and contains verifiable criteria. The review is complete only with real evidence and traceability between requirement, experience and result.
