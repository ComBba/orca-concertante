# Orca Concertante

A goal-driven coding-agent collaboration skill for [Orca](https://www.onorca.dev/).

Give the agent a goal once. Concertante helps it define completion, divide work, review independently, and hand off at safe checkpoints without repeatedly asking you to choose the next routine step.

This is an independent community project, not an official Orca product.

## Install

Prerequisites: Orca and its registered CLI, at least one configured coding agent, and Python 3.11+ for the optional helpers. Agents retain their existing authentication and model configuration.

```bash
npx skills add https://github.com/ComBba/orca-concertante --skill orca-concertante --global
```

For one project, omit `--global`. Review the installer target selection before accepting it. Installation does not change repository rules, provider credentials, models, or production settings.

Then ask your agent:

> Use Orca Concertante to add CSV export to this application. Complete implementation, independent review, and verification. Follow this repository's PR policy.

You can invoke `$orca-concertante` explicitly where supported. Ordinary natural-language discovery depends on the agent's skill support.

## Default collaboration profile

| Responsibility | Default |
|---|---|
| Initial concept, scope, acceptance criteria | Codex |
| Implementation, research, verification | Codex or Claude, chosen per task |
| Independent review | The other primary agent |
| Current coordination | One primary agent at a time |
| Optional third perspective | Antigravity: brief observations only |

These are defaults, not vendor requirements. A project can replace the agents or use one agent, reporting the missing independent review rather than pretending it happened. Work allocation follows task fit, context, access, actual availability, and handoff cost—not subscription price.

## Included

- A portable skill entrypoint using the installed Orca CLI's version-matched guides.
- Goal, ownership, handoff, recovery, and evidence conventions.
- Optional read-only `doctor` and advisory `route` helpers; Python standard library only.
- A generic example and executable routing tests.

The helper **does not** collect provider credentials, launch workers, transfer coordinator authority, or run a background scheduler. The agent executes supported Orca operations under the user's task authorization. A skill is guidance, not a guarantee of perpetual unattended execution.

## Helpers

Resolve the installed skill directory and use its script:

```bash
python3 <skill-directory>/scripts/concertante.py doctor
python3 <skill-directory>/scripts/concertante.py route <private-snapshot.json>
```

`doctor` reads Orca runtime readiness and advertised capabilities. `route` validates a supplied usage snapshot and recommends keeping or changing the next task owner. Neither mutates Orca or the project. See [usage and routing](skills/orca-concertante/references/usage.md).

## Support and verification

The installed Orca guide is authoritative for command syntax. Initial compatibility inspection used Orca 1.4.222 on macOS; other versions and platforms require their own verification. Unknown capability or ambiguous execution stays unverified.

[Validation status](docs/validation.md) distinguishes local tests, live read-only inspection, installation, and end-to-end agent collaboration. Successful tests do not imply autonomous cross-agent completion is proven.

## Development

```bash
python3 tests/test_route.py
python3 -m compileall -q skills/orca-concertante/scripts
```

Use feature branches and commit-preserving PR merges. Do not commit private snapshots, credentials, raw session transcripts, or project-specific operational records.

## Official references

- [Skills registry and distribution](https://www.onorca.dev/docs/cli/skills)
- [Orchestration](https://www.onorca.dev/docs/cli/orchestration)
- [CLI reference](https://www.onorca.dev/docs/cli/reference)
- [Usage tracking](https://www.onorca.dev/docs/agents/usage-tracking)
- [Session restore](https://www.onorca.dev/docs/model/session-restore)

License: MIT.
