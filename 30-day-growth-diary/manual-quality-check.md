# Manual Quality Check

Date: 2026-06-25

Purpose: keep the 30-day practical manual readable, internally consistent, and safe to operate from.

## Current Check Result

Status: passed local manual health check.

Checked:

- 94 Markdown files scanned.
- 30 daily log files exist under `30-day-growth-diary/days/`.
- No broken local Markdown links were found.
- `git diff --check` passed.
- English README and Chinese README now point to the current main SOP and 30-day completion plan.
- Daily Command Center now prioritizes the 30-day growth plan before secondary outreach tracks.
- Day 18-20 now separate prepared work from publication checklists.
- Day 11, Day 12, and Day 14 are marked as archived plans with later execution references instead of empty planned logs.

## Manual Structure

Primary entry points:

- `README.md`
- `README.zh-CN.md`
- `daily-command-center.md`
- `playbooks/sandbase-daily-growth-sop.md`
- `30-day-growth-diary/30-day-completion-plan.md`

Daily execution:

- `30-day-growth-diary/days/day01-...md` through `day30-...md`

Weekly plans:

- `30-day-growth-diary/weekly-recaps/week01-foundation-recap.md`
- `30-day-growth-diary/weekly-recaps/week02-distribution-plan.md`
- `30-day-growth-diary/weekly-recaps/week03-open-source-growth-base.md`
- `30-day-growth-diary/weekly-recaps/week04-launch-readiness-and-recap.md`

Supporting playbooks:

- `playbooks/sandbase-daily-growth-sop.md`
- `playbooks/sandbase-ai-three-site-growth-plan.md`
- `playbooks/day16-multichannel-distribution-sop.md`
- `playbooks/open-source-opportunity-sourcing.md`
- `playbooks/emerging-agent-infrastructure-registry.md`

## Repeatable Check Commands

Run from the repository root.

```sh
find 30-day-growth-diary/days -maxdepth 1 -name 'day*.md' | sort | wc -l
```

Expected result:

```text
30
```

Check local Markdown links:

```sh
node - <<'NODE'
const fs=require('fs'); const path=require('path');
function walk(dir){let out=[]; for(const e of fs.readdirSync(dir,{withFileTypes:true})){ if(e.name==='.git') continue; const p=path.join(dir,e.name); if(e.isDirectory()) out=out.concat(walk(p)); else if(e.isFile()&&p.endsWith('.md')) out.push(p);} return out;}
const files=walk('.'); const re=/\[[^\]]+\]\(([^)]+)\)/g; let issues=[];
for(const file of files){const text=fs.readFileSync(file,'utf8'); let m; while((m=re.exec(text))){let href=m[1].trim(); if(!href || href.startsWith('#') || /^https?:|^mailto:/.test(href)) continue; href=href.split('#')[0]; if(!href) continue; const target=path.resolve(path.dirname(file),href); if(!fs.existsSync(target)) issues.push({file,href});}}
console.log(JSON.stringify({files:files.length, brokenLinks:issues},null,2));
NODE
```

Check whitespace and patch hygiene:

```sh
git diff --check
```

## Status Vocabulary

Use these statuses consistently:

- `Completed`: public action or local execution is done and recorded.
- `Completed locally`: local repo/docs work is done; commit or publish may still be pending.
- `Prepared`: drafts, images, or comment packs are ready, but public posting still needs confirmation.
- `Planned`: future day, not executed yet.
- `Archived plan`: original plan was not executed as written, but the work was later covered elsewhere.

## Confirmation Boundary

Codex may prepare:

- docs
- drafts
- generated images
- local repo edits
- checklists
- comment drafts
- article outlines

Human confirmation is required before:

- publishing X / LinkedIn / DEV.to posts
- posting GitHub comments
- submitting directories
- making paid submissions
- launching Product Hunt or similar surfaces
- changing account settings or permissions
