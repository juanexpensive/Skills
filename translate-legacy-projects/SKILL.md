---
name: translate-legacy-projects
description: Plan and execute safe translation or modernization of legacy projects and codebases. Use when Codex needs to translate legacy code to another language or framework, migrate old services or monoliths incrementally, preserve behavior with parity checks, avoid literal non-idiomatic output, ground generated code against approved APIs, or manage security and compliance risks during legacy modernization. Triggers include requests such as "translate this legacy project", "migrate this old app", "modernize this monolith", "port COBOL/PLSQL/C++/Java/.NET code", or "traducir un proyecto legacy".
---

# Translate Legacy Projects

Use this skill to avoid treating legacy translation as a one-shot rewrite. Prefer small, validated modernization slices over literal file-by-file conversion.

## Quick Start

1. Decide whether the request is translation or migration.
2. Capture current behavior before editing code.
3. Slice the system into domains or seams.
4. Translate one slice with target-language idioms and approved APIs.
5. Run build, tests, and runtime parity checks in a loop.
6. Fix non-idiomatic output before expanding scope.

Read [references/legacy-modernization-guide.md](references/legacy-modernization-guide.md) when the task involves large systems, missing tests, environment setup problems, or compliance constraints.

## Workflow

### 1. Classify the job correctly

Treat it as translation when the main goal is semantic equivalence in a new language or framework.
Treat it as migration when the change also affects architecture, infrastructure, data stores, deployment, or team operating model.

Say this distinction out loud early because it changes scope, timeline, and validation.

### 2. Establish a behavioral baseline

Before translating code, recover what the legacy system actually does:

- inspect entrypoints, dependencies, config, and runtime assumptions
- gather existing tests, fixtures, telemetry, logs, and representative inputs and outputs
- document risky hidden behaviors such as global state, ordering dependencies, side effects, batch windows, and error handling conventions

If tests are weak, prioritize capturing golden inputs and outputs or differential test fixtures before large rewrites.

### 3. Decompose before converting

Avoid whole-monolith rewrites by default.
Prefer:

- bounded domains or subcomponents
- seams around APIs, jobs, files, or modules
- strangler-style replacement paths
- atomic sessions with narrow goals and clean checkpoints

For large work, propose 2-4 concrete slice options instead of asking open-ended scoping questions.

### 4. Translate with grounding

Do not translate line by line unless the user explicitly wants a mechanical port.
Prefer:

- target-language idioms
- approved internal or framework APIs
- explicit type and data-model mapping
- architecture-aligned abstractions instead of copied procedural flow

Watch for "JOBOL"-style output: syntactically valid code that preserves legacy structure so literally that the new code becomes unmaintainable.

### 5. Keep the environment in the loop

Treat compilation and execution feedback as part of the translation process, not as a final check.
Progress through this validation ladder:

1. installability
2. testability
3. runnability

Use compiler errors, dependency resolution failures, test regressions, and runtime mismatches as first-class inputs for the next iteration.

### 6. Validate behavior, not just syntax

Require evidence beyond "it compiles".
Prefer:

- differential tests against the legacy system
- snapshot or golden-master comparisons
- integration tests around external systems
- performance checks for sensitive paths
- manual review of security-sensitive and money-moving flows

Do not declare success from textual similarity.

### 7. Govern risk explicitly

Assume AI-generated migration code may replicate insecure patterns at scale.
Check for:

- unsafe SQL construction
- deprecated crypto
- broken auth or path handling
- license contamination risk
- exposure of proprietary code or regulated data to external models
- missing human review records for ownership and compliance

### 8. Close each slice cleanly

Finish each slice with:

- passing validation for that slice
- a short note on residual risk
- the next smallest safe increment

Reset context between large slices when possible to reduce instruction drift.

## Good Defaults

- Prefer small, reversible changes.
- Prefer parity harnesses before deep refactors.
- Prefer refactoring the translated output into idiomatic target code before scaling it out.
- Prefer organization-approved libraries and patterns over generated novelty.
- Prefer explicit assumptions over silent guessing.

## Ask the User Only When It Changes the Plan

Escalate when one of these is unclear and materially changes the work:

- target language or platform
- acceptable degree of redesign versus strict equivalence
- access to the legacy runtime for parity testing
- regulated or proprietary data constraints
- whether to preserve bugs that downstream systems depend on

When asking, offer concrete options and recommend one.

## Example Triggers

- "Translate this legacy project from C++ to Rust."
- "Migrate this old Java 8 service to Java 21 without breaking behavior."
- "Modernize this COBOL batch flow into maintainable Java services."
- "Port this PL/SQL package to a Spring service."
- "Traducir este proyecto legacy."
- "Migrar este monolito poco a poco con pruebas de paridad."
