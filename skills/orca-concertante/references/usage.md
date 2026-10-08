# Usage-aware next-task routing

Use live provider windows relevant to the intended model. Preserve provider, window, used percent, observed time, reset time, and availability. Do not compare subscription prices or assume equal raw percentages mean equal work capacity.

First investigate the installed Orca's supported machine-readable usage interface. Otherwise use provider-supported local read paths. Do not scrape credentials, copy auth cookies, spend reset credits, switch accounts, or alter HUD settings merely to observe usage. If a provider requires setup beyond existing authority, record unavailable and continue work that does not depend on it.

The optional route helper accepts normalized observations; it is not a collector or scheduler. Any adapter must confirm actual provider semantics. Do not assume `primary` always means five hours. A missing window is unknown; only mark it `not_applicable` when independently confirmed, and do not hardcode temporary account conditions into the package.

## Snapshot schema

Times are Unix seconds. `created_at` is snapshot creation time and `observed_at` belongs to each provider. The helper uses its own system clock for freshness; a snapshot older than five minutes or more than five seconds in the future is rejected. `available=false` means the agent is positively known unavailable; `true` means runnable, not guaranteed capacity. `windows=[]` is unknown. Omit genuinely inapplicable windows using an explicit entry. Agent keys are configurable strings; `current` must be one of them, and exactly two primary agents are required by this helper.

```json
{
  "created_at": 2000000100,
  "current": "primary-a",
  "ownership_state": "idle",
  "agents": {
    "primary-a": {
      "available": true,
      "observed_at": 2000000090,
      "windows": [{"name": "weekly", "status": "available", "used_percent": 85, "resets_at": 2000050000}]
    },
    "primary-b": {
      "available": true,
      "observed_at": 2000000095,
      "windows": [{"name": "session", "status": "available", "used_percent": 20, "resets_at": 2000009000}]
    }
  }
}
```

Each window status is `available`, `unavailable`, or `not_applicable`. Available windows require a finite percent in 0–100 and a positive reset time. Unknown/stale/expired observations never become zero usage. Future observation timestamps are rejected by parsing.

The timestamps above illustrate the format; replace them with current observations before execution. Ownership must be exactly `idle`, `active`, or `outcome_unknown`. Only `idle` allows a handoff recommendation. Unsupported/missing top-level fields are refused, so legacy boolean or additional safety state cannot silently disappear.

## Initial policy

- Below 80%: keep context; task suitability can still choose the other primary.
- At 80%: prefer a fresh, runnable alternative below 80% for a long new task.
- At 90%: recommend that same safe-boundary switch urgently.
- Active or outcome-unknown work: preserve current ownership; inspect first.
- Both pressured or alternative unknown: retain the current runnable owner, report pressure, and choose a small useful unit. Actual execution refusal requires official recovery, not infinite retry.
- A known-unavailable current agent may yield to a runnable alternative, with quota uncertainty explicit.

Five-minute freshness and 80/90% are starting defaults, not provider limits or optimality claims. Reset times determine whether observations are valid; do not automatically equate an imminent reset with renewed capacity. Check at task starts and meaningful checkpoints, not with a new constant polling daemon.

The helper's decision is advisory. It does not authorize mutations or prove the prior dispatch settled. Apply the current Orca handoff contract before any reassignment.
