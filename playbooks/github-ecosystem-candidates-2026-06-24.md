# GitHub Ecosystem Candidates — 2026-06-24

Purpose: identify credible GitHub projects where SandBase can build relationships through useful technical interaction, not backlink spam.

Search scope:

```text
agent sandbox runtime
pushed after 2026-06-01
```

## Candidate Summary

| Project | Category | Fit | Interaction Status |
|---------|----------|-----|--------------------|
| `runseal-labs/runseal` | Sandbox runtime | High | No open issues; keep as probe target |
| `jeremylongshore/agent-governance-plane` | Governance / sandbox / HITL | Medium-high | Watch #84 / #114; do not comment unless there is concrete evidence |
| `leizd/deepseek` | Local-first agent infra | High | Commented on #15 |
| `WasmAgent/wasmagent-js` | Portable agent runtime | Medium-high | Candidate for compatibility checklist |
| `finogeeks/finsafe` | Runtime sandbox | Medium-high | Candidate for sandbox-runtime registry |
| `ros-claw/rosclaw` | Physical AI runtime infra | Medium | Good registry candidate, less immediate for sandbox probe |

## Completed Interaction

### `leizd/deepseek`

Issue: https://github.com/leizd/deepseek/issues/15

Topic: external MCP server bridging into the local Agent tool surface.

Why it fits:

- MCP tools
- local agent tool surface
- unified Tool Policy gate
- audit and SSRF boundaries
- direct overlap with SandBase's safe tool access positioning

Comment added:

- suggested splitting acceptance into `capability profile`, `policy decision`, and `audit trace`
- did not link SandBase
- kept the comment in Chinese to match the issue language

Comment URL:

```text
https://github.com/leizd/deepseek/issues/15#issuecomment-4786990208
```

## Candidate Notes

### `runseal-labs/runseal`

URL: https://github.com/runseal-labs/runseal

Fit:

- stable execution protocol
- sandbox levels
- network modes
- capability reporting
- audit events
- conformance tests

Current status:

- no open issues
- keep as the first target for `agent-sandbox-runtime-probe`
- do not open a low-effort issue until the probe has runnable or reviewable evidence

Next useful action:

- map the runtime compatibility checklist to Runseal capabilities and note gaps as observations, not claims.

### `jeremylongshore/agent-governance-plane`

URL: https://github.com/jeremylongshore/agent-governance-plane

Relevant issues / PRs:

- #84: model-only egress allowlist sandbox
- #114: Topology C egress-allowlist core

Fit:

- fail-closed egress design
- sandbox policy
- audit journal
- human-in-the-loop approval

Current status:

- the maintainer already has a detailed plan
- avoid generic comments

Next useful action:

- only comment later if SandBase can share a concrete compatibility checklist or external test case around egress allowlist behavior.

### `WasmAgent/wasmagent-js`

URL: https://github.com/WasmAgent/wasmagent-js

Description observed:

Portable agent runtime for browser, edge, and sandboxed kernels.

Fit:

- agent runtime
- browser / edge / sandboxed execution
- evaluation and rollout ranking

Next useful action:

- inspect README and examples
- decide whether it belongs in the registry as `Agent Runtimes`
- look for capability / isolation / audit surfaces

### `finogeeks/finsafe`

URL: https://github.com/finogeeks/finsafe

Description observed:

Runtime sandbox for AI agents.

Fit:

- sandbox runtime
- likely useful for comparing runtime boundaries

Next useful action:

- inspect README
- check whether issues are open
- classify as `Sandboxes & Computer Use` if technically credible

### `ros-claw/rosclaw`

URL: https://github.com/ros-claw/rosclaw

Description observed:

Runtime infrastructure for Physical AI and embodied agents with sandbox safety, capability routing, physical memory, runtime intervention, and skill evolution.

Fit:

- agent runtime
- physical AI / robotics
- sandbox safety
- capability routing

Next useful action:

- add to registry watchlist rather than immediate outreach
- useful as a broader ecosystem signal for embodied agents, not today's sandbox probe

## Operating Rule For GitHub Interaction

Only interact when one of these is true:

- we can answer a specific technical question
- we can suggest a concrete acceptance criterion
- we can share a small test case or checklist
- we can report a real bug found while trying the project

Do not comment only to create a backlink.
