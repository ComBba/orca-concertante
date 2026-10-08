# Security and effect boundaries

The skill grants no new permissions. Existing user authorization, repository
rules, and Orca's execution authority remain in force.

Helpers do not read authentication files, transmit usage snapshots, mutate Orca,
or launch agents. Keep observations and checkpoints private. Never replay an
uncertain mutation just because an agent or quota changed.

Do not report secrets or sensitive evidence in public issues. Use GitHub's
**Report a vulnerability** entry if private reporting is enabled. Otherwise keep
the evidence private and ask the maintainer for a private channel.

Support claims and unverified scenarios are tracked in [validation](docs/validation.md).
