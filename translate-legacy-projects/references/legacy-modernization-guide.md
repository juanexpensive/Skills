# Legacy Modernization Guide

## Contents

1. What usually fails
2. Recommended agent roles
3. Validation ladder
4. Governance checklist
5. Practical heuristics

## 1. What usually fails

Legacy modernization work breaks when the agent:

- treats migration as a single prompt instead of a staged engineering process
- performs literal translation that preserves old control flow and global-state patterns
- invents or misuses destination APIs
- validates only syntax, not runtime behavior
- ignores environment setup, dependency drift, or data contracts
- spreads one insecure pattern across many files

Treat compilable but non-idiomatic output as a failure mode, not a near-win.

## 2. Recommended agent roles

For large or risky efforts, simulate these roles even if only one Codex instance is working:

- `planning agent`
  Inventory the system, identify seams, map dependencies, and define the next safe slice.
- `translation agent`
  Produce the first pass for the selected slice using target-language idioms.
- `api grounding agent`
  Reconcile generated code with approved libraries, internal helpers, and compiler feedback.
- `environment agent`
  Build the target environment, resolve dependency issues, and surface reproducible errors.
- `testsuite agent`
  Create or expand unit, integration, regression, and parity tests.
- `refinement agent`
  Iterate until the slice is installable, testable, runnable, and maintainable.

Do not let the translation step absorb all responsibilities. That is how hidden failures slip through.

## 3. Validation ladder

Use this maturity ladder for every slice:

### Installability

- dependencies resolve
- builds start reliably
- generated code integrates with the workspace

### Testability

- unit and integration tests execute
- fixtures are stable
- parity checks can compare legacy and translated behavior

### Runnability

- services or batch jobs start
- external integrations behave as expected
- critical workflows match legacy outputs closely enough for the agreed tolerance

If a slice fails at a lower rung, drop back and fix that layer before pushing upward.

## 4. Governance checklist

Check these before calling a migration slice done:

- approved frameworks and libraries only
- no deprecated crypto or unsafe SQL patterns
- no accidental data exfiltration to public tooling
- no unexplained license or provenance risks
- human review trail captured for sensitive changes
- security-sensitive paths tested explicitly
- architecture changes acknowledged instead of hidden inside "translation"

## 5. Practical heuristics

- Prefer strangler-style replacement over big-bang rewrites.
- Prefer golden-master or differential testing when legacy tests are weak.
- Prefer translating the smallest behaviorally meaningful unit first.
- Prefer reusing organization-approved abstractions instead of generating new infrastructure.
- Prefer explicit notes on known mismatches, preserved quirks, and deferred cleanup.
- Prefer ending each session with one validated increment and a clear next step.
