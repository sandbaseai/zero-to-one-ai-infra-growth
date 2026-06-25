# Day 16 Runtime Control Plane Follow-up Pack

Date: 2026-06-25

Purpose: continue distribution after the LinkedIn company-page post without repeating the same wording everywhere.

## Published Anchor

LinkedIn company-page post:

```text
For production AI agents, sandboxing is not just a security checkbox.

It becomes part of the runtime control plane.
```

Media:

```text
assets/generated-images/day16-runtime-control-plane.png
```

Observed share id:

```text
urn:li:share:7475703355357663232
```

## X Short Post

```text
Production agents need a runtime control plane, not just a sandbox flag.

Useful questions:

- did the latest tool policy reach the executor?
- can the runtime prove the active policy version?
- are denied actions visible in audit logs?
- can a failed sandbox be cleaned up or replayed?

Sandboxing is useful when it is observable.
```

## X Reply Variant

Use this only under a concrete discussion about agent runtimes, tool permissions, or sandboxing:

```text
One runtime detail I keep coming back to:

"sandboxed" is not enough as a label.

For production agents, I want the runtime to prove which policy version was active, what was denied, and whether cleanup/replay worked after failure.
```

## Discord / Community Prompt

```text
Today's agent-runtime question:

For long-running or tool-using agents, what evidence would make you trust a sandbox boundary?

- active policy version
- denied action audit logs
- filesystem/network mode
- timeout and cleanup behavior
- replayable trace after failure

Curious which one matters most in real projects.
```

## GitHub Comment Candidate — Azure/kars #451

Issue:

```text
https://github.com/Azure/kars/issues/451
```

Context:

- title: `Controller: InferencePolicy/ToolPolicy watch goes stale on AKS — CR edits don't reach the ConfigMap without a controller restart`
- state: open
- comments: 0
- fit: high
- status: posted from GitHub account `denial123789`
- comment URL: https://github.com/Azure/kars/issues/451#issuecomment-4794762820

Comment:

```text
This is a useful failure mode to make explicit for agent-runtime operators.

For ToolPolicy / InferencePolicy style control planes, I would treat "policy freshness" as part of the runtime safety contract, not just a controller implementation detail.

One validation angle that may help: alongside the watch timeout / relist fix, add a small conformance case that records:

- CR generation observed by the controller
- compiled policy digest / ConfigMap resourceVersion
- max propagation time from policy edit to effective runtime config
- router/runtime acknowledgement of the new digest

That would make stale reflector behavior visible as a bounded freshness SLO instead of only surfacing through a restart workaround.
```

## GitHub Comment Candidate — ageos-runtime #24

Issue:

```text
https://github.com/ageos-labs/ageos-runtime/issues/24
```

Context:

- title: `Harden sandbox with seccomp`
- state: open
- comments: 0
- fit: medium-high
- status: posted from GitHub account `denial123789`
- comment URL: https://github.com/ageos-labs/ageos-runtime/issues/24#issuecomment-4795214437

Comment:

```text
For seccomp hardening, it may help to split validation into two tracks:

1. Positive path: the normal OpenClaw workflows still pass under the default profile.
2. Negative path: a few intentionally denied operations fail with structured, public-safe errors.

For agent runtimes, the negative path matters a lot because callers need to distinguish "tool failed" from "runtime policy denied this syscall / capability".

A small regression matrix could cover:

- basic file read/write inside the allowed workspace
- denied access outside the workspace
- process spawn behavior
- network behavior if the sandbox supports network modes
- timeout / cleanup after a denied or crashed process
```

## GitHub Watch Candidate — OpenSandbox #1120

Issue:

```text
https://github.com/opensandbox-group/OpenSandbox/issues/1120
```

Context:

- title: `java sdk windows wsl2 docker模式下NetworkPolicy参数传入会报错`
- state: open
- fit: high for network policy / sandbox runtime troubleshooting
- status: reviewed, not commented

Why skip today:

- maintainer already provided a strong diagnostic path
- reporter provided detailed logs after that response
- another comment now would likely duplicate the existing thread

Follow-up angle:

```text
Agent sandbox network policy needs a failure checklist:

- kernel module / iptables / nftables capability
- DNS redirect install result
- egress sidecar readiness and healthz
- port binding conflicts in Docker Desktop / WSL2
- structured error surfaced back to SDK callers
```

## GitHub Comment Candidate — OpenClaw #39685

Issue:

```text
https://github.com/openclaw/openclaw/issues/39685
```

Context:

- title: `[Feature]: Network Access Control (allowedDomains / denyDomains) — Egress Firewall`
- state: open
- labels include `enhancement`, `impact:security`, `needs-maintainer-review`, `needs-product-decision`, and `needs-security-review`
- fit: high for agent runtime egress policy and sandbox/network-control positioning
- status: reviewed through public GitHub API; browser posting attempted but GitHub page timed out twice

Suggested comment:

```text
This would be a strong control-plane boundary for agent web tools.

One acceptance angle that may help is to separate policy syntax from enforcement evidence. For example, alongside `allowedDomains` / `denyDomains`, I would want tests or runtime events that prove:

- deny rules win over allow rules, including wildcard matches
- host canonicalization happens before the decision, including redirects and CNAME-like resolution paths where applicable
- the existing SSRF protections still apply after domain allowlist checks
- invalid or unparsable policy config fails closed
- each denied request emits a structured, redacted audit event with the effective policy source/version
- successful requests can be tied back to the policy digest that allowed them

For agent runtimes, this makes the feature more than a config knob: operators can prove what egress policy was active for a specific tool call.
```

Next action:

- post manually or retry from the logged-in browser when GitHub pages are stable
- after posting, record the exact comment URL and recheck for maintainer response

## GitHub Watch Candidate — ARD spec #7

Issue:

```text
https://github.com/ards-project/ard-spec/issues/7
```

Context:

- title: `Proposal: TRACE-v0.2 runtime governance attestation type + governed-agent registry federation`
- state: open
- fit: medium-high for runtime evidence, attestation, and governed agent registry positioning
- status: reviewed; not commented because the thread is already deep and converging on normative wording

Possible future angle:

```text
Runtime governance records should distinguish session-level policy attestation from action-level tool-call receipts.
```

## Notes

- GitHub CLI was not logged in during this run.
- The in-app browser GitHub tab was later available and the `Azure/kars#451` comment was posted.
- The `ageos-runtime#24` seccomp validation comment was also posted later from the in-app browser.
- Peerlist profile was reachable in earlier passes, but the composer / DOM did not remain controllable; keep the drafted update for a manual or retry window.
