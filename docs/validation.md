# Validation status

This first release is a skill package with advisory helpers. It is not a new scheduler.

| Surface | Status |
|---|---|
| Normalized usage routing CLI | PASS: 20 executable synthetic CLI scenarios |
| Skill structure/frontmatter | PASS: skill-creator quick validator |
| Live Orca read-only readiness | PASS: doctor on Orca 1.4.222/macOS, runtime and graph ready |
| Skill discovery/install | PASS: npx skills local installation for Codex and Claude into an isolated temporary project; entrypoint/helper bytes equal source |
| Independent behavioral review | Pending execution |
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
