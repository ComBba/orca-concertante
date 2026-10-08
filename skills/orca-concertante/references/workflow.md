# Goal-to-completion workflow

## Establish the goal

The user provides the outcome, not a required task template. Internally record:

- Goal and observable acceptance criteria.
- Project rules, authorized effects, and any excluded scope.
- Source base, current changes, current coordinator, and intended editors.
- Next bounded task and its evidence consumer.

Preserve unrelated work. Independent implementations use separate worktrees or non-overlapping files. A shared mutable directory or external system still needs explicit ownership; worktree separation alone does not isolate it.

## Use Orca's current coordination contract

For supervised work, follow the installed orchestration guide: confirm runtime, bind a Run, start ready independent tasks, consume messages, validate settlements, then acknowledge deliveries. Task specs contain target, change, constraints, ownership, and observable acceptance. Use `worker-start` unless the installed guide identifies a genuine expressiveness gap.

The Run is a namespace and inbox, not an autonomous scheduler. The current coordinator must remain responsible for progress. Worker questions about routine implementation go to the coordinator, not the user. Escalate only missing user authority, unavailable user-only authentication, or a material goal/policy decision; continue independent tasks meanwhile.

Input acceptance, turn start, settlement, and goal completion are separate facts. Use exact current dispatch identities. Read every delivered question/failure before acknowledging. Once Orca accepts settlement, reuse the proven terminal for immediate follow-up or release it through the official contract. Do not close unrelated user terminals.

A simple transfer without supervision uses the installed CLI handoff path, not a fabricated Run. A transfer ends the old owner's work; it must not keep editing in parallel.

## Review and repair

The other primary agent reviews the actual diff and acceptance evidence without modifying the implementer's files. Prioritize correctness, unintended effects, missing goal requirements, and real regressions. Do not stall completion on style opinions or hypothetical redesigns. The implementer fixes material findings; the reviewer verifies those fixes.

Run targeted tests and drive the relevant real surface. Test-only results remain test-only. Missing dependencies, unavailable review, failed tests, and untested environments are explicitly recorded. Never label them PASS.

## Checkpoints and finish

At a meaningful boundary, write a short checkpoint and update Orca's worktree comment. Use the target project's evidence and PR practices. Otherwise prefer `.concertante/checkpoint.md`, excluded from Git before writing private content. It is a human-readable evidence index, not lifecycle authority.

Include goal, base/current commit, owner, observed result, unresolved work, next action, and exact evidence references. Keep project secrets and raw user data out of checkpoint text.

Finish only when acceptance is verified and required review/PR actions are complete. State what changed, what was verified, and remaining support limits. A preserved blocked state is not success; identify the actual blocker and independent work already completed.
