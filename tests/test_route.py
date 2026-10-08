"""Behavioral CLI scenarios; synthetic usage only, no provider or Orca mutations."""

import json
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "skills/orca-concertante/scripts/concertante.py"


def scenario(used=20, other=20, **changes):
    return {
        "now": 2000000100,
        "current": "primary-a",
        "in_flight": False,
        "agents": {
            "primary-a": {"available": True, "observed_at": 2000000090, "windows": [
                {"name": "weekly", "status": "available", "used_percent": used, "resets_at": 2000010000},
            ]},
            "primary-b": {"available": True, "observed_at": 2000000090, "windows": [
                {"name": "session", "status": "available", "used_percent": other, "resets_at": 2000010000},
            ]},
        },
        **changes,
    }


def invoke(data):
    with tempfile.TemporaryDirectory(prefix="concertante-test-") as directory:
        path = Path(directory) / "snapshot.private.json"
        path.write_text(json.dumps(data), encoding="utf-8")
        result = subprocess.run([sys.executable, str(SCRIPT), "route", str(path)], capture_output=True, text=True, check=False)
        return result.returncode, json.loads(result.stdout)


def main():
    cases = []
    for used, action, owner in [(79.9, "keep", "primary-a"), (80, "handoff", "primary-b"), (90, "handoff", "primary-b"), (100, "handoff", "primary-b")]:
        cases.append((scenario(used), 0, action, owner))
    cases.append((scenario(100, in_flight=True), 0, "hold", "primary-a"))
    cases.append((scenario(95, 85), 0, "keep", "primary-a"))
    stale = scenario(95)
    stale["agents"]["primary-b"]["observed_at"] = 1999990000
    cases.append((stale, 0, "keep", "primary-a"))
    expired = scenario(95)
    expired["agents"]["primary-b"]["windows"][0]["resets_at"] = 2000000100
    cases.append((expired, 0, "keep", "primary-a"))
    unknown = scenario(95)
    unknown["agents"]["primary-b"]["windows"] = []
    cases.append((unknown, 0, "keep", "primary-a"))
    partial = scenario(95)
    partial["agents"]["primary-b"]["windows"].append({"name": "weekly", "status": "unavailable"})
    cases.append((partial, 0, "keep", "primary-a"))
    inapplicable = scenario(85)
    inapplicable["agents"]["primary-a"]["windows"].append({"name": "session", "status": "not_applicable"})
    cases.append((inapplicable, 0, "handoff", "primary-b"))
    unavailable = scenario()
    unavailable["agents"]["primary-a"]["available"] = False
    cases.append((unavailable, 0, "handoff", "primary-b"))
    both = scenario()
    for agent in both["agents"].values():
        agent["available"] = False
    cases.append((both, 0, "blocked", None))
    for bad in [True, -1, 101, float("nan"), "10"]:
        cases.append((scenario(bad), 2, None, None))
    future = scenario()
    future["agents"]["primary-a"]["observed_at"] = 2000000101
    cases.append((future, 2, None, None))
    malformed = scenario(in_flight="false")
    cases.append((malformed, 2, None, None))
    for index, (data, code, action, owner) in enumerate(cases):
        actual_code, actual = invoke(data)
        assert actual_code == code, (index, actual_code, actual)
        if code == 0:
            assert (actual["action"], actual["owner"]) == (action, owner), (index, actual)
            assert actual["advisory_only"] is True
        else:
            assert actual["ok"] is False
    print(f"PASS: {len(cases)} routing CLI scenarios")


if __name__ == "__main__":
    main()
