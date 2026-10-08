# Loop engineering and communication

The product is a goal-directed collaboration loop. The first release encodes its
policy in a skill and provides optional read-only/advisory tools. It does not claim
that a new automatic scheduler has been implemented.

## The unit of progress

Each iteration has a concrete target, one owner, a bounded change, an observable
acceptance check, and a resulting decision. A test run is evidence for its covered
behavior; it is not proof of a whole feature, live operation, or user goal.

The coordinator compares the result to acceptance, routes material repairs, and
selects the next useful unit. Avoid loops that only repeat status, rebuild unchanged
evidence, or chase style opinions. Stop when the goal is proven, the user cancels,
or a genuine blocker preserves a resumable checkpoint.

## Communication that changes action

| Message | Contents | Consumer action |
|---|---|---|
| Task | Target, change, constraints, owner, observable acceptance | Execute the bounded scope |
| Question | Blocking fact/decision and bounded options | Coordinator resolves within authority |
| Finding | Exact source, scenario, severity, observed failure | Implementer repairs; reviewer rechecks |
| Completion | Current dispatch identity, outcome, evidence, unresolved work | Validate settlement, decide next owner |
| Handoff | Unchanged goal/authority, source state, evidence, held effects, next task | Prove transfer before new execution |

Use Orca's supported messages rather than titles or free-form “continue” commands
as lifecycle proof. Accepted input is not a started turn; a heartbeat is not
completion; a timeout is not failure. Process messages before acknowledgment.

## Three specialists, flexible work

The goal lead establishes the concept. A primary specialist builds and verifies.
Another primary independently reviews; an optional third specialist offers brief
cross-checks. Primary roles can rotate at settled boundaries. The default profile
does not require equal workload, equal model capability, or three simultaneous editors.

Add an agent when an independent slice or perspective materially improves the result.
Parallelize independent work; serialize shared edits and effects.

## Recovery belongs in the loop

Fresh usage helps assign the next unit. It never authorizes replaying an ambiguous
effect, interrupting a writer, bypassing authentication, or changing the agreed goal.
Outcome-unknown state preserves ownership. Inspect original receipts and execution
state through the installed Orca recovery contract.

Coordinator transfer is separate from task reassignment. Support depends on Orca's
current authority/binding contract and must be proved in an actual integration test.
The first release marks generic automatic coordinator takeover as unverified.

## Public evidence

Publish portable reproduction steps and synthetic fixtures. Keep credentials,
private transcripts, personal paths, and operational data out of issues and examples.
Record support claims only after testing the exact installation/runtime scenario.
