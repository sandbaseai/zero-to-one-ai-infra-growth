# Runseal Compatibility Probe Brief

Date: 2026-06-24

Purpose: turn the Day 15 open-source sourcing result into a small, useful SandBase ecosystem asset.

## Why Runseal

Runseal is a strong fit for SandBase's agent infrastructure positioning because it focuses on local-first sandboxed execution for AI agents, with a stable execution protocol, policy-governed filesystem and network boundaries, capability reporting, JSONL audit output, and black-box conformance tests.

The opportunity is not to compete with Runseal. The opportunity is to define a small neutral probe that helps agent builders compare sandbox runtimes in practical terms.

## Current Candidate State

Repository: https://github.com/runseal-labs/runseal

Observed on 2026-06-24:

- public repository
- Apache-2.0 license
- primary language: Rust
- pushed on 2026-06-24
- homepage: https://runseal-labs.github.io/runseal/
- status described as a technical-preview release for third-party integration

Relevant surfaces:

- CLI: `runseal exec --json`
- event stream: `runseal exec --events`
- JSON-RPC stdio: `runseal rpc --stdio`
- service stdio: `runseal service --stdio`
- capability discovery: `getCapabilities`
- setup readiness: `getSetupStatus`
- audit access: `getAuditEvents`, `tailAudit`
- conformance tests: `tests/`

## Proposed Asset

Working name:

```text
agent-sandbox-runtime-probe
```

First version:

- README explaining the probe dimensions
- a runtime compatibility checklist
- sample JSON test cases
- optional CLI harness later

Do not start with SandBase branding. Start with a neutral developer utility and mention SandBase as the maintainer context only after the asset is useful on its own.

## Probe Dimensions

### 1. Capability Discovery

Questions:

- Can the runtime describe supported sandbox levels?
- Can it describe supported network modes?
- Can it distinguish supported, experimental, and unsupported features?
- Does the client have enough information to fail closed before execution?

Expected evidence:

- structured capabilities output
- explicit unsupported states
- stable protocol or schema version

### 2. Filesystem Boundary

Questions:

- Can the runtime allow workspace writes while blocking writes outside the workspace?
- Can it support read-only execution?
- Does it document whether host files may remain readable?
- Does it handle parent traversal and symlink traversal cases?

Expected evidence:

- allowed write inside workspace
- denied write outside workspace
- explicit behavior for host reads
- public-safe error output

### 3. Network Boundary

Questions:

- Can the runtime run with unmanaged networking?
- Can it deny networking?
- Can it proxy networking when supported?
- Does unsupported proxy mode fail closed?

Expected evidence:

- direct network pass-through when requested
- direct socket or HTTP egress denial when disabled
- proxy support or explicit unsupported result
- audit event for network decision

### 4. Execution Lifecycle

Questions:

- Does the runtime support timeout?
- Does it clean up child processes?
- Can a running execution be cancelled?
- Can completed executions be queried or replayed?

Expected evidence:

- timeout error
- cancellation behavior
- no orphaned process tree
- execution ID or trace ID

### 5. Audit And Trace

Questions:

- Are execution decisions emitted as structured events?
- Are denied operations recorded?
- Can clients retrieve audit logs after execution?
- Are logs safe to share publicly?

Expected evidence:

- JSON or JSONL event stream
- start, finish, denial, setup failure, and network decision events
- no leaked backend-private details

## Initial Test Cases

```json
[
  {
    "id": "capabilities-basic",
    "goal": "Runtime exposes sandbox levels and network modes before execution."
  },
  {
    "id": "workspace-write-inside",
    "goal": "Command can create a file inside the declared workspace."
  },
  {
    "id": "workspace-write-outside-denied",
    "goal": "Command cannot create a file outside the declared workspace."
  },
  {
    "id": "network-disabled-denies-egress",
    "goal": "HTTP or socket egress fails when network mode is disabled."
  },
  {
    "id": "timeout-kills-execution",
    "goal": "Long-running command terminates with a structured timeout result."
  },
  {
    "id": "audit-events-present",
    "goal": "Execution produces structured audit or trace events."
  }
]
```

## Day 15 Decision

Pick Runseal as the first ecosystem probe target.

Reason:

- It is active today.
- It is close to SandBase's sandbox/runtime theme.
- It exposes clear integration surfaces.
- A probe/checklist can be useful without needing permission from the maintainer.
- It creates a credible future community interaction: share a concrete checklist or test result instead of a promotional link.

## Next Build Step

Create a small standalone repository or folder with:

```text
README.md
checklists/runtime-compatibility.md
cases/sandbox-runtime-probe.json
notes/runseal-observations.md
```

First public interaction should be a useful note or issue only after the probe is concrete enough to show what it checks.
