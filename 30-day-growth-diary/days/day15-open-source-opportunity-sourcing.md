# Day 15 — Open Source Opportunity Sourcing

Date: 2026-06-24

Stage: Week 3 — ecosystem building and repeatable distribution

Status: Completed

## Goal

Turn daily open-source discovery into a repeatable habit: find 3 candidate projects, score them, choose 1, and record why.

## Planned Work

- Check search / site health quickly.
- Find 3 new open-source opportunities around agent infrastructure.
- Score them with buildability and SandBase fit in mind.
- Pick 1 to build later.
- Do one real community interaction around a credible project.

## Tools To Use

| Tool | Role |
|------|------|
| GitHub | Source of candidate projects |
| Codex | Scoring, notes, and decision log |
| Peerlist / X / Discord | Community context and reaction signals |
| Registry playbook | Filter for quality and future signal |

## Execution Log

- Daily channel sweep scope was clarified:
  - X
  - LinkedIn
  - Discord
  - Peerlist
  - DevHunt
  - already registered backlink/profile surfaces
  - new backlink and open-source opportunities
- X daily operation:
  - Replied to a discussion about Vercel `eve` and the "agent as a directory of files" model.
  - Added the production runtime perspective: beyond file conventions, agents need inspectable runtime assets such as permissions, environment config, tool traces, approvals, logs, and replay data.
  - Replied to a real infrastructure question about building a cluster for coding and agentic applications.
  - Suggested separating compute into two pools:
    - GPU-heavy inference
    - CPU / isolation-heavy sandbox execution
  - Published one SandBase opinion post:

```text
Production agents do not only need model inference.

They need two kinds of compute:

- GPU compute for reasoning
- isolated CPU/runtime compute for tools, browser sessions, shell commands, and files

The agent runtime is where those two worlds meet.
```
- X notification check:
  - No replies or mentions needed a response.
  - Yesterday's agent runtime reply received a like, which is a useful early signal that technical replies can create lightweight visibility without hard promotion.
- LinkedIn company page check:
  - Company page is healthy and visible.
  - Observed 3 followers, 8 search appearances, and 1 new follower.
  - No comment thread required a response.
  - Profile completion suggestions remain: add company location and validate a company email domain.
- Discord check:
  - Checked `#agent-runtime` and `#builder-chat`.
  - No new member questions or replies needed a response.
  - Removed an old draft from the input box to avoid accidental posting.
  - Decision: no forced Discord update today unless there is a real product or community prompt.
- Peerlist check:
  - Checked notifications and found a real reply from a builder around permission boundaries, memory lifecycle, and scoped agent capabilities.
  - Replied with a product-relevant comment:

```text
That would be a strong demo. Showing when memory is created, scoped, updated, or denied would make the permission model much easier to evaluate.
```

  - This is the right interaction pattern for early-stage distribution: contribute a useful lens, do not paste a link.
- DevHunt check:
  - Tool submission page is available.
  - Launch weeks are still priced at $49.
  - Since the current directory budget is under $30, DevHunt remains "watch only" for now.
- External-link progress:
  - Uneed draft was re-checked.
  - Current draft is still intact:
    - name: `SandBase`
    - URL: `https://www.sandbase.ai`
    - category: `Development`
    - pricing: `Freemium`
    - tags: `API & Data`, `AI`, `Development`
    - tagline: `Agent infrastructure for developers building production AI agents.`
  - Uneed now shows `Schedule your launch`, which is a public scheduling action. Do not click it without explicit confirmation.
  - After confirmation, SandBase was added to the free Uneed waiting line.
  - Public Uneed page is live:
    - URL: `https://www.uneed.best/tool/sandbase`
    - launch date: November 9, 2026
    - cost: free
    - paid upsell skipped: `Auto-Submit to 100+ directories ($249)`
  - Peerlist Launchpad was re-checked. The current week page is accessible, but the `Launch` button still does not open a usable submission form in this browser session.
  - AlternativeTo and SaaSHub submit pages were checked and both showed bot-protection / "Just a moment" states, so they were not counted as completed actions.
  - Product Hunt submit was checked but also showed a bot-protection / "Just a moment" state, so it was not counted.
  - Created a public GitHub organization profile asset:
    - repository: `https://github.com/sandbaseai/.github`
    - profile README: `https://github.com/sandbaseai/.github/tree/main/profile`
    - organization page: `https://github.com/sandbaseai`
  - The GitHub organization README now links to the website, docs, blog, X, LinkedIn, Discord, Uneed launch page, and open resource repositories.
  - This counts as a stronger developer-trust asset than another generic directory listing.
- Additional backlink candidate sweep:
  - BetaList:
    - URL checked: `https://betalist.com/submit`
    - result: redirects to sign-in
    - status: keep as a candidate after login
    - fit: decent startup discovery surface, but less developer-specific than Peerlist
  - Indie Hackers:
    - URL checked: `https://www.indiehackers.com/products/new`
    - result: redirects to sign-in
    - status: keep as a candidate after login
    - fit: good for a product/story page if the copy stays founder/product-led rather than SEO-led
  - Fazier:
    - URL checked: `https://fazier.com/launch`
    - result: accessible
    - status: candidate for a future launch submission after sign-in
    - fit: product discovery surface with some AI-agent products, but quality is mixed
  - Product Hunt:
    - URL checked: `https://www.producthunt.com/posts/new`
    - result: bot-protection page
    - status: wait; do not force today
  - TAIFT:
    - URL checked: `https://theresanaiforthat.com/submit/`
    - result: bot-protection page
    - status: wait; broad AI directory, use carefully
  - AlternativeTo, SaaSHub, OpenHub, Launching Next, Startup Buffer:
    - result: blocked by bot-protection or not usable in this session
    - status: not counted
  - Microlaunch:
    - result: redirected to premium/pricing
    - status: not a priority today
  - StackShare:
    - result: `/submit` path did not behave like a clean product submission flow
    - status: not counted
  - GitHub organization profile:
    - result: verified live and showing the new public README
    - public repositories were pinned on the organization profile:
      - `awesome-native-agent-platforms`
      - `agent-sandbox-cookbook`
      - `.github`
      - `zero-to-one-ai-infra-growth`
    - result: the GitHub organization page now works as a stronger developer-trust surface, not just an empty org shell.
  - DEV Community:
    - profile created and verified: `https://dev.to/sandbaseai`
    - display name: `SandBase AI`
    - website: `https://www.sandbase.ai`
    - bio: `Agent infrastructure for developers building production AI agents.`
    - location: `Remote`
    - work: `Agent infrastructure at SandBase AI`
    - followed relevant technical tags:
      - `ai`
      - `python`
      - `opensource`
      - `devops`
      - `machinelearning`
      - `security`
      - `typescript`
      - `go`
      - `docker`
      - `kubernetes`
      - `rag`
      - `langchain`
    - declined newsletter subscription.
    - result: this is a useful developer-community profile and a future publishing surface for technical articles.
  - DEV Community technical article publication:
    - Converted the SandBase blog post `Why Production AI Agents Need a Runtime Layer` into a DEV.to-native version.
    - Conversion strategy:
      - Keep the technical thread around `agent runtime`, `durable state`, `sandboxed execution`, `resource limits`, and `lifecycle`.
      - Reduce site-internal SEO structure and product-pitch density.
      - Mention SandBase at the end as building context instead of opening with promotion.
    - DEV.to draft title: `Production AI Agents Need a Runtime Layer`
    - Tags: `ai`, `architecture`, `security`
    - Canonical URL set to the original SandBase article:
      - `https://www.sandbase.ai/blog/production-ai-agents-need-a-runtime-layer/`
    - Status: published.
    - Published URL:
      - `https://dev.to/sandbaseai/production-ai-agents-need-a-runtime-layer-2o2a`
    - Local draft file:
      - `30-day-growth-diary/drafts/devto-production-ai-agents-runtime-layer.md`
  - Post-publication distribution:
    - X:
      - Published a short opinion post from the SandBaseAI account.
      - Focus: production agents need a runtime layer, not only a framework.
      - Main points: durable state, sandboxed tool execution, resource limits, lifecycle control.
      - URL: `https://x.com/SandbaseAI/status/2068948735107994092`
    - LinkedIn:
      - Published a longer company-page version from SandBaseAI.
      - Tone: B2B / infrastructure, centered on the difference between framework and runtime.
    - Discord:
      - Posted a lightweight community update in `#agent-runtime`.
      - Framed as a feedback invitation for builders working on long-running or tool-using agents, not a hard promotion.
  - Fazier:
    - URL checked: `https://fazier.com/submit`
    - result: pricing and submission rules inspected
    - Basic: free, but requires adding a Fazier backlink badge on the SandBase homepage or footer
    - Lite: $19, no backlink required, within the $30 budget
    - Premium: $39, above the current budget
    - decision: skip for now; the channel is mixed quality and not developer-infrastructure specific enough to justify even a small paid experiment today
  - BetaList:
    - private submission draft created
    - copy rewritten to avoid overclaims and keep the agent infrastructure positioning clear
    - topics adjusted toward `Infrastructure`, `API Integration`, and `Observability`
    - package page reached
    - lowest package: Lite $39
    - decision: do not submit because it is above the $30 channel budget
  - Indie Hackers:
    - profile created: `https://www.indiehackers.com/sandbaseai`
    - product section was attempted, but the editor did not reliably persist the product fields to the public profile
    - decision: keep as a created profile / follow-up candidate, but do not count as a completed external link yet
- Open-source opportunity sourcing:
  - GitHub search for the exact phrase `agent runtime sandbox tool calling` returned no repository matches but many code matches, which suggests the opportunity is in examples and adapters rather than a mature category name.
  - Broader GitHub search for `AI agent sandbox` returned fresh projects updated today.
  - Three candidates were shortlisted:
    - `jeremylongshore/agent-governance-plane`: Slack-native governance for AI coding agents, sandboxed execution, approval on every tool call, signed audit logs.
    - `runseal-labs/runseal`: OS-native sandbox layer and stable execution protocol for AI agents.
    - `blissito/sandbox-host`: self-hosted Firecracker microVM platform for AI agent sandboxes and MCP-style sandbox tools.
  - Recommended pick for later build: `runseal-labs/runseal`, because it maps directly to SandBase's sandbox/runtime positioning and can be turned into a small checklist or probe project without becoming too large.
- Day 15 continuation on 2026-06-24:
  - Treated the repository task list as the source of truth and continued from the Day 15 open-source opportunity sourcing thread.
  - Re-checked candidate status through the GitHub API:
    - `runseal-labs/runseal` is public, Apache-2.0, Rust, and was pushed on 2026-06-24.
    - `jeremylongshore/agent-governance-plane` is public, Apache-2.0, TypeScript, active on 2026-06-24, and has 5 open issues.
    - `blissito/sandbox-host` now returns 404 through the GitHub API, so it should not remain an active Day 15 candidate unless the repository becomes public again.
  - Downloaded the active external candidates into the local workspace for inspection:
    - `work/external-candidates/runseal`
    - `work/external-candidates/agent-governance-plane`
  - Read the Runseal README and confirmed the strongest SandBase-aligned surfaces:
    - stable execution protocol
    - `runseal exec --json`
    - `runseal exec --events`
    - JSON-RPC stdio
    - service stdio
    - `getCapabilities`
    - `getSetupStatus`
    - execution and audit event APIs
    - black-box conformance tests
  - Read the AGP README and confirmed it is valuable but heavier for Day 15 because it focuses on governance, Slack HITL approval, signed audit journals, Docker sandboxing, and multi-harness control.
  - Decision:
    - keep Runseal as the Day 15 pick
    - treat AGP as a future governance/HITL research candidate
    - drop `sandbox-host` from the active set for now
  - Created a Day 15 follow-up brief:
    - `playbooks/runseal-compatibility-probe.md`
  - Proposed first build asset:
    - `agent-sandbox-runtime-probe`
    - a neutral compatibility checklist and probe case set for agent sandbox runtimes
    - no hard SandBase promotion until the asset has standalone developer value
  - Started the first local draft of the proposed asset:
    - `work/sandbaseai/agent-sandbox-runtime-probe/README.md`
    - `work/sandbaseai/agent-sandbox-runtime-probe/checklists/runtime-compatibility.md`
    - `work/sandbaseai/agent-sandbox-runtime-probe/cases/sandbox-runtime-probe.json`
    - `work/sandbaseai/agent-sandbox-runtime-probe/notes/runseal-observations.md`
  - Added an API-generated article header image for the runtime checklist draft:
    - article: `30-day-growth-diary/drafts/agent-sandbox-runtime-compatibility-checklist.md`
    - generated PNG: `assets/generated-images/agent-sandbox-runtime-checklist.png`
    - source generator: `scripts/generate-images-sandbase.py`
    - local SVG fallback also exists at `assets/social-cards/agent-sandbox-runtime-checklist.svg`, but the article uses the API-generated PNG.
  - Added a SandBase image API prompt to `scripts/generate-images-sandbase.py` for `agent-sandbox-runtime-checklist`.
    - API run submitted: `7c42b29b-7643-4fa5-bc22-70316ccd003f`
    - result: completed and saved as `assets/generated-images/agent-sandbox-runtime-checklist.png`
  - Validated the probe case JSON locally.
- Social maintenance continuation on 2026-06-24:
  - X notifications:
    - Ignored low-signal unrelated reply chains.
    - Replied to a real community question from `@zatdex55` about what kind of community "alpha" can shape the roadmap beyond bug reports.
    - Reply angle: SandBase wants signal around permission boundaries, hard-to-debug tool/runtime failures, and traces or approvals that make production agents trustworthy.
  - X build note:
    - Published a Day 15 build note about turning agent sandbox research into a runtime compatibility probe.
    - URL: `https://x.com/SandbaseAI/status/2069684761078194345`
  - DEV Community:
    - Checked notifications.
    - No comments required a reply.
    - Article received a like from Dimitris Kyrkos.
    - Account received the `Writing Debut` badge.
  - LinkedIn company page:
    - Checked admin dashboard.
    - Page status: 3 followers, 8 search appearances, 1 new follower, 392 post impressions, 8 page visitors.
    - Page activity notifications showed 0 new page notifications.
    - Published a LinkedIn company update about the Day 15 runtime compatibility probe direction.
  - Discord:
    - Attempted to open the SandBaseAI server from the browser session.
    - The Discord page repeatedly caused browser-control timeouts, so no Discord message was posted.
    - Decision: do not force Discord interaction today without reliable page state.
- Additional social maintenance continuation on 2026-06-24:
  - X search:
    - Searched latest posts around `agent runtime` and `AI agent sandbox`.
    - Found a relevant post from `@rishflips` about defining a strict contract before giving an AI agent sandbox access.
    - Replied with two production-runtime additions:
      - capability discovery before execution
      - audit shape after a tool call fails or is denied
    - Kept the reply technical and did not include a SandBase link.
  - Peerlist:
    - Attempted to open notifications.
    - The page caused another browser-control timeout, so no Peerlist interaction was completed in this pass.
    - Decision: retry later from a stable browser session instead of forcing it.
- Content and GitHub continuation on 2026-06-24:
  - Wrote a new technical article draft:
    - `30-day-growth-diary/drafts/agent-sandbox-runtime-compatibility-checklist.md`
    - working title: `A Practical Checklist for AI Agent Sandbox Runtimes`
    - angle: sandboxing should become observable runtime behavior, not a vague security label
    - includes capability discovery, filesystem boundaries, network boundaries, lifecycle, audit/trace, integration surface, and operational fit
  - Attempted to publish the article to DEV Community.
    - DEV editor opened.
    - Uploaded the SandBase API-generated PNG through the DEV editor so the public article uses a DEV-hosted image URL.
    - Published URL: `https://dev.to/sandbaseai/a-practical-checklist-for-ai-agent-sandbox-runtimes-4m58`
    - Tags: `ai`, `security`, `opensource`, `architecture`
  - Prepared follow-up distribution copy:
    - `30-day-growth-diary/drafts/runtime-checklist-distribution-copy.md`
    - channels: X, LinkedIn, Discord/community, Peerlist
  - Attempted direct browser distribution after publishing:
    - X intent / compose page repeatedly timed out or failed to retain the tab in the in-app browser session.
    - LinkedIn company admin page also failed to begin navigation in the in-app browser session.
    - Decision: do not force posting through unstable browser automation; use the saved copy for a later stable browser pass or screen-control handoff.
  - User asked to retry specifically with the built-in browser.
    - The built-in browser reached an owned X compose tab, but X page inspection, screenshot capture, `tweetButton` lookup, keyboard submit, and prefilled intent navigation all timed out or remained stuck at `https://x.com/compose/post`.
    - Chrome screen-control was intentionally stopped after the user clarified to use the built-in browser.
  - X article distribution:
    - The user manually published the X post from the prepared short copy after the built-in browser automation became unreliable.
    - Status: completed manually.
    - Tweet URL: not captured in this session.
  - Discord article distribution:
    - The built-in browser reached the SandBaseAI Discord channel at `https://discord.com/channels/1516741633310199818/1516742498888843375`.
    - The user confirmed the Discord post appeared to have been sent.
    - Status: completed manually / visually confirmed by user.
    - Message URL: not captured in this session.
  - LinkedIn / Peerlist continuation:
    - Attempted to navigate from the built-in browser Discord tab to LinkedIn company admin and Peerlist.
    - Both attempts remained on the Discord channel URL and did not complete navigation.
    - Status: pending manual publishing from saved copy.
  - GitHub ecosystem search:
    - searched recent projects around `agent sandbox runtime`
    - discovered / reviewed candidates:
      - `WasmAgent/wasmagent-js`
      - `leizd/deepseek`
      - `finogeeks/finsafe`
      - `ros-claw/rosclaw`
      - `runseal-labs/runseal`
      - `jeremylongshore/agent-governance-plane`
  - GitHub interaction:
    - commented on `leizd/deepseek` issue #15 about external MCP server bridging into the local Agent tool surface
    - comment suggested splitting acceptance into:
      - capability profile
      - policy decision
      - audit trace
    - comment was written in Chinese to match the issue language
    - no SandBase link was included
    - comment URL: `https://github.com/leizd/deepseek/issues/15#issuecomment-4786990208`
  - Backlink / ecosystem candidate asset:
    - created `playbooks/github-ecosystem-candidates-2026-06-24.md`
    - linked it from `playbooks/emerging-agent-infrastructure-registry.md`
    - decision: prioritize GitHub ecosystem relationship-building over weak directory links

## Links Created Or Updated

- X opinion post: https://x.com/SandbaseAI/status/2068866907579847023
- Peerlist discussion reply: https://peerlist.io/scroll/post/ACTHKKD9EGGK77GDN1LQ6KJNBPMPRB
- Uneed public launch page: https://www.uneed.best/tool/sandbase
- GitHub organization profile: https://github.com/sandbaseai
- GitHub organization README repository: https://github.com/sandbaseai/.github
- DEV Community profile: https://dev.to/sandbaseai
- DEV Community published article: https://dev.to/sandbaseai/production-ai-agents-need-a-runtime-layer-2o2a
- DEV Community published article: https://dev.to/sandbaseai/a-practical-checklist-for-ai-agent-sandbox-runtimes-4m58
- X distribution post: https://x.com/SandbaseAI/status/2068948735107994092
- X article distribution post: completed manually; URL not captured
- Discord article distribution post: completed manually; URL not captured
- Discord distribution: posted in the public `#agent-runtime` community channel
- X Day 15 build note: https://x.com/SandbaseAI/status/2069684761078194345
- LinkedIn Day 15 company update: published from the SandBaseAI company page
- Candidate: BetaList submit page: https://betalist.com/submit
- Candidate: Indie Hackers product page: https://www.indiehackers.com/products/new
- Candidate: Fazier launch page: https://fazier.com/launch
- Indie Hackers profile created: https://www.indiehackers.com/sandbaseai
- BetaList draft prepared privately
- GitHub candidate search: https://github.com/search?q=AI+agent+sandbox&type=repositories&s=updated&o=desc
- Candidate: https://github.com/jeremylongshore/agent-governance-plane
- Candidate: https://github.com/runseal-labs/runseal
- Candidate: https://github.com/blissito/sandbox-host
- Runseal compatibility probe brief: ../../../playbooks/runseal-compatibility-probe.md
- Local draft asset: ../../../agent-sandbox-runtime-probe/
- Article draft: ../drafts/agent-sandbox-runtime-compatibility-checklist.md
- Distribution copy: ../drafts/runtime-checklist-distribution-copy.md
- GitHub comment on `leizd/deepseek` #15: https://github.com/leizd/deepseek/issues/15#issuecomment-4786990208
- GitHub ecosystem candidate batch: ../../../playbooks/github-ecosystem-candidates-2026-06-24.md

## Questions / Blockers

- Uneed is scheduled in the free waiting line.
- GitHub organization profile README is live.
- Peerlist Launchpad is still blocked by UI / account state.
- DevHunt is not a fit today because the launch cost is above the current budget.
- `blissito/sandbox-host` returned 404 on 2026-06-24 and should be treated as unavailable until it is public again.
- No public GitHub issue, pull request, or community reply was made for Runseal today. The next interaction should wait until SandBase has a concrete compatibility probe or checklist to share.

## Lesson

Early community distribution should prioritize useful technical replies over generic promotion. A small but real interaction on Peerlist is more valuable than posting the SandBase link into every thread.

Directory work should not be forced. If the submit page is blocked, expensive, or pushes SandBase into a generic AI-tool category, skip it and preserve positioning. A GitHub organization README can be a better external trust asset than another weak product directory.

For Week 3, the better move is to turn ecosystem discovery into small useful assets. Runseal is a good first target because its protocol, capabilities, execution, and audit surfaces make the sandbox-runtime evaluation problem concrete.

## Next Action

Continue `agent-sandbox-runtime-probe` as the small neutral asset for Day 15:

- refine the runtime compatibility checklist
- refine JSON probe cases
- add a simple CLI harness only after the cases are stable
- only then decide whether to share the result with the Runseal maintainer or community

Open-source discovery is most useful when it produces one buildable next step. Today's best project direction is a small agent sandbox capability checklist / probe, inspired by the `runseal` direction.

## Follow-up Queue

For the next backlink batch, prioritize:

1. Indie Hackers product page after login.
2. BetaList if the pricing / review path is acceptable.
3. Fazier if the submission flow is free or reasonably priced.
4. Product Hunt only after launch assets and reply plan are ready.

After today's follow-up, revise the order:

1. Fix or retry Indie Hackers product persistence later.
2. Keep BetaList only if the budget rule changes above $39.
3. Keep Fazier as a low-priority paid experiment, not a core backlink channel.
4. Continue improving GitHub developer assets because they have higher trust fit for SandBase.
5. Use DEV Community for one technical article when the next agent runtime or sandbox post is ready.
