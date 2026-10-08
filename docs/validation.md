# Validation status

This first release is a skill package with advisory helpers. It is not a new scheduler.

| Surface | Status |
|---|---|
| Normalized usage routing CLI | PASS: 28 executable synthetic CLI scenarios, including system-clock freshness and outcome-unknown ownership |
| Doctor error boundary | PASS: 5 isolated process-boundary scenarios, including missing CLI, nonzero status and malformed status |
| Skill structure/frontmatter | PASS: skill-creator quick validator |
| Live Orca read-only readiness | PASS: doctor on Orca 1.4.222/macOS, runtime and graph ready |
| Skill discovery/install | PASS: npx skills local installation for Codex and Claude into an isolated temporary project; entrypoint/helper bytes equal source |
| Independent behavioral review | Initial review found two HIGH and one MEDIUM; fixes awaiting independent recheck |
| End-to-end Codex↔Claude task handoff | Not covered |
| Generic coordinator takeover | Not covered; only supported Orca contracts may be used |
| Host reboot / daemon failure recovery | Not covered |
| Linux and Windows live Orca integration | Not covered |

Tests use synthetic usage records and do not consume provider quota. Live readiness
does not prove successful dispatch, settlement, or autonomous goal completion.

Additional checks: Ruff passed; basedpyright reported zero errors and two warnings
at the standard-library JSON decode boundary. Parsed fields are checked before routing.
Compilation passed. A public-content scan found no project-specific service names,
host addresses, domain names, customer records, or workstation paths in package files.

The initial discovery command combined `--list --json`; the installer refused that
combination before installation. Discovery was retried with supported flags. Actual
installation used `--json` without `--list` and succeeded. No global installation or
existing agent settings were changed by the isolated installation test.

Independent review identified caller-controlled freshness time, unrepresentable
outcome-unknown ownership, and ambiguous Linux executable selection. The revised
helper uses system time, requires `idle|active|outcome_unknown`, refuses unsupported
top-level fields, accepts an explicitly resolved CLI, and reports distinct sanitized
doctor errors. Linux requires a resolved executable or the exported CLI environment.
