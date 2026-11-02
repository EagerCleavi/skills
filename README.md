# Skills

Source repository for reusable Agent Skills in the open format used by `npx skills` and compatible agents.

## Quick Start

```sh
npm install
npm run skills:list
npm run skills:validate
npm test
npm run typecheck
```

`npm test` runs deterministic script and corpus tests. Model behavior/trigger evaluations use the `skill-creator` workflow and are reviewed separately.

For a first-time brain setup, follow this order: initialize the vault,
install the suite for Codex or OpenCode, configure the vault, then run the
verification commands in **First-time Verification**.

## Skills

- `attribution`: configurable external-work attribution.
- `excalidraw`: editable technical diagrams with a mandatory render, inspect, and refine loop.
- `brain`: shared brain-suite foundation, contract, configuration, and router.
- `brain-contextualize`: read-only turn-one and context-switch orientation.
- `brain-recall`: bounded read-only memory retrieval.
- `brain-remember`: proactive/explicit capture and checkpoints.
- `brain-consolidate`: structural doctor, repair, migration, archive, and forgetting.
- `brain-synthesize`: cross-owner pattern reporting and automatic high-confidence promotion.
- `brain-build`: durable onboarding/refresh for repositories, workspaces, wikis, and tools.
- `skill-creator`: Anthropic's Apache-2.0 skill for creating and evaluating skills.

The seven `brain*` skills form one versioned suite. Install and update them together; operator skills are not standalone packages.

## Imported personal collection

The repository now contains **95 skills**: the ten existing skills above plus 32 primary personal
workflows and 53 required dependency copies from Matt Pocock, pstack, and cursor-team-kit. See the
[imported catalog](docs/personal-skills.md) for descriptions and manual/passive invocation,
and the [collision and overlap review](docs/collisions-and-overlaps.md) for routing boundaries,
dependency closure, and host adaptations. There were no exact skill-name collisions.

The personal additions include the complete selected grilling family, research, planning,
handoff, debugging, retrospectives, communication, and preference workflows. They do not
include the project QA collection or repo-side `/help`. Matt's `tdd`, `codebase-design`, and
`code-review` retain repo ownership but are duplicated here because the personal implementation
workflows require them. Pstack playbooks bring their complete supporting principles and tools.

Install the complete personal collection, including its dependencies:

```sh
npx skills add . --global --agent codex --all --yes
```

This installs all 95 skills, including the complete existing brain suite. For a selective installation,
include the requested skills and the transitive `requires` entries from the import manifest;
`npx skills` does not resolve that graph automatically.

Use the relevant supported agent flag for other hosts. After installation, add a pointer to
`docs/collisions-and-overlaps.md` from the host's personal instructions using the stable absolute
path of this source checkout. Retain the existing brain bootstrap. Installation does not run
tracker setup, configure attribution, scan transcripts, or edit your vault. Required skill dependencies are included in this collection. Runtime tools, model access,
credentials, and per-project initialization still need their normal setup.

Run `npm run skills:validate:personal` to verify the imported source hashes, unique names,
frontmatter, and explicit-only policies. Missing required skills or host-capability providers fail validation.
The manifest pins all source revisions, and each imported skill retains its upstream license.

The original helpers under `poteto-mode/scripts` and `statechart/scripts` have their own
package manifests and runtime requirements (including Bun and formal-verification tooling where
applicable). They are preserved as upstream packages and excluded from the brain toolkit's root
TypeScript compilation. Their source hashes are checked; install and run their own checks when
adopting those capabilities. Root tests do not claim those runtime environments are initialized.

## Initialize a Brain Vault

The brain suite expects an initialized Contract v2 Markdown vault; installing the skills does not create one. Before running `configure:brain`, create or migrate a vault with these root routers:

```text
index.md
wikis.md
projects.md
workspaces.md
tools.md
decisions.md
gotchas.md
codestyle.md
improvements.md
```

`index.md` must link the other eight routers. Create the configured primary context as a node entry point, for example `wikis/user/_user.md`, with `created`, `updated`, and `status` frontmatter and a final owner tag such as `#wiki/user`. Register that entry point in the matching router, for example:

```markdown
# Wikis

## Active

- [[wikis/user/_user|User]]

## Dormant

## Archived

#index
```

If you start from an Obsidian vault, remove or migrate its default
`Welcome.md` note before a strict audit; substantive root notes are reported as
legacy-root-note findings.

## Configure Brain

Brain deployment configuration lives outside installed skill directories at:

```text
${XDG_CONFIG_HOME:-$HOME/.config}/agent-brain/config.json
```

Generate it after the target vault paths exist:

```sh
npm run configure:brain -- \
  --vault-name "oc-brain" \
  --vault-path "/absolute/path/to/vault" \
  --primary-context "wikis/user/_user.md"
```

The script accepts legacy `--primary-user-note` and `--graph-palette-note` flag names during migration. It requires an initialized vault and verifies every configured Markdown path.

`--graph-palette-node` is optional. Add it only when the referenced Markdown
file already exists in the vault:

```sh
npm run configure:brain -- \
  --vault-name "oc-brain" \
  --vault-path "/absolute/path/to/vault" \
  --primary-context "wikis/user/_user.md" \
  --graph-palette-node "tools/vault-graph/_vault-graph.md"
```

## Install

Install the complete suite globally for the host you use.

### Codex

```sh
npx skills add . --global --agent codex \
  --skill brain \
  --skill brain-contextualize \
  --skill brain-recall \
  --skill brain-remember \
  --skill brain-consolidate \
  --skill brain-synthesize \
  --skill brain-build \
  --yes
```

Add the bootstrap from `skills/brain/references/host-bootstrap.md` to
`~/.codex/AGENTS.md`, then start a new Codex task after changing the global
instruction file. Codex detects skill changes automatically; restart Codex if
an installed skill does not appear.

### OpenCode

```sh
npx skills add . --global --agent opencode \
  --skill brain \
  --skill brain-contextualize \
  --skill brain-recall \
  --skill brain-remember \
  --skill brain-consolidate \
  --skill brain-synthesize \
  --skill brain-build \
  --yes
```

Merge the bootstrap from `skills/brain/references/host-bootstrap.md` into
`~/.config/opencode/AGENTS.md`, then quit and restart OpenCode after changing
global skills or the global instruction file.

For either host, run `npm run brain:suite:verify` against source and verify
installed copies as part of deployment. Remove any legacy installed
`deep-dive` skill after `brain-build` is present.

Install all repository skills for all supported agents only when that is intentional:

```sh
npx skills add . --global --all
```

The universal global store is normally `~/.agents/skills/`. Treat installed copies as generated deployments; edit this repository instead.

## First-time Verification

After the vault is initialized, configured, and the suite is installed, run:

```sh
npm run brain:suite:verify
npm run brain:audit -- --strict
```

The suite verifier checks the source deployment and the audit checks the
configured vault. A clean Contract v2 vault should report zero errors and zero
warnings. If you install into a non-default skills root, run the verifier
directly with that root:

```sh
npx tsx skills/brain/scripts/validate-suite.ts \
  --skills-root "/absolute/path/to/installed/skills"
```

## Brain Operations

Run the read-only contract-v2 doctor:

```sh
npm run brain:audit
npm run brain:audit -- --vault-path "/alternate/vault" --strict
```

Run the read-only pattern report:

```sh
npm run brain:patterns -- --vault-path "/absolute/vault" --strict --pretty
```

The doctor validates root routers, wikis/projects/workspaces/tools, owner tags, atomic records, cold history, workspace membership, project dependencies, global collections, graph groups, issue tags, and backlog state. The pattern reporter only discovers/ranks candidates; `brain-synthesize` performs semantic gates and controlled writes.

## Validation

```sh
npm run skills:validate:brain-suite
npm run brain:suite:verify
npm run test:brain
```

Each operator has an eval corpus under `evals/evals.json`. Joint routing tests must show all seven descriptions together because isolated trigger tests cannot detect `contextualize`/`recall`, `consolidate`/`synthesize`, or `build`/ordinary-build collisions.

## Layout

```text
skills/
  excalidraw/               # Excalidraw workflow and visual quality loop
  brain/                    # shared contract/config/scripts
  brain-contextualize/
  brain-recall/
  brain-remember/
  brain-consolidate/
  brain-synthesize/
  brain-build/
  attribution/
  skill-creator/
```

Every directory has a `SKILL.md` whose `name` matches the directory. Shared configuration and policy belong only to `brain`; sibling operators load the foundation rather than copying it.

## Development

- Keep skill descriptions precise and include near-miss exclusions.
- Keep scripts deterministic, bounded, and dependency-light.
- Use disposable fixture vaults for tests; never run mutating evaluations against the live vault.
- Keep evaluation workspaces outside this repository so discovery cannot find snapshot skills.
- Preserve the vendored `skill-creator/LICENSE.txt` and keep local changes small.

The `.skill` packager excludes eval directories and attribution's generated private identity config. Brain configuration is external and therefore cannot leak through skill archives.
