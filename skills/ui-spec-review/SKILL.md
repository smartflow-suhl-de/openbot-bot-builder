---
name: ui-spec-review
description: Write implementable UI/UX specifications and review how faithfully the implementation matches them. Use to specify pages, components or flows and to compare a preview with a spec.
example-prompt: Create a mobile spec with acceptance criteria and then review the implementation.
---

# UI spec and review

Outcome: visual and interaction decisions that another agent can implement and verify without guessing.

## 1. Understand before designing
- Read the problem, the audience and the technical constraint.
- Inspect the current experience when a preview or code is available.
- Consult the design system and reuse tokens and components before creating new ones.

## 2. Write the spec
Include only what the task needs:
1. problem, goal and what is out of scope;
2. key decisions and rationale;
3. structure, components, tokens and content;
4. states: empty, loading, error, success, focus and disabled when applicable;
5. mobile, tablet and desktop behavior;
6. keyboard, screen reader, contrast and target size;
7. performance and visual stability when relevant;
8. observable acceptance criteria and how to test them.

Do not turn aesthetic preference into a rule without explaining the decision. Do not implement code.

## 3. Review the implementation
1. Compare the real preview with each spec criterion.
2. Test interactions and relevant screen sizes.
3. List divergences by impact: blocks use, harms comprehension, or refinement.
4. For each divergence, state location, expected, observed and evidence.
5. Without a preview, state the limitation and what needs inspection; never invent the visual result.

## 4. Handoff
Give the Dev the spec path and the acceptance criteria. If a reusable component or token emerges, update the design system instead of duplicating rules in the spec.

## Check
The spec covers behavior and acceptance; the review cites real evidence; every divergence has a priority and a clear action.
