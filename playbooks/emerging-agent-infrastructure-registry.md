# Emerging Agent Infrastructure Registry

Status: Draft

Owner: SandBase growth / ecosystem

## Positioning

SandBase should not build a generic AI tools directory.

The sharper opportunity is:

```text
Emerging Agent Infrastructure
```

This is a curated registry for new, future-facing, technically valuable projects around AI agents, especially projects that could eventually integrate deeply with SandBase.

## Why This Matters

SandBase is agent infrastructure. A registry can become an ecosystem layer if it helps builders discover the components shaping production AI agents:

- runtimes
- tools and MCP servers
- sandboxes
- computer use
- memory
- observability and evals
- deployment
- compute
- multi-agent systems
- agent workspaces

The registry should help answer:

```text
What new infrastructure projects are shaping the future of AI agents?
Which of them could run on, connect to, or extend SandBase?
```

## What This Is Not

This should not become:

- a generic AI tool directory
- a list of chatbot wrappers
- a collection of writing/image/video AI apps
- a pay-to-list directory
- a backlink farm
- a marketplace before there is ecosystem substance

## Selection Criteria

Every listed project should match most of these criteria:

1. Agent-native  
   Built for agents, tool use, runtime, orchestration, memory, sandboxing, eval, deployment, or agent workflows.

2. Emerging  
   New, fast-moving, or still under-discovered. Mature projects can be included only when they define an important category.

3. Infrastructure value  
   Solves a technical capability problem rather than being a thin end-user AI app.

4. Future signal  
   Points toward a larger trend: MCP, computer use, multi-agent systems, agent-native cloud, sandboxed execution, agent observability, or distributed agent compute.

5. Builder-friendly  
   Has public code, docs, examples, demos, technical writing, or visible maintainers.

6. SandBase integration potential  
   Could eventually run on SandBase, use SandBase sandboxing, become a tool provider, extend agent infrastructure, or bring builders into the ecosystem.

## Categories

- Agent Runtimes
- Tool & MCP Infrastructure
- Sandboxes & Computer Use
- Agent Memory
- Observability & Evals
- Deployment & Compute
- Multi-Agent Systems
- Agent Workspaces
- Vertical Agent Infrastructure

## Project Card Fields

Each project should include:

| Field | Purpose |
|-------|---------|
| Name | Project name |
| One-line description | What it does |
| Category | Technical category |
| Stage | emerging / growing / established |
| Why it matters | The judgment that makes the registry useful |
| Future signal | What larger trend it represents |
| SandBase fit | runtime / sandbox / tooling / MCP / observability / compute / deployment / community |
| Integration potential | high / medium / watch |
| Links | GitHub / website / docs / demo |
| Notes | Open questions or follow-up |

## Integration Potential Rubric

### High

The project could clearly integrate with SandBase in one or more ways:

- run inside SandBase
- use SandBase sandbox/runtime
- expose tools to SandBase agents
- become an MCP/tool provider
- extend observability, evals, memory, compute, or deployment
- bring an active builder community

### Medium

The project is relevant to the agent infrastructure ecosystem, but the integration path needs more research.

### Watch

The project is early or promising, but not yet clear enough to prioritize.

## First Version Scope

The first version should be small:

- 20-30 curated projects
- manual review
- no paid listings
- no public ranking by default
- no generic AI apps
- clear submit criteria
- simple SandBase compatibility labels

## Navigation Recommendation

Start under:

```text
Resources -> Agent Registry
```

Do not make it a top-level `Marketplace` yet.

When the registry has enough quality projects, integrations, and submissions, it can evolve into:

```text
Ecosystem
```

## First Data Format

Start with a structured file before building a full product surface:

```text
name
category
description
stage
why_it_matters
future_signal
sandbase_fit
integration_potential
github
website
docs
notes
```

This can become JSON, CSV, or database records later.

## Operating Rule

```text
Curate for future signal, not volume.
```

The registry should make SandBase look like an ecosystem organizer, not a directory operator.
