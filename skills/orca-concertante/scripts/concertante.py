# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
# Run: python3 concertante.py doctor | route <private-snapshot.json>
"""Read-only Orca readiness and advisory next-task routing, with no dependencies."""

from __future__ import annotations

import json
import math
import os
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Final, TypeAlias

Json: TypeAlias = str | int | float | bool | None | list["Json"] | dict[str, "Json"]
FRESHNESS: Final = 300
WARNING: Final = 80
CRITICAL: Final = 90


class InputError(Exception):
    """Invalid normalized input; values are not echoed into public output."""


@dataclass(frozen=True, slots=True)
class Agent:
    name: str
    available: bool
    peak: float | None


@dataclass(frozen=True, slots=True)
class Snapshot:
    current: Agent
    alternative: Agent
    in_flight: bool


@dataclass(frozen=True, slots=True)
class Decision:
    owner: str | None
    action: str
    reason: str
    advisory_only: bool = True


def mapping(value: Json) -> dict[str, Json]:
    if not isinstance(value, dict):
        raise InputError("expected_object")
    return value


def number(value: Json) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise InputError("expected_number")
    try:
        result = float(value)
    except OverflowError as error:
        raise InputError("number_out_of_range") from error
    if not math.isfinite(result):
        raise InputError("expected_finite_number")
    return result


def boolean(value: Json) -> bool:
    if type(value) is not bool:
        raise InputError("expected_boolean")
    return value


def parse_agent(name: str, value: Json, now: float) -> Agent:
    """Unknown, expired, or partial observations cannot earn a low-use verdict."""
    data = mapping(value)
    available = boolean(data.get("available"))
    observed = number(data.get("observed_at"))
    if observed <= 0 or observed > now:
        raise InputError("invalid_observation_time")
    windows = data.get("windows")
    if not isinstance(windows, list):
        raise InputError("expected_windows")
    peaks: list[float] = []
    unknown = now - observed > FRESHNESS
    names: set[str] = set()
    for window_value in windows:
        window = mapping(window_value)
        window_name = window.get("name")
        if not isinstance(window_name, str) or not window_name or window_name in names:
            raise InputError("invalid_window_name")
        names.add(window_name)
        match window.get("status"):
            case "not_applicable":
                continue
            case "unavailable":
                unknown = True
            case "available":
                used = number(window.get("used_percent"))
                reset = number(window.get("resets_at"))
                if not 0 <= used <= 100 or reset <= 0:
                    raise InputError("invalid_window_value")
                unknown = unknown or reset <= now
                peaks.append(used)
            case _:
                raise InputError("invalid_window_status")
    peak = max(peaks) if peaks and not unknown else None
    return Agent(name, available, peak)


def parse_snapshot(raw: Json) -> Snapshot:
    data = mapping(raw)
    now = number(data.get("now"))
    if now <= 0:
        raise InputError("invalid_decision_time")
    agents = mapping(data.get("agents"))
    if len(agents) != 2 or any(not name.strip() for name in agents):
        raise InputError("expected_two_named_primary_agents")
    current = data.get("current")
    if not isinstance(current, str) or current not in agents:
        raise InputError("invalid_current_agent")
    alternative = next(name for name in agents if name != current)
    return Snapshot(
        parse_agent(current, agents[current], now),
        parse_agent(alternative, agents[alternative], now),
        boolean(data.get("in_flight")),
    )


def route(snapshot: Snapshot) -> Decision:
    """Suggest the next task owner; never transfer active ownership."""
    current, other = snapshot.current, snapshot.alternative
    if snapshot.in_flight:
        return Decision(current.name, "hold", "active_or_uncertain_work")
    if not current.available:
        if other.available:
            return Decision(other.name, "handoff", "current_unavailable_check_alternative_quota")
        return Decision(None, "blocked", "both_unavailable_preserve_state")
    if current.peak is None:
        return Decision(current.name, "keep", "quota_unknown_refresh_before_long_task")
    if current.peak >= WARNING:
        if other.available and other.peak is not None and other.peak < WARNING:
            reason = "critical_usage_safe_boundary" if current.peak >= CRITICAL else "high_usage_next_task"
            return Decision(other.name, "handoff", reason)
        return Decision(current.name, "keep", "usage_pressure_alternative_unproven_or_pressured")
    return Decision(current.name, "keep", "context_and_task_fit")


def orca_executable() -> str:
    configured = os.environ.get("ORCA_CLI_COMMAND")
    if configured:
        return configured
    if os.environ.get("ORCA_DEV_REPO_ROOT"):
        return "orca-dev"
    if sys.platform.startswith("linux"):
        # Conservative outside-session default; explicit env handles managed sessions.
        return "orca-ide"
    return "orca"


def doctor() -> int:
    """Emit only runtime readiness/version/capabilities, not raw status or stderr."""
    result = subprocess.run(
        [orca_executable(), "status", "--json"],
        capture_output=True, text=True, timeout=30, check=False,
    )
    if result.returncode != 0:
        print(json.dumps({"ok": False, "error": "orca_status_failed"}))
        return 1
    raw: Json = json.loads(result.stdout)
    envelope = mapping(raw)
    payload = mapping(envelope.get("result"))
    runtime = mapping(payload.get("runtime"))
    graph = mapping(payload.get("graph"))
    ok = envelope.get("ok") is True and runtime.get("reachable") is True and runtime.get("state") == "ready"
    ready = ok and graph.get("state") == "ready"
    print(json.dumps({
        "ok": ready,
        "app_version": runtime.get("appVersion"),
        "runtime_state": runtime.get("state"),
        "graph_state": graph.get("state"),
        "capabilities": runtime.get("capabilities", []),
        "read_only": True,
    }))
    return 0 if ready else 1


def main() -> int:
    args = sys.argv[1:]
    try:
        match args:
            case ["doctor"]:
                return doctor()
            case ["route", filename]:
                with Path(filename).open(encoding="utf-8") as stream:
                    raw: Json = json.load(stream)
                print(json.dumps(asdict(route(parse_snapshot(raw)))))
                return 0
            case _:
                print("Usage: concertante.py doctor | route <private-snapshot.json>", file=sys.stderr)
                return 2
    except InputError as error:
        print(json.dumps({"ok": False, "error": str(error)}))
        return 2
    except (OSError, subprocess.TimeoutExpired, json.JSONDecodeError):
        print(json.dumps({"ok": False, "error": "read_failed_or_invalid_json"}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
