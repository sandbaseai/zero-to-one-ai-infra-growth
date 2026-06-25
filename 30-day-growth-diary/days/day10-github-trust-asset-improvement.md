# Day 10 — Early Brand Search Feedback and Continued Distribution

Date: 2026-06-21

Stage: Week 2 — Distribution and daily operations

Status: Completed

## Goal

Use the first visible brand-search feedback from Google to adjust the next distribution moves.

Yesterday's work started to show up externally:

- SandBase docs pages are visible in Google results.
- Peerlist is showing a `Posts by SandBase AI` result with the positioning line:

```text
SandBase AI. Agent infrastructure for developers building production AI agents.
```

This is an early sign that the external profile strategy is working.

## Planned Work

- Capture the Google result as an early evidence screenshot.
- Record the Peerlist indexing signal.
- Watch for incorrect third-party entity results and build stronger correct signals.
- Continue light social interaction around agent infrastructure topics.
- Continue one high-quality directory/profile target.
- Keep the technical SEO fixes moving: blog sitemap, future-dated posts, and brand entity consistency.

## Tools To Use

| Tool | Role |
|------|------|
| Codex | Record evidence, clarify strategy, prepare daily plan |
| Google Search | Brand result observation |
| Peerlist | External profile and indexed social surface |
| GitHub / Website / Blog | Correct entity signals and technical trust assets |

## Execution Log

- A Google search screenshot showed SandBase-owned or relevant results beginning to appear:
  - SandBase Docs result: `JavaScript / TypeScript SDK | SandBase Docs`
  - Peerlist result: `Posts by SandBase AI`
  - Peerlist snippet: `SandBase AI. Agent infrastructure for developers building production AI agents. 2 followers.`
- This confirms that the Day 9 Peerlist profile was not just a directory task. It created a crawlable, brand-relevant public surface.
- The screenshot also showed an unrelated / incorrect Tracxn result describing a different "SandBase" entity.
- Decision: do not panic about the incorrect result. Build stronger correct signals through:
  - official website pages
  - docs
  - blog articles
  - GitHub organization
  - LinkedIn company page
  - Peerlist profile
  - DevHunt / Uneed / Product Hunt profiles
  - Agent Ecosystem
  - Hackathon Support
- P0 SEO fixes were reported as completed by the user: blog sitemap, future-dated posts, and entity consistency.
- P0 SEO fixes were verified on production:
  - `sitemap-blog.xml` now includes 85 URLs, including individual English and Chinese article URLs.
  - the previously future-dated `n8n vs Dify` article now shows `June 20, 2026`.
  - no future-date matches were found on the blog listing for dates after June 21, 2026.
  - homepage title now reads `SandBase - Agent Infrastructure for Production AI Agents`.
  - homepage description now focuses on production agents, sandboxed runtime, tool access, model routing, cloud sandboxes, and unified APIs.
  - Organization JSON-LD now uses the correct entity links: X, GitHub `sandbaseai`, LinkedIn company page, Peerlist, and Discord.
  - `sitemap-pages.xml` includes the Agent Ecosystem and its individual project pages.
  - `Hackathon Support` is not yet visible in the production pages sitemap, so it should be checked again after that branch is deployed.
- Google Search Console sitemap follow-up:
  - the existing non-www sitemap index `https://sandbase.ai/sitemap-index.xml` is still valid and shows `Success`, last read on June 20, 2026, with 954 discovered pages.
  - submitted the canonical www sitemap index `https://www.sandbase.ai/sitemap-index.xml` on June 21, 2026.
  - GSC confirmed the submission, but the new www entry initially shows `Couldn't fetch` / unknown with 0 discovered pages.
  - Decision: keep both entries for now, treat the www entry as a fresh submission, and re-check tomorrow before making more changes.
- Directory/profile follow-up:
  - DevHunt was checked again. The submit path exists at `https://devhunt.org/login`, with GitHub and Google login options.
  - DevHunt Google login was completed by the user.
  - DevHunt auto-created a profile, so the visible fields were changed to SandBase company information:
    - full name: `SandBase AI`
    - username: `sandbaseai`
    - social URL: `https://www.linkedin.com/company/sandbaseai/`
    - bio: `SandBase AI builds agent infrastructure for developers building production AI agents: sandboxed runtime, safe tool access, model routing, APIs, and distributed compute.`
  - A new DevHunt tool draft form was opened and the SandBase product fields were prepared:
    - tool name: `SandBase`
    - slogan: `Agent infrastructure for production AI agents`
    - website: `https://www.sandbase.ai`
    - GitHub: `https://github.com/sandbaseai`
    - description: `SandBase is agent infrastructure for developers building production AI agents. It provides the runtime layer for agent apps: sandboxed execution, safe tool access, model routing, APIs, and distributed compute for agent workloads.`
  - DevHunt launch week options were checked. Available launch weeks showed `$49`, which is above the current $30 budget.
  - Decision: do not schedule or submit DevHunt today. Keep the prepared copy and revisit only if a free option appears or the budget decision changes.
  - Uneed was opened as the next directory target.
  - A SandBase product draft was created in Uneed's waiting-line editor.
  - Uneed generated an initial draft from the website, then the copy was adjusted to match SandBase's core positioning.
  - Current Uneed draft:
    - name: `SandBase`
    - slug: `sandbase`
    - URL: `https://www.sandbase.ai`
    - category: `Development`
    - pricing: `Freemium`
    - tags: `API & Data`, `AI`, `Development`
    - tagline: `Agent infrastructure for developers building production AI agents.`
  - The product draft was saved successfully. Uneed showed `Product updated`.
  - Preview mode was checked. The public-style preview correctly shows the SandBase logo, tagline, category, pricing, tags, and a website link with Uneed referral parameters.
  - No paid `Submit to 100+ directories` action was used.
  - No launch date was scheduled yet.
- LinkedIn company distribution follow-up:
  - A company-page post was prepared around the Uneed launch preparation and SandBase's production-agent positioning.
  - A supporting visual was generated with the local image-generation workflow in `scripts/generate-images-sandbase.py`.
  - Generated asset: `assets/generated-images/linkedin-uneed-agent-infra.png`.
  - The image was inserted into the LinkedIn company post manually.
  - The post copy was tightened before publishing so it reads as a product update, not an operations diary:
    - opening question: `What breaks first when AI agents move from demo to production?`
    - product context: `We are preparing SandBase for a small launch on Uneed.`
    - positioning: agent infrastructure for developers building production AI agents.
    - proof points: sandboxed runtime, safe tool access, model routing, distributed compute.
  - The post appeared in the LinkedIn company page published list.
- LinkedIn operational-account privacy cleanup:
  - The operating account is used for administration, but public activity should represent the company, not a private individual.
  - Privacy settings were reviewed and tightened where appropriate.
  - Principle: company channels can be public; operational account details should stay private and non-promotional.

## Links Created Or Updated

- Evidence screenshot: [Google brand result with Peerlist](../../assets/google-brand-result-peerlist-2026-06-21.png)
- LinkedIn social visual: [linkedin-uneed-agent-infra.png](../../assets/generated-images/linkedin-uneed-agent-infra.png)
- Peerlist profile/posts surface: https://peerlist.io/sandbase
- Uneed draft slug prepared: `sandbase`

## Questions / Blockers

- The incorrect Tracxn entity result may continue to appear until Google has stronger confidence in the new SandBase.ai entity.
- Need to re-check the newly submitted `https://www.sandbase.ai/sitemap-index.xml` in Google Search Console tomorrow.
- Need to re-check `Hackathon Support` after deployment and confirm it appears in `sitemap-pages.xml`.
- Need to continue producing correct third-party profile signals, not only website content.
- Need to decide whether to schedule the Uneed launch or keep it as a draft until launch assets are ready.
- Need to decide later whether DevHunt's $49 launch is worth doing. Current rule says no because it is above the $30 cap.

## Lesson

Early brand search results are not only about ranking. They are about entity formation.

The important signal from today:

```text
Google is starting to associate SandBase AI with "agent infrastructure for developers building production AI agents."
```

The next job is to make that association stronger and cleaner.

Do not chase every directory. Build a small number of high-trust surfaces that repeat the same positioning.

## Next Action

Today:

- Re-check the newly submitted www sitemap index in Google Search Console tomorrow.
- Do 2-3 light interactions on X / Peerlist around production agents.
- Decide whether Uneed should be scheduled now or held until launch assets are ready.
- Prepare a product-facing post around Agent Ecosystem or Hackathon Support.
