# Day 17 Local Asset Inventory

Date: 2026-06-25

Scope: local-only inventory. No social posting, no public comments, no directory submissions.

## Current Boundary

Today is Day 17 and social operation has already happened.

Do not touch:

- X
- LinkedIn
- Peerlist
- public GitHub comments
- public maintainer outreach
- directory submissions

Local work is allowed:

- docs
- repo readiness
- SOP cleanup
- quality checks
- commit prep
- asset inventory

## Primary Repositories

### `awesome-agent-runtime`

Path:

```text
work/sandbaseai/awesome-agent-runtime
```

Status:

- has uncommitted local changes
- expanded to 500 projects
- README regenerated
- contribution entry point added
- category cleanup issue template added
- Day 18 announcement pack added
- maintainer outreach shortlist added

Recommended action:

- commit and push before Day 18 publication

Suggested commit:

```text
Expand agent runtime landscape to 500 projects
```

Day 18 dependency:

- public social posts should link to this repo after the commit is pushed

### `global-ai-cold-start`

Path:

```text
work/sandbaseai/global-ai-cold-start
```

Status:

- has uncommitted local changes
- 30-day manual structure completed
- Day 17-30 daily logs created
- main SOP added
- manual quality check added
- Day 18-20 distribution packs prepared
- Day 18 PNG generated
- 96 Markdown files checked
- local Markdown links currently pass

Recommended action:

- commit after `awesome-agent-runtime`

Suggested commit:

```text
Complete 30-day growth manual structure
```

## Supporting Repositories

### `agent-sandbox-runtime-probe`

Path:

```text
work/sandbaseai/agent-sandbox-runtime-probe
```

Status:

- not currently a git repository
- local draft is present
- includes README, publishing notes, compatibility checklist, JSON cases, and runtime notes

Files:

- `README.md`
- `PUBLISHING.md`
- `checklists/runtime-compatibility.md`
- `cases/sandbox-runtime-probe.json`
- `notes/runseal-observations.md`
- `notes/kars-policy-freshness.md`
- `notes/ageos-seccomp-validation.md`

Role:

- useful future open-source asset for Day 19 and Day 27
- can become a small public repo after license and repository creation

Recommended action:

- do not publish today
- later decide whether to create a GitHub repo
- if published, position as a neutral compatibility checklist, not a SandBase product claim

### `agent-sandbox-cookbook`

Path:

```text
work/sandbaseai/agent-sandbox-cookbook
```

Status:

- git working tree is clean

Role:

- supporting developer education asset
- can be used in later sandbox/runtime content

Recommended action:

- leave untouched today

### `.github`

Path:

```text
work/sandbaseai/.github
```

Status:

- git working tree is clean

Role:

- GitHub organization profile and trust surface

Recommended action:

- leave untouched today

### `awesome-native-agent-platforms`

Path:

```text
work/sandbaseai/awesome-native-agent-platforms
```

Status:

- git working tree is clean

Role:

- older / adjacent ecosystem resource
- may be referenced later, but `awesome-agent-runtime` is now the primary open-source entry asset

Recommended action:

- leave untouched today

### `sandbase-monorepo`

Path:

```text
work/sandbaseai/sandbase-monorepo
```

Status:

- has one existing local change:
  - `sandbase-dashboard/package-lock.json`

Role:

- product monorepo
- not part of today's Day 17 manual / open-source-growth cleanup

Recommended action:

- do not touch in this session
- avoid mixing product dependency lockfile changes into growth/manual commits

## Next Local-Only Options

If continuing today without public side effects, choose one:

1. Commit prep only:
   - review final diffs
   - stage by repository
   - prepare commit messages
2. Probe prep only:
   - add license recommendation to `agent-sandbox-runtime-probe/PUBLISHING.md`
   - prepare repo description and topics
3. Manual polish only:
   - add a top-level "Current status" section to the manual
   - keep Day 18-20 publication checklists pending

## Recommended Next Step

Commit order:

1. `awesome-agent-runtime`
2. `global-ai-cold-start`

Then stop for today.

Start Day 18 in the next operating session.
