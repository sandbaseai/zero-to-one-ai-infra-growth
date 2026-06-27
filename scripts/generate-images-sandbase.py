#!/usr/bin/env python3
"""Generate social cards through the SandBase run API.

Usage:
  SANDBASE_API_KEY=... python scripts/generate-images-sandbase.py

The script never prints the API key. It saves returned image URLs or base64
payloads under assets/generated-images/.
"""

from __future__ import annotations

import base64
import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError


BASE = os.environ.get("SANDBASE_API_BASE", "https://api.sandbase.ai/v1")
API_KEY = os.environ.get("SANDBASE_API_KEY")
OUT_DIR = Path("assets/generated-images")


CARDS = [
    (
        "week01-foundation",
        "Create a polished 1600x900 social media infographic for X and LinkedIn. "
        "Text: 'Week 1: Trust Foundation' and 'Before growth, build something real to point to.' "
        "Show seven connected blocks around a central SandBase node: SEO, Search Console, Blog, X, Discord, LinkedIn, GitHub. "
        "Style: clean technical editorial, off-white background, black text, teal accents, subtle grid, large readable typography, no tiny text, no real platform logos.",
    ),
    (
        "day01-seo-crawlability",
        "Create a polished 1600x900 social media infographic. "
        "Text: 'Day 1: Can Google See the Site?' and 'Before content, fix crawlability.' "
        "Show a simple flow: Browser = 200, Googlebot = 404, Fix crawler fallback. "
        "Style: clean technical editorial, off-white background, black text, teal accents, large readable typography, no tiny text.",
    ),
    (
        "day02-verification",
        "Create a polished 1600x900 social media infographic. "
        "Text: 'Day 2: Verification Is Growth Work' and 'Do not ask Google to index a broken page.' "
        "Show a checklist: Googlebot 200, Canonical host, Sitemap OK, Search Console ready. "
        "Style: clean checklist dashboard, off-white background, teal checkmarks, large readable typography, no tiny text.",
    ),
    (
        "day03-x-build-signal",
        "Create a polished 1600x900 social media infographic. "
        "Text: 'Day 3: X as a Build Signal' and 'One clear post beats link spam.' "
        "Show a setup path: Logo, Bio, Website, First post, Daily build note. "
        "Style: abstract setup diagram, no realistic social profile, no handles, no URLs, no fake names, no real X logo, off-white background, black text, teal accents, large readable typography. "
        "Only render the exact requested text and the five setup labels.",
    ),
    (
        "day04-discord-community",
        "Create a polished 1600x900 social media infographic. "
        "Text: 'Day 4: Discord as Product Infrastructure' and 'Small and clear beats big and empty.' "
        "Show four community paths: Start here, Quickstart, Ask for help, Report bugs. "
        "Style: clean community map without real Discord logo, off-white background, black text, teal accents, large readable typography.",
    ),
    (
        "day05-linkedin-trust",
        "Create a polished 1600x900 social media infographic. "
        "Text: 'Day 5: LinkedIn Builds B2B Trust' and 'A company page is a credibility object.' "
        "Show a company profile card connected to Website, About, First post, Company author. "
        "Style: abstract B2B company-page diagram without realistic company names, no fake company profile, no employee counts, no locations, no URLs, no real LinkedIn logo, off-white background, black text, teal accents, large readable typography. "
        "Only render the exact requested text and the four labels: Website, About, First post, Company author.",
    ),
    (
        "day06-blog-system",
        "Create a polished 1600x900 social media infographic. "
        "Text: 'Day 6: Blog as Content Infrastructure' and 'The website explains the product. The blog explains the category.' "
        "Show a blog engine connected to Markdown, RSS, Sitemap, JSON-LD, Topic clusters. "
        "Style: technical content system diagram, off-white background, muted gray panels, teal accents, large readable typography.",
    ),
    (
        "day07-trust-system",
        "Create a polished 1600x900 social media infographic. "
        "Text: 'Day 7: Connect the Trust System' and 'Website + Blog + GitHub + Community tell one story.' "
        "Show SandBase in the center connected to Website, Blog clusters, GitHub repo, Discord feedback, LinkedIn, X. "
        "Style: abstract network diagram, no fake URLs, no domains, no handles, no made-up taglines, no real platform logos, off-white background, black text, teal connector lines, large readable typography. "
        "Only render the exact requested text and the six labels: Website, Blog clusters, GitHub repo, Discord feedback, LinkedIn, X.",
    ),
    (
        "day08-distribution",
        "Create a polished 1600x900 social media infographic. "
        "Text: 'Day 8: Distribution After Trust' and 'Fewer, better placements beat link dumping.' "
        "Show a central SandBase trust asset connected to Dev.to, Directories, GitHub, Communities, LinkedIn, X. "
        "Style: clean distribution map, no real platform logos, no fake URLs, no handles, no made-up metrics, off-white background, black text, teal connector lines, large readable typography. "
        "Only render the exact requested text and the six labels: Dev.to, Directories, GitHub, Communities, LinkedIn, X.",
    ),
    (
        "week02-distribution",
        "Create a polished 1600x900 README and social media infographic for a public AI infrastructure cold-start case study. "
        "Text: 'Week 2: Distribution System' and 'Turn trust assets into discoverable surfaces.' "
        "Show a clean distribution hub connected to six readable nodes: Dev.to, Directories, GitHub, X, LinkedIn, Discord. "
        "Use a small secondary line: 'Context beats link dumping.' "
        "Style: calm technical editorial, off-white background, black text, muted gray panels, teal accents, subtle grid, professional README image, large readable typography. "
        "Use plain text labels and simple generic line icons only. Do not draw any real platform logo marks, app icons, brand glyphs, or trademark-like symbols. "
        "Avoid: tiny text, fake dashboards, fake metrics, private account data, emails, tokens, real platform logos, stock-photo people, cartoon mascots, neon cyberpunk, excessive gradients, hype claims, misspellings.",
    ),
    (
        "week03-open-source-growth-base",
        "Create a polished 1600x900 README and social media infographic for an open-source AI infrastructure growth case study. "
        "Text: 'Week 3: Open-Source Growth Base' and 'Map the ecosystem before asking for attention.' "
        "Show Awesome Agent Runtime as the central open-source asset connected to five readable nodes: 500 Projects, Runtime Stack, Sandbox Cluster, MCP Tools, Maintainer Outreach. "
        "Use a small secondary line: 'Useful maps create permission to participate.' "
        "Style: calm technical editorial, off-white background, black text, muted gray panels, teal accents, subtle grid, professional GitHub README image, large readable typography. "
        "Avoid: tiny text, fake dashboards, fake metrics, private account data, emails, tokens, real platform logos, stock-photo people, cartoon mascots, neon cyberpunk, excessive gradients, hype claims, misspellings.",
    ),
    (
        "week04-launch-readiness-recap",
        "Create a polished 1600x900 README and social media infographic for a 30-day AI infrastructure cold-start recap. "
        "Text: 'Week 4: Launch Readiness & Recap' and 'Package the proof, then decide what to amplify.' "
        "Show a clean launch-readiness board with six readable checks: Positioning, Website Trust, Public Assets, Metrics, Case Study, Next 30 Days. "
        "Use a small secondary line: 'Polish the proof before the push.' "
        "Style: calm technical editorial, off-white background, black text, muted gray panels, teal accents, subtle grid, professional README image, large readable typography. "
        "Avoid: tiny text, fake dashboards, fake metrics, private account data, emails, tokens, real platform logos, stock-photo people, cartoon mascots, neon cyberpunk, excessive gradients, hype claims, misspellings.",
    ),
    (
        "linkedin-uneed-agent-infra",
        "Create a polished 1600x900 LinkedIn social media infographic for a B2B developer infrastructure company. "
        "Text: 'Agent Infrastructure for Production AI Agents' and 'From demos to reliable systems.' "
        "Show a clean architecture diagram with three layers: Agent Apps, SandBase Infrastructure, Production Systems. "
        "Under SandBase Infrastructure, show five readable capability blocks: Sandboxed Runtime, Safe Tool Access, Model Routing, APIs, Distributed Compute. "
        "Add a small question at the bottom: 'What breaks first when agents move to production?' "
        "Style: calm technical editorial, off-white background, black text, muted gray panels, teal accents, subtle grid, professional LinkedIn-ready design, large readable typography. "
        "Avoid: tiny text, fake dashboards, private data, real platform logos, stock-photo people, cartoon mascots, neon cyberpunk, excessive gradients, hype claims, misspellings.",
    ),
    (
        "agent-sandbox-runtime-checklist",
        "Create a polished 1600x900 editorial infographic for a B2B developer infrastructure article. "
        "Text: 'Agent Sandbox Runtime Checklist' and 'Before, during, and after execution.' "
        "Show a clean technical diagram with three horizontal stages: Before Execution, During Execution, After Execution. "
        "Under the stages, include six readable nodes: Capabilities, Filesystem, Network, Lifecycle, Audit, Integration. "
        "Use subtle connections between stages to imply runtime verification. "
        "Style: calm technical editorial, off-white background, black text, muted gray panels, teal accents, subtle grid, professional article header image, large readable typography. "
        "Avoid: tiny text, fake dashboards, fake metrics, real platform logos, stock-photo people, cartoon mascots, neon cyberpunk, excessive gradients, hype claims, misspellings.",
    ),
    (
        "day16-runtime-control-plane",
        "Create a polished 1600x900 LinkedIn infographic for a B2B developer infrastructure company. "
        "Text: 'Runtime Control Plane' and 'Sandboxing is useful when it is observable.' "
        "Show a clean technical architecture diagram with a central Agent Runtime box connected to four readable control-plane signals: Policy Version, Sandbox Boundary, Audit Trace, Cleanup & Replay. "
        "Add a subtle lower caption: 'Before execution. During execution. After failure.' "
        "Style: calm technical editorial, off-white background, black text, muted gray panels, teal accents, subtle grid, professional LinkedIn-ready design, large readable typography. "
        "Avoid: tiny text, fake dashboards, fake metrics, real platform logos, stock-photo people, cartoon mascots, neon cyberpunk, excessive gradients, hype claims, misspellings.",
    ),
    (
        "day18-500-agent-runtime-map",
        "Create a polished 1600x900 LinkedIn and X infographic for a B2B developer infrastructure company. "
        "Text: '500 AI Agent Infrastructure Projects' and 'A map of the production agent stack.' "
        "Show a clean radial or layered technical map with ten readable category labels: Agent Runtime, Execution Sandbox, Browser Automation, Tool Protocol, App Integrations, Memory/Context, Safety/Evals, Model Gateway, Observability, Deployment/Compute. "
        "Place 'Awesome Agent Runtime' as the central title node and include a small footer: 'github.com/sandbaseai/awesome-agent-runtime'. "
        "Style: calm technical editorial, off-white background, black text, muted gray panels, teal accents, subtle grid, professional open-source announcement image, large readable typography. "
        "Avoid: tiny text, fake dashboards, fake metrics, real platform logos, stock-photo people, cartoon mascots, neon cyberpunk, excessive gradients, hype claims, misspellings.",
    ),
    (
        "day20-cold-start-progress-report",
        "Create a polished 1600x900 README hero image for a public case study about an AI infrastructure startup cold start. "
        "Text: 'SandBase.ai Cold-Start Progress' and 'Day 1-20: from invisible to developer-facing trust surface.' "
        "Show a clean journey map from Invisible Product to Public Trust Layer to Open-Source Growth Base. "
        "Include five readable signal nodes: Website, GitHub, Technical Content, Social Channels, Community. "
        "Do not add any footer sentence or extra explanatory body text beyond the requested title, subtitle, journey labels, and signal node labels. "
        "Style: calm technical editorial, off-white background, black text, muted gray panels, teal accents, subtle grid, professional GitHub README image, large readable typography. "
        "Avoid: tiny text, fake dashboards, fake metrics, private account data, emails, tokens, real platform logos, stock-photo people, cartoon mascots, neon cyberpunk, excessive gradients, hype claims, misspellings.",
    ),
    (
        "open-source-growth-flywheel",
        "Create a polished 1600x900 infographic for an open-source AI infrastructure growth flywheel. "
        "Text: 'Open-Source Growth Flywheel' and 'Map the ecosystem. Help maintainers. Earn trust.' "
        "Show a circular flywheel with six readable stages: Research, Curate, Publish, Invite Corrections, Improve Descriptions, Compound Trust. "
        "Place 'Awesome Agent Runtime' in the center. "
        "Style: calm technical editorial, off-white background, black text, muted gray panels, teal accents, subtle grid, professional GitHub README image, large readable typography. "
        "Avoid: tiny text, fake dashboards, fake metrics, private data, real platform logos, stock-photo people, cartoon mascots, neon cyberpunk, excessive gradients, hype claims, misspellings.",
    ),
    (
        "promo-awesome-agent-runtime-map",
        "Create a polished 1600x900 social media poster for X and LinkedIn. "
        "Text: '500 AI Agent Infrastructure Projects' and 'A map of the production agent stack.' "
        "Show a clean landscape map with ten readable category labels: Runtimes, Sandboxes, Browser Automation, MCP Tools, App Integrations, Memory, Safety, Observability, Model Gateways, Deployment. "
        "Place 'Awesome Agent Runtime' as the central title node. "
        "Style: calm technical editorial, off-white background, black text, muted gray panels, teal accents, subtle grid, strong first-glance readability, professional open-source launch poster. "
        "Use plain labels and generic line icons only. Do not draw real platform logos or app icons. "
        "Avoid: tiny text, long URLs, fake metrics, ranking language, endorsements, private data, stock-photo people, cartoon mascots, neon cyberpunk, excessive gradients, hype claims, misspellings.",
    ),
    (
        "promo-awesome-maintainers-welcome",
        "Create a polished 1600x900 social media poster for open-source maintainer outreach. "
        "Text: 'Maintainers: Corrections Welcome' and 'Help make the agent infrastructure map more accurate.' "
        "Show a clean review workflow with four readable steps: Listed, Review, Correct, Improve. "
        "Include a small label: 'Awesome Agent Runtime'. "
        "Style: calm technical editorial, off-white background, black text, muted gray panels, teal accents, subtle grid, constructive and neutral tone, professional GitHub community poster. "
        "Use generic check, edit, and document icons only. Do not draw real platform logos or app icons. "
        "Avoid: tiny text, long URLs, fake dashboards, ranking language, endorsement claims, private data, stock-photo people, cartoon mascots, neon cyberpunk, excessive gradients, hype claims, misspellings.",
    ),
    (
        "promo-global-ai-cold-start",
        "Create a polished 1600x900 social media poster for a public founder/operator case study. "
        "Text: 'Global AI Cold Start' and '30 days to build a public trust layer.' "
        "Show a clean journey from Invisible Product to Searchable Trust Surface to Developer Adoption. "
        "Include five readable signal nodes: Website, GitHub, Content, Community, Backlinks. "
        "Style: calm technical editorial, off-white background, black text, muted gray panels, teal accents, subtle grid, professional startup case-study poster, strong first-glance readability. "
        "Use generic line icons only. Do not draw real platform logos or app icons. "
        "Avoid: tiny text, long URLs, fake metrics, private operational details, stock-photo people, cartoon mascots, neon cyberpunk, excessive gradients, hype claims, misspellings.",
    ),
    (
        "promo-sandbase-open-source-assets",
        "Create a polished 1600x900 social media poster introducing two public SandBase open-source assets. "
        "Text: 'Two Public SandBase Assets' and 'An ecosystem map plus a cold-start playbook.' "
        "Show two large side-by-side panels: 'Awesome Agent Runtime' and 'Global AI Cold Start'. "
        "Under the first panel, include three labels: 500 Projects, 10 Categories, Maintainer Corrections. "
        "Under the second panel, include three labels: 30 Days, Trust Layer, Founder Playbook. "
        "Style: calm technical editorial, off-white background, black text, muted gray panels, teal accents, subtle grid, balanced two-column composition, professional social launch poster. "
        "Use generic line icons only. Do not draw real platform logos or app icons. "
        "Avoid: tiny text, long URLs, fake metrics, endorsement claims, private data, stock-photo people, cartoon mascots, neon cyberpunk, excessive gradients, hype claims, misspellings.",
    ),
]


def request_json(method: str, url: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    req = Request(
        url,
        data=body,
        method=method,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "SandBaseGrowthJournal/1.0 (+https://github.com/sandbaseai/zero-to-one-ai-infra-growth)",
        },
    )
    try:
        with urlopen(req, timeout=60) as resp:
            raw = resp.read().decode("utf-8")
            return json.loads(raw)
    except HTTPError as exc:
        msg = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code}: {msg}") from exc
    except URLError as exc:
        raise RuntimeError(f"Network error: {exc}") from exc


def find_images(value: Any) -> list[str]:
    found: list[str] = []
    if isinstance(value, dict):
        for key, item in value.items():
            if key.lower() in {"url", "image", "image_url", "b64_json", "base64"} and isinstance(item, str):
                found.append(item)
            else:
                found.extend(find_images(item))
    elif isinstance(value, list):
        for item in value:
            found.extend(find_images(item))
    return found


def save_image(name: str, image: str) -> Path:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if image.startswith("http://") or image.startswith("https://"):
        req = Request(image, headers={"User-Agent": "SandBase image downloader"})
        with urlopen(req, timeout=120) as resp:
            content_type = resp.headers.get("content-type", "")
            data = resp.read()
        ext = ".png"
        if "jpeg" in content_type or "jpg" in content_type:
            ext = ".jpg"
        elif "webp" in content_type:
            ext = ".webp"
        path = OUT_DIR / f"{name}{ext}"
        path.write_bytes(data)
        return path

    raw = re.sub(r"^data:image/[^;]+;base64,", "", image)
    path = OUT_DIR / f"{name}.png"
    path.write_bytes(base64.b64decode(raw))
    return path


def wait_for_run(name: str, run_id: str) -> Path:
    while True:
        result = request_json("GET", f"{BASE}/run/{run_id}")
        status = result.get("status")
        print(f"{name}: {status}")
        if status in {"completed", "failed", "timeout"}:
            break
        time.sleep(2)

    if status != "completed":
        raise RuntimeError(f"{name} failed: {json.dumps(result, ensure_ascii=False)[:1000]}")

    images = find_images(result)
    if not images:
        path = OUT_DIR / f"{name}.json"
        path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
        raise RuntimeError(f"{name}: no image URL/base64 found; saved response to {path}")

    return save_image(name, images[0])


def generate_one(name: str, prompt: str) -> Path:
    submitted = request_json("POST", f"{BASE}/run", {
        "model": "openai/gpt-image-2",
        "aspect_ratio": "16:9",
        "output_format": "png",
        "quality": "high",
        "prompt": prompt,
    })
    run_id = submitted["id"]
    print(f"{name}: submitted {run_id}")
    return wait_for_run(name, run_id)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", action="append", default=[], help="Generate only the named card. Can be repeated.")
    parser.add_argument("--resume-run-id", help="Poll an existing SandBase run id and save it with --resume-name.")
    parser.add_argument("--resume-name", help="Output basename to use with --resume-run-id.")
    args = parser.parse_args()

    if not API_KEY:
        print("SANDBASE_API_KEY is missing. Set it in the environment and rerun.", file=sys.stderr)
        return 2

    if args.resume_run_id:
        if not args.resume_name:
            print("--resume-name is required with --resume-run-id.", file=sys.stderr)
            return 2
        path = wait_for_run(args.resume_name, args.resume_run_id)
        print("Saved:")
        print(f"- {path}")
        return 0

    selected = CARDS
    if args.only:
        wanted = set(args.only)
        selected = [card for card in CARDS if card[0] in wanted]
        missing = wanted - {card[0] for card in selected}
        if missing:
            print(f"Unknown card name(s): {', '.join(sorted(missing))}", file=sys.stderr)
            return 2

    saved: list[Path] = []
    for name, prompt in selected:
        saved.append(generate_one(name, prompt))

    print("Saved:")
    for path in saved:
        print(f"- {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
