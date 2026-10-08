# Handoff and recovery

## Safe task-owner changes

At a completed or positively settled boundary, record the unchanged goal, permissions, current commit/diff, evidence, holds, and next bounded task. Inspect the actual recipient and workspace. Follow the installed Orca guide to deliver and prove acceptance; input acceptance alone does not prove work began.

Do not interrupt an active external write or deployment because of quota. If its result is unknown, preserve the evidence and assignment until its effect and ownership are resolved. Do not delete markers, replay writes, or start a competing editor.

## Coordinator changes

Task reassignment is not coordinator takeover. Read the installed `orchestration` guide and its relevant recovery/binding reference; inspect the existing Run and principal. Use only a supported, attested transfer for that run type. A legacy-specific takeover flag is not a generic coordinator switch.

Prove the former coordinator has stopped coordinating and the new coordinator owns the same current authority before consuming mail or dispatching. If transfer cannot be proven, keep coordination with the original primary and delegate the next task; record automatic coordinator takeover as unsupported. Do not create a new Run to evade a failed attempt or circuit breaker.

## Interrupted or uncertain attempts

Inspect actual Orca liveness and receipts. Silence, timeout, stale output, TUI idle, contact loss, or missing quota data do not prove process exit or authorize retry. Load the installed recovery/cleanup guide and follow its exact next action. An uncertain mutation is recovered using the original request identity when supported, never a fresh blind send.

After a host restart, reconcile files, Git state, Run/Dispatch, and external-effect evidence before resuming. App window closure, daemon survival, and host restart are distinct cases. Never use old terminal handles after a runtime change without rediscovery.

## Minimal handoff record

```text
Goal and unchanged acceptance:
Authority and excluded effects:
Run/Task/Dispatch (only real current IDs):
Source base / current commit / uncommitted scope:
Current owner and proven settlement or transfer:
Completed evidence:
Unresolved effects and preserved holds:
Recipient and next bounded action:
Validation required to finish:
```

The agent fills this record. Do not require the user to complete it or choose routine steps again.
