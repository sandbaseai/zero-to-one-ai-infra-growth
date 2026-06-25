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

## Candidate Batches

- [GitHub Ecosystem Candidates — 2026-06-24](github-ecosystem-candidates-2026-06-24.md)

## Reviewed Project Cards

### Azure/kars

| Field | Value |
|-------|-------|
| Name | Azure/kars |
| One-line description | Kubernetes agent reference stack for governed agent runtime, tool policy, egress control, and hardened per-agent sandboxes. |
| Category | Agent Runtimes |
| Stage | growing |
| Why it matters | Shows agent runtime problems as Kubernetes control-plane problems: policy compilation, router reload, egress approval, and sandbox isolation. |
| Future signal | Agent infrastructure is moving toward explicit policy/control-plane APIs rather than one-off tool wrappers. |
| SandBase fit | runtime / sandbox / tooling / observability |
| Integration potential | high |
| Links | https://github.com/Azure/kars |
| Notes | Track issue #451 for policy freshness. Useful comparison point for SandBase runtime evidence: observed CR generation, compiled policy digest, propagation time, and runtime acknowledgement. |

### ageos-labs/ageos-runtime

| Field | Value |
|-------|-------|
| Name | ageos-labs/ageos-runtime |
| One-line description | Runtime control layer for AI agents with sandboxed local execution and OpenClaw workflow support. |
| Category | Sandboxes & Computer Use |
| Stage | emerging |
| Why it matters | Makes syscall-level hardening and runtime isolation a visible part of agent execution rather than an implicit platform concern. |
| Future signal | Agent sandboxes will need negative-path validation, not only happy-path execution. |
| SandBase fit | sandbox / runtime / observability |
| Integration potential | medium |
| Links | https://github.com/ageos-labs/ageos-runtime |
| Notes | Track issue #24 for seccomp validation. A strong comment should focus on positive-path and negative-path regression matrices. |

### kubernetes-sigs/agent-sandbox

| Field | Value |
|-------|-------|
| Name | kubernetes-sigs/agent-sandbox |
| One-line description | Kubernetes SIG project for isolated, stateful workloads and AI agent runtime environments. |
| Category | Deployment & Compute |
| Stage | established signal / emerging project |
| Why it matters | High-authority signal that agent execution environments are becoming an infrastructure category inside Kubernetes. |
| Future signal | Sandboxed agent workloads may become a first-class scheduling and isolation pattern. |
| SandBase fit | deployment / compute / sandbox |
| Integration potential | watch |
| Links | https://github.com/kubernetes-sigs/agent-sandbox |
| Notes | Track as an ecosystem anchor. Do not comment until SandBase has concrete compatibility tests or implementation feedback. |

### opensandbox-group/OpenSandbox

| Field | Value |
|-------|-------|
| Name | opensandbox-group/OpenSandbox |
| One-line description | Open sandbox platform with SDKs, Docker-backed execution, and configurable egress/network policy controls. |
| Category | Sandboxes & Computer Use |
| Stage | growing |
| Why it matters | Makes network policy and egress sidecars a concrete operator concern for agent execution environments. |
| Future signal | Production agent sandboxes need diagnosable network-policy enforcement, including kernel capability checks, DNS redirect behavior, sidecar readiness, and structured failure reasons. |
| SandBase fit | sandbox / runtime / network policy / observability |
| Integration potential | medium |
| Links | https://github.com/opensandbox-group/OpenSandbox |
| Notes | Track issue #1120 for WSL2 Docker `NetworkPolicy` failure. Comment only if SandBase can add a distinct troubleshooting matrix or compatibility signal beyond existing maintainer analysis. |

### openclaw/openclaw

| Field | Value |
|-------|-------|
| Name | openclaw/openclaw |
| One-line description | Agent runtime / tooling platform with active work around web-tool network access control and egress policy. |
| Category | Agent Runtimes |
| Stage | growing |
| Why it matters | Exposes egress firewall design as a product and security-control question for agent web tools. |
| Future signal | Agent runtimes will need domain policy, SSRF composition, deny/allow precedence, and audit evidence as first-class runtime controls. |
| SandBase fit | runtime / network policy / observability / security |
| Integration potential | medium |
| Links | https://github.com/openclaw/openclaw |
| Notes | Track issue #39685. Prepared a comment on enforcement evidence and policy digest acceptance criteria; browser posting was blocked by GitHub page timeouts. |

### ards-project/ard-spec

| Field | Value |
|-------|-------|
| Name | ards-project/ard-spec |
| One-line description | Agent registry / trust-manifest specification discussing runtime governance attestations and governed-agent registry federation. |
| Category | Observability & Evals |
| Stage | emerging |
| Why it matters | Connects agent registries with runtime evidence such as policy hashes, signed tool-call transcripts, and append-only audit records. |
| Future signal | Agent infrastructure may converge on portable evidence records that prove what policy and runtime were active during execution. |
| SandBase fit | observability / runtime / registry / governance |
| Integration potential | watch |
| Links | https://github.com/ards-project/ard-spec |
| Notes | Track issue #7. Do not comment until the normative wording draft lands or SandBase has a sharper session-level vs action-level receipt framing. |
