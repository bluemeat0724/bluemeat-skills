---
name: review-commit-push
description: Review repository changes, commit them by functional unit, and push each unit separately.
disable-model-invocation: true
---

# Review, Commit, Push

Audit the complete change, then ship it as the smallest sequence of coherent functional units. A functional unit is one independently understandable behavior change together with its tests and required documentation or configuration. Push each completed unit before preparing the next one. If the change contains only one real unit, make one commit and one push; preserve cohesion instead of manufacturing batches.

Invoking this skill authorizes ordinary commits and non-force pushes of the in-scope changes to the current branch. Ask before choosing another branch or remote, rewriting history, including changes whose ownership is uncertain, or expanding the requested behavior. Prefer built-in user-input tools exposed by the current agent runtime — e.g., `request_user_input`, `ask_user_question`, `ask_user`, or `AskUserQuestion`.

## 1. Establish scope

Read repository instructions. Inspect the current branch, upstream, remotes, status, recent commit-message convention, staged and unstaged diffs, relevant untracked files, and commits ahead of upstream. Detect merge/rebase conflicts, detached HEAD, missing upstream, or unrelated user work before changing the index.

Treat every pre-existing modification as user-owned. Infer the intended scope from the request and repository evidence; ask only when ownership, destination, or behavior cannot be inferred safely. Keep unrelated changes unstaged and untouched.

**Complete when:** every changed and unpushed item is classified as in scope, unrelated, or awaiting an explicit user decision, and the destination branch and remote are known.

## 2. Review the change

Read every in-scope diff and trace each affected flow through callers, tests, contracts, persisted data, and trust boundaries. Review for correctness, regressions, security, data loss, accidental API changes, missing error handling, and accidental secrets, generated files, binaries, or debug output. Run the smallest existing checks that cover the changed behavior; do not install tooling only for this run.

Fix clear in-scope defects at their root and review the resulting diff again. Stop before committing when a safe fix requires a product decision or scope expansion. Report the blocking finding with file and line evidence.

**Complete when:** every in-scope line has been reviewed, relevant checks have passed or their unavailable/failing state is understood, and no unresolved blocking finding remains.

## 3. Build the batch plan

Partition the reviewed change by functional unit and dependency order. Keep implementation, tests, migrations, and required docs for one behavior together. Split mixed files by hunk when needed. Each commit should leave the repository in a valid state and explain one outcome; use the repository's existing commit-message convention.

Existing unpushed commits remain in order. Group only contiguous commits into functional push boundaries; preserve published and user-authored history. Present the planned batches briefly before execution.

**Complete when:** every in-scope change belongs to exactly one ordered batch and each boundary names its behavior and verification.

## 4. Commit and push one batch at a time

For each batch, finish this loop before staging the next:

1. Stage only its exact paths or hunks; avoid broad staging commands when unrelated changes exist.
2. Inspect the staged diff, run `git diff --cached --check`, and rerun the smallest relevant check if staging changed the tested composition.
3. Commit with a concise outcome-focused message, then inspect the committed name/status and diff.
4. Push that boundary immediately with a normal fast-forward push. Set upstream only when the current branch's destination is unambiguous. For already-existing unpushed commits, advance the remote branch to each planned boundary in order rather than pushing all boundaries at once.
5. Confirm the remote accepted the update, then continue to the next batch.

Preserve remote history with fast-forward updates. If a later problem is found after a batch was pushed, add a corrective commit and push it as the next batch. Keep hooks enabled and surface failures instead of bypassing them.

**Complete when:** every planned batch has one verified commit boundary, each boundary was pushed in order, and no later batch entered the index before the prior push succeeded.

## 5. Verify and report

Inspect final status and the local/remote relationship. Confirm unrelated changes remain intact and no intended commit is still ahead of the remote.

Report each batch's functional purpose, commit hash, push result, and checks run. Then list remaining unrelated changes, skipped checks, or follow-up risks; omit empty sections.

**Complete when:** the user can match every functional unit to a pushed commit and the final repository state is explicit.
