# Open Source Opportunity Sourcing SOP

Purpose: find three small open-source opportunities per day that can help SandBase participate in the agent infrastructure ecosystem.

This is not about chasing stars or copying popular projects. The goal is to find useful gaps around emerging agent infrastructure projects and build small, credible, maintainable assets.

## Daily Output

Each day:

1. Scan GitHub, Peerlist, X, and relevant launch/community feeds.
2. Find three candidate opportunities.
3. Score each candidate.
4. Pick one to build or prepare.
5. Record why we chose it.

## Selection Criteria

A good candidate should match most of these:

- agent infrastructure related
- emerging or fast-moving
- not too complex for a 1-2 day build
- useful to the original project's users
- can be maintained as a small standalone repo
- naturally fits SandBase's positioning
- does not require pretending to be an official integration
- creates a reason for genuine community interaction

## Good Project Types

- starter templates
- compatibility checkers
- examples
- adapters
- benchmark scripts
- security checklists
- comparison notes
- MCP/tool wrappers
- sandbox demos
- deployment recipes

## Avoid

- cloning a product
- competing directly with a maintainer's core work
- filing low-effort issues just to get attention
- adding SandBase branding before the project has standalone value
- building something too broad to finish quickly
- targeting generic AI apps with no infrastructure angle

## Daily Scoring

Score each candidate from 1 to 5:

| Field | Question |
|-------|----------|
| Relevance | Is it clearly agent infrastructure? |
| Buildability | Can we ship a useful first version in 1-2 days? |
| Community fit | Would the original project or users care? |
| SandBase fit | Does it connect to runtime, sandbox, tools, compute, evals, or deployment? |
| Distribution value | Can it create a credible public signal without spam? |

Pick the project with the best combination of buildability and ecosystem fit.

## Today's Candidates — 2026-06-21

### 1. `emberd` Agent Tool Sandbox Examples

Repository: https://github.com/hdprajwal/emberd

What it is:

Firecracker-based sandboxing runtime that runs AI-agent tool calls inside isolated microVMs.

Opportunity:

Create a small repo with client examples and a compatibility checklist for running agent tool calls against an emberd-style HTTP sandbox API.

Possible repo:

```text
agent-tool-sandbox-examples
```

First version:

- Python example: run code in a sandbox through HTTP
- TypeScript example: same flow
- checklist: timeout, stdout/stderr, exit code, file access, network access, cleanup
- notes: what production agents need from a sandbox API

Why it is good:

- very close to SandBase's sandboxed tool execution positioning
- low complexity
- useful even if emberd changes
- can later become a SandBase compatibility benchmark

Score:

- Relevance: 5
- Buildability: 5
- Community fit: 4
- SandBase fit: 5
- Distribution value: 4

Recommendation: highest priority.

### 2. `trytet` Wasm Agent Sandbox Proof Examples

Repository: https://github.com/bneb/trytet

What it is:

Wasm sandbox runtime for AI agent code execution with deterministic traps, fuel-bounded execution, MCP-native direction, and quick demos.

Opportunity:

Create a small proof/example repo around fuel-bounded agent tasks and explain how to evaluate sandbox behavior for agents.

Possible repo:

```text
agent-sandbox-fuel-tests
```

First version:

- tiny infinite-loop test
- CPU-bound task test
- file access expectation checklist
- MCP-style tool-call safety notes
- README explaining why fuel limits matter for production agents

Why it is good:

- strong technical story
- maps to sandbox safety
- useful for explaining agent runtime risk

Risk:

- project is already broad and opinionated
- may require learning its CLI/build path before producing useful examples

Score:

- Relevance: 5
- Buildability: 3
- Community fit: 3
- SandBase fit: 5
- Distribution value: 4

Recommendation: good second choice.

### 3. `funky` Agent Runtime Contract Examples

Repository: https://github.com/funkyhq/funky

What it is:

Open protocol for cloud-native AI agents with pluggable sandboxes, session stores, and runtimes behind one contract.

Opportunity:

Create a small "agent runtime contract checklist" or example implementation notes for comparing sandbox runtime, session store, and agent loop boundaries.

Possible repo:

```text
agent-runtime-contract-checklist
```

First version:

- README checklist
- minimal JSON/YAML contract examples
- session lifecycle diagram
- sandbox/runtime/session-store boundary notes
- compatibility questions for builders

Why it is good:

- strong conceptual overlap with SandBase
- low code complexity if started as docs/checklist
- can become a useful content asset

Risk:

- less concrete than a runnable example
- may feel too abstract unless tied to a demo

Score:

- Relevance: 5
- Buildability: 4
- Community fit: 3
- SandBase fit: 5
- Distribution value: 3

Recommendation: good if we want a documentation-first open-source asset.

## Today's Pick

Recommended pick:

```text
agent-tool-sandbox-examples
```

Why:

- easiest to ship quickly
- closest to SandBase's sandbox/runtime positioning
- useful regardless of which sandbox backend is used
- can start as standalone examples, then later add SandBase, emberd, E2B, Modal, or local adapters

## First Build Plan

Repo name:

```text
agent-tool-sandbox-examples
```

Initial structure:

```text
README.md
examples/
  python-http-sandbox/
  typescript-http-sandbox/
checklists/
  sandbox-api-compatibility.md
  production-agent-tool-safety.md
```

README positioning:

```text
Examples and checklists for running AI-agent tool calls inside sandboxed runtimes.
```

No hard SandBase promotion in the first version. Add SandBase as the maintainer / ecosystem context, not as the only supported backend.

## Daily Operating Rule

```text
Find projects with real technical momentum.
Build small assets that make the ecosystem easier to use.
Let SandBase earn attention by being useful.
```
