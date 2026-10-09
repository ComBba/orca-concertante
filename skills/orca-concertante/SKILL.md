---
name: orca-concertante
description: Coordinate goal-driven coding work in Orca with explicit ownership, independent review, usage-aware task allocation, and safe handoffs. Use when asked to carry a coding goal across agents or apply Concertante; not for unrelated solo edits or one-off terminal inspection.
---

# Orca Concertante

Turn one user goal into verified coding work. Preserve that goal, authority, and completion criteria across agent changes. Follow repository rules and the user's newer instructions.

## Start without a questionnaire

Read the goal and project rules; inspect current work before making changes. Derive observable acceptance criteria and a practical first task. Ask only for information or authority that genuinely blocks a material decision. Complete clear authorized work without repeated permission prompts.

Resolve Orca exactly as its installed discovery guide requires: `ORCA_CLI_COMMAND` when set, otherwise `orca-dev` for a session exposing `ORCA_DEV_REPO_ROOT`, `orca-ide` on Linux outside Orca, otherwise `orca`. Reuse that executable; do not silently switch runtimes after errors.

Read its `skills get orca-cli --json`, `skills get orchestration --json`, and `status --json`. Do not invent flags or use retired scheduler commands. Full ownership handoff and supervised work are different paths: follow the current guide for the selected path.

## Roles

Default to Codex for the initial concept and acceptance criteria; Codex and Claude are both primary implementers and reviewers. Choose the next task by fit, context, access, and actual availability. Keep one coordinator and one editor per overlapping scope. Independent changes may use isolated worktrees.

Antigravity, if present, provides brief third-party observations only. Do not assign it deep research, large implementations, production actions, or final acceptance. Respect user-selected models; otherwise inherit configured defaults. Other agent combinations are allowed.

If invoked in Claude with no initial design, obtain Codex's concept through supported Orca coordination when available. If Codex is unavailable, record the exception and preserve progress within authority; do not force the user to restart the task. One-agent execution cannot claim independent review.

Read [workflow](references/workflow.md) for actual coordination, checkpoints, and completion. Read [usage](references/usage.md) when deciding task allocation. Read [handoff](references/handoff.md) before changing ownership or recovering an interrupted run.

Make collaboration inspectable: identify each participating agent's role, workspace, and visible tab; report observed progress and results. When the user requests visibility or preservation of agent sessions, retain settled worker terminals through Orca's supported contract rather than automatically closing them. Follow [workflow](references/workflow.md) for visibility and cleanup accounting.

## Complete with evidence

Execute the smallest useful task, verify its real surface, use an independent review where available, and fix material findings. Follow the target repository's PR and release policy. Do not treat an input receipt, heartbeat, green tests, or merge as proof of the user's full goal.

Record concise private checkpoints under the project's ignored `.concertante/` directory, or its existing designated private evidence location. Reuse Orca's Run/Task/Dispatch as lifecycle authority; do not create a competing task database. Never put credentials or raw private transcripts into reports.

For publication, include portable instructions and synthetic examples only. Stop on uncertain external effects and inspect; never replay an ambiguous write to make progress. A model limit is a scheduling condition, not permission to broaden scope or bypass safeguards.
