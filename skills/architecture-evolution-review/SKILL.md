---
name: architecture-evolution-review
description: Periodically assess and optimize an organically grown or vibe-coded repository as a whole. Use when the user wants a full-codebase architecture review, architecture-drift cleanup, systemic optimization, a simpler target architecture, or a broad refactoring report beyond the current feature or diff.
disable-model-invocation: true
---

# Whole-Codebase Architecture Optimization

Periodically step outside feature-level work and optimize the repository as one system. Detect architecture drift caused by organic growth, early assumptions, and agents solving local features without seeing the whole. Produce one evidence-backed target and an optimization portfolio ranging from deletion and consolidation to a fundamental redesign. Preserve code because it is sound, never because it already exists.

This skill reports only—it may create the requested report, but changes no application code, tests, configuration, or dependencies.

## Defaults

- Scope: the whole repository, excluding dependencies, generated output, caches, binaries, and vendored code unless they define an architectural constraint.
- Output: `.architecture/architecture-optimization-<project>-<YYYY-MM-DD-HHmm>.md`, written in the user's language. Use stdout or another path when requested.
- Review log: `.architecture/optimization-log.md`. The first verified run creates it; later runs validate and reuse it to avoid rereading unchanged code.
- Evidence: repository contents first; Git history and runnable project checks when available. Do not install tools or dependencies just for the review.
- Internal compatibility: existing modules, internal APIs, abstractions, file layout, and implementation-shaped tests impose no constraint. Prefer the clean target over adapters that preserve old code.
- External impact: inventory public APIs, persisted data, user-visible behavior, and deployment interfaces. They are impact boundaries, not automatic vetoes; a breaking recommendation must name its benefit, blast radius, migration, verification, and rollback.

Ask only when the repository, scope, or required output cannot be inferred safely. Record other uncertainty in the report instead of stalling.

## Repeated-Run Log

The log is a **validated index**, not evidence by authority. Code wins whenever it disagrees with the log. Never reduce confidence or coverage claims merely to keep an incremental run small.

### Choose the scan mode

Start every run by listing first-party files and reading repository instructions, manifests, and the log when present. Validate the logged repository identity and baseline commit, then inspect changes since that baseline, including staged, unstaged, untracked, renamed, and deleted paths. A previously dirty path remains stale until inspected again.

Run a full scan when any condition holds:

- the log is missing, malformed, belongs to another repository, or its baseline cannot be reached;
- the user requests a full scan or prior coverage is Low/Unknown in a core area;
- four incremental runs have occurred since the last full scan;
- changed first-party files reach the smaller of 20% of first-party files (rounded up) or 200 files;
- entry points, manifests, package/feature boundaries, composition roots, persistence schemas, public contracts, or deployment topology changed enough to invalidate the system map.

Otherwise run an incremental scan over:

- every changed or previously dirty path;
- its direct first-party imports and importers, expanding transitively when ownership or dependency direction may change;
- each affected core flow, contract, state owner, and cross-cutting concern;
- one unchanged sibling implementation for every changed feature pattern;
- every open finding whose evidence or invalidation trigger intersects the change set.

The review still reasons about the whole system through the validated map. Label reused evidence separately from freshly inspected evidence in the report.

### Log contract

Keep the log terse and structural. It contains these sections:

1. **Baseline** — repository identity, HEAD, dirty paths, date, full/incremental mode, last full-scan commit/date, incremental count, report path, and coverage confidence.
2. **System map** — entry points, modules/responsibilities, dependency direction, core flows, state owners, and external systems.
3. **Target and invariants** — current recommended target plus the few dependency, ownership, and contract rules future work must preserve.
4. **Coverage ledger** — one row per first-party area with last inspected commit/date, evidence source, confidence, and invalidation triggers.
5. **Finding ledger** — stable ID, status (`Open`, `Accepted`, `Resolved`, `Superseded`), affected scope, evidence paths, first/last seen, and target action. Detailed reasoning stays in the linked report.
6. **Invalidation watchlist** — assumptions and the files/events that make them stale.
7. **Run history** — the latest 10 runs: date, baseline, mode, fresh scope, reused scope, findings opened/resolved, and report path.

Rewrite canonical sections instead of appending duplicates. Keep open findings and findings resolved since the last full scan; older detail remains in linked reports. Remove renamed/deleted paths and superseded assumptions. Never store code bodies, environment values, credentials, or secret-derived data.

Update the log only after the report passes its verification. An interrupted run leaves the previous verified baseline intact.

## Architectural Lens

Optimize for safe, local change:

- **Whole-system coherence over local convenience.** Compare sibling features and cross-cutting concerns; a locally tidy feature can still deepen repository-wide drift.
- **Readability over reuse.** Prefer direct code and small, cohesive modules. Accept clear duplication when sharing would couple distinct concepts.
- **Business capability over technical layers.** Prefer vertical modules that can be understood and changed together; keep a small shared kernel only for genuinely stable, jointly owned concepts.
- **One owner, one source of truth.** State, invariants, and transitions need an explicit owner.
- **Explicit boundaries.** Dependencies, contracts, side effects, and failure behavior should be visible from module APIs.
- **Modular monolith by default.** Recommend services only when independent deployment, fault isolation, team autonomy, or materially different scaling is already required.
- **Concrete before abstract.** Introduce an abstraction when it removes demonstrated change friction, not because a second implementation is imaginable.
- **Change locality over formal purity.** A common change should not require ceremonial edits across unrelated layers.
- **Low rewrite cost, high evidence bar.** Vibe-coded implementation is cheap to replace, so recommend direct rewrites when they reduce total complexity. Runtime, data, security, and migration risks still require evidence and controls.

Security, data integrity, error handling that prevents loss, and trust-boundary validation remain hard constraints.

## Process

### 1. Establish current coverage

Apply the repeated-run protocol to choose full or incremental mode. Read the repository guidance, manifests, README and architecture documentation needed to validate the system map. Enumerate first-party source, tests, migrations, scripts, configuration, CI, and deployment files. Identify languages, frameworks, entry points, processes, packages, generated areas, and external systems.

Use fast repository-aware searches such as `rg --files` and `rg`. Respect repository instructions and avoid printing secrets.

When the inventory finds a first-party Python backend, read [`references/python-backend.md`](references/python-backend.md) completely and apply its evidence pass and target-architecture lens. Keep its evidence inside this skill's report contract rather than generating a separate checklist.

When the inventory finds a first-party React frontend, read [`references/react-frontend.md`](references/react-frontend.md) completely and apply its evidence pass and target-architecture lens. Keep its evidence inside this skill's report contract rather than generating a separate checklist.

**Complete when:** every in-scope top-level area is classified as freshly inspected, supported by a still-valid log entry, excluded with a reason, or unknown; every stale entry has expanded the fresh scan scope.

### 2. Reconstruct the current architecture

On a full scan, build the evidence ledger from code. On an incremental scan, verify logged evidence for affected areas and retrace stale paths while retaining explicitly labeled, still-valid evidence for unchanged areas:

- module responsibilities and internal dependency direction;
- every core user or system flow from entry point through state change and output;
- state, invariants, transactions, caches, and source-of-truth ownership;
- public APIs, persisted schemas, events, files, commands, and deployment contracts;
- cross-cutting behavior such as authentication, validation, errors, logging, configuration, and background work.
- competing patterns for the same responsibility across features;
- abandoned paths, temporary adapters, duplicated infrastructure, and abstractions left behind by earlier iterations.

Cite file paths and symbols. Distinguish observed facts from inferences. When static inspection cannot establish runtime behavior, mark the gap.

**Complete when:** every first-party module has a current owner/purpose and dependency context, every identified core flow has fresh or validated end-to-end evidence, and every shared mutable state or external contract has an owner or an explicit `unknown` entry.

### 3. Find system-wide optimization leverage

Compare sibling features and trace cross-cutting concerns across the whole repository. Identify recurring change types from product vocabulary, tests, issues or documentation, and Git history when available. Use co-change hotspots and repeated edits across boundaries as supporting evidence, not proof by themselves. If prior architecture reports exist, distinguish resolved findings, new drift, and regressions.

For each candidate problem, answer:

1. Which features, flows, or cross-cutting concerns exhibit the problem?
2. What realistic change is obstructed, and how often does it occur?
3. Which dependency, ownership ambiguity, duplicated convention, or indirection is the root cause?
4. What can be deleted, merged, moved, renamed, or rewritten to create one clear shape?
5. Would a broader redesign produce less total code and fewer concepts than preserving the current structure?

Run existing architecture checks, tests, builds, or type checks only when they are safe and relevant. Record commands and results.

**Complete when:** every first-party area has fresh or validated sibling/cross-cutting comparison, each recommendation has concrete evidence and affected scope, and unsupported intuitions are removed or labeled unknown.

### 4. Design one coherent optimization target

Recommend the warranted mix of retention, deletion, consolidation, boundary repair, and rewrite. Most reviews should yield concrete optimization without inventing a new architecture. When the current shape makes simplicity impossible, redesign it fundamentally. Internal modules and technology choices may change freely.

Briefly record only credible rejected alternatives and the evidence that makes them worse. Do not hand the decision back as a menu.

**Complete when:** the target follows from the evidence ledger, addresses every high-impact finding, removes competing patterns where one clear pattern suffices, and contains nothing solely for hypothetical reuse or scale.

### 5. Design the shortest safe execution

Map current modules and responsibilities to their target homes. Prefer direct replacement over parallel old/new architectures: internal compatibility is not a goal. Split work only where independent verification, deployability, data safety, or team coordination makes stages valuable. Each stage must state prerequisites, exact boundary moved, external impact, verification, rollback or safe stopping point, and what becomes deletable.

Prefer deletion, direct moves, and rewrites. Permit temporary adapters only for real external or operational constraints; name the stage that removes each adapter.

**Complete when:** every current responsibility is retained, moved, replaced, or explicitly deleted; every breaking change has a migration; every temporary structure has a removal stage.

### 6. Write, verify, and checkpoint

Use the report contract below. Check every claim against its cited evidence. Never expose secret values. State scan mode, fresh and reused evidence, coverage limits, and invalidated log entries plainly. Lower confidence when core flows, runtime behavior, or history were unavailable. After verification, update `.architecture/optimization-log.md` using the log contract.

**Complete when:** all required sections exist, every finding is reflected in the target or explicitly deferred, every execution stage is verifiable, the log points to this verified run, and both saved paths are returned to the user.

## Finding Contract

Include only findings that affect architectural change. Each finding contains:

- title and status: `Confirmed` or `Suspected`;
- change obstruction: `Blocking`, `High`, `Moderate`, or `Low`;
- frequency: `Frequent`, `Recurring`, `Rare`, or `Unknown`;
- confidence: `High`, `Medium`, or `Low`;
- evidence: file paths, symbols, dependency path or data flow, and observed behavior;
- realistic change scenario and present edit surface;
- root cause, not merely the visible symptom;
- recommended optimization, affected repository scope, expected readability/change-locality benefit, cost, and migration risk.

Do not assign an overall score or letter grade. Do not report generic best-practice violations without a demonstrated change consequence.

## Report Contract

Write these sections in order:

1. **Executive assessment** — overall architecture health, systemic drift themes, optimization direction, expected benefit, cost/risk, and confidence.
2. **Scope and evidence** — scan mode, baseline, fresh/reused areas, invalidated log entries, exclusions, commands, unavailable evidence, and coverage confidence.
3. **Current system model** — entry points, module/responsibility map, dependency direction, core flows, state owners, and external contracts.
4. **What should remain** — sound boundaries and implementation choices worth preserving.
5. **Optimization portfolio** — evidence-backed findings using the contract above, ordered by repository-wide leverage, change obstruction, then frequency.
6. **Recommended target architecture** — one target; module/directory draft, responsibility table, allowed dependency directions, state ownership, core data flows, and contract policy. Use a compact Mermaid diagram when it clarifies the shape.
7. **Current-to-target map** — every current responsibility mapped to retain, move, replace, or delete.
8. **Execution stages** — the shortest independently verifiable path to the target, with stopping points and temporary-adapter removal.
9. **Rejected alternatives** — only credible competitors and evidence-based rejection reasons.
10. **Drift prevention** — the few enforceable boundaries, checks, or ownership rules that prevent feature-focused work from recreating the same problems.
11. **Decision record** — assumptions, unresolved questions, and triggers that would justify revisiting the architecture.

Use small code or interface sketches only when a boundary cannot be explained precisely without one. Keep implementation code out of the report.
