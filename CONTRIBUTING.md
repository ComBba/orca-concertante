# Contributing

Start with a reproducible failure or concrete improvement to goal completion.
Include Orca and agent/CLI versions, support boundary, and redacted steps. Do not
upload credentials, private transcripts, personal paths, or production data.

Use a feature branch and include behavioral verification:

```bash
python3 tests/test_route.py
python3 -m compileall -q skills/orca-concertante/scripts
```

For instruction changes, exercise a realistic request and inspect the result;
checking whether a sentence exists does not prove an instruction works. For live
integration, use an isolated generic project and distinguish input acceptance,
task settlement, and verified goal completion.

PRs explain the problem, resulting behavior, evidence, and limits. Fix material
review findings before merging. Use commit-preserving merges, not squash.
No new dependency or execution component without demonstrated need.
