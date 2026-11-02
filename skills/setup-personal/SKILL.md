---
name: setup-personal
description: "Explicit personal skill setup, readiness checks, and targeted refresh for brain, attribution, host integration, Matt Pocock project workflows, and pstack/Cursor model roles. Use when the user invokes /setup-personal; do not run during ordinary development or startup."
disable-model-invocation: true
argument-hint: "[--check] [--project /absolute/path] [--refresh area]"
---

# Set up the personal skill collection

One entry point for initial setup and maintenance. Run only when explicitly requested.
Installing or reporting skills does not invoke this workflow. Creating/editing this skill
is not an instruction to configure the current machine.

## Choose scope and inspect

- `/setup-personal`: configure missing personal foundations for the active host. Discover
  project needs, but do not silently configure the current directory as a project.
- `/setup-personal --project /path`: also set up Matt's project conventions and pstack
  model roles for that named project. Those artifacts remain project-owned.
- `/setup-personal --check`: read-only inspection and next actions. Combine with `--project`
  to inspect a project. Do not write, invoke setup, install tools, audit private history,
  or ask setup questions in check mode. Check mode takes precedence over other flags.
- `/setup-personal --refresh attribution` (or `brain`, `host`, `matt`, `pstack`, `runtimes`):
  reassess that area and update only changed settings. Project areas require an explicit
  project target. Refresh is not permission to reset, migrate, delete, or replace working data.

1. Identify the active host, installed collection, explicit project if any, and requested
   area. Use the host's skill catalog/native loader. Resolve `brain` and `attribution`
   through that loader and retain their exact returned base directories. If no loader
   exists, use only exact SKILL.md paths advertised in the host catalog. Do not locate
   brain resources by scanning parent skill directories or probing alternate config roots.
2. Read `references/setup-contract.json` for setup ownership and per-skill coverage.
   This registry describes the shipped collection; compare it with actual installed skills.
   Missing required skills are install gaps, not initialized capabilities. Do not install
   the whole collection automatically when a narrower skill selection was intentional.
3. Observe canonical artifacts with the bundled helper, supplying exact resolved bases:

   ```sh
   python3 <setup-base>/scripts/check_setup.py --host codex \
     --brain-dir <resolved-brain-base> --attribution-dir <resolved-attribution-base>
   ```

   Add `--project /path` only for a supplied target, `--triage-installed` only when confirmed,
   and `--host-instructions /path` when the host reports a nonstandard instruction surface.
   Supported host labels: `codex`, `claude`, `cursor`, `opencode`. Omitted resource bases
   produce Unknown. The helper only observes; it never repairs or executes setup.
4. Classify each area as missing, incomplete, present/unverified, verified in this run,
   unknown/blocked, not applicable, or deliberately deferred. File presence is not proof
   of valid credentials, a working renderer, usable models, successful tests, or lifecycle loading.
   Follow project pointers for custom layouts instead of guessing filenames.
5. In setup mode, reuse valid existing choices and continue independently actionable work.
   Ask only for required missing decisions, grouped by area. Give concrete proposed values
   and edits before the relevant upstream confirmation. Never infer an agent identity,
   invent a vault, choose an inaccessible model, or recreate completed setup just to run
   every module. Do not store a second readiness database or a blanket "setup complete" marker.

## Personal foundations, once per user/host

### Brain

Load `brain` and use its suite/contract version. Missing canonical configuration is the
expected onboarding state; collect the required choices instead of searching for a vault.
Read `references/brain-onboarding.md` before writing any vault artifact.

1. Verify all seven suite operators are available and compatible. Resolve operators through
   the native loader, not guessed sibling paths. Keep them at one version; do not replace
   an existing suite as a side effect of configuring it.
2. Read only `${XDG_CONFIG_HOME:-$HOME/.config}/agent-brain/config.json`. Reuse valid vault
   name/path, primary context, and optional graph node. Missing choices require the user.
3. For a chosen new empty vault, initialize the Contract v2 routers and user-approved primary
   context using the onboarding reference, then run the resolved foundation's
   `scripts/configure-brain.ts` with explicit `--vault-name`, `--vault-path`, and
   `--primary-context`. Only supply a graph node that already exists. Use the host-supported
   TypeScript runner; do not invent source-repository npm scripts in an installed skill.
4. A nonempty, partial, legacy, or incompatible vault needs the `brain-consolidate` audit and
   repair safeguards. Show findings; do not overwrite notes, migrate, or clean up automatically.
   Read the foundation's vault contract before all vault mutation.
5. Run read-only suite verification against an explicit host-reported installed skills root
   when available, and the resolved brain audit with `--strict`. Otherwise validate the exact
   loaded operator resources and report the verification limit. Distinguish errors and warnings
   from setup success. Do not run synthesis or durable onboarding merely to test setup.

### Attribution

Resolve the active attribution skill and read its contract. Its identity lives at
`<attribution-base>/references/attribution-config.md`, not in brain configuration.
If missing or changing, collect the **agent name and emoji**; do not infer the user's name
or silently pick Codex. Run that skill's `scripts/configure-attribution.ts --name ... --emoji ...`
with structured arguments or safe shell quoting. Verify the file and a locally formatted
sample signoff. Do not create a remote issue/comment/PR as a test. If source and installed
skills are separate copies, configure the active copy; do not assume configuring source
updated every deployment. Keep the private identity excluded from Git and skill archives.

### Active host integration

Merge the foundation's short bootstrap into the active host's personal instructions, preserving
unrelated content and updating an existing block rather than duplicating it. Point to this
collection's routing/overlap guidance through its stable source path when available. Use
`references/host-integration.md` for scope and path translations. Brain's startup hook loads
`brain` then `brain-contextualize`; it does not run this setup skill, `/poteto-mode`, every
personal skill, or a full vault audit each session. Report any host reload/restart requirement.
An edited instruction file is not proof that this already-running session reloaded it.

## Project modules, once per named project

Read `references/project-setup.md`. Apply these modules directly from their setup contracts
and templates under this explicit unified setup request. Do not invoke another human-only
skill through the Skill tool. Retain upstream interviews, draft review, and confirmation gates;
the user does not need to issue a second setup command to complete this orchestrator.

- **Matt**: inspect and reuse tracker, domain layout, and optional triage vocabulary. Draft
  missing/changed artifacts, confirm unresolved choices, then write project-owned docs and
  the existing project instruction block. Create remote labels only when adopting triage,
  with an authenticated configured tracker and explicit scope. Do not create issues or PRs
  as a readiness test. Full tracker setup is conditional on adopting those workflows.
- **pstack/Cursor**: discover actual supported models and reasoning settings, reuse current
  project policy, collect missing budget/role choices, validate every real model, and write
  the host's **project-local** configuration plus its instruction pointer. `inherit-parent`
  is a supported fallback when agreed; it is not a fabricated cross-model comparison.
  Preserve role names. Do not write global defaults merely because the original upstream
  setup uses a user-global path. Do not enable poteto style automatically.
- TDD seam agreement is **per task**, not a one-time initialization checkbox. Setup cannot
  authorize tests at all future seams. Generated behavioral/formal verification is conditional
  project work; offer it when relevant rather than creating harnesses for every personal install.

## Conditional capabilities across the collection

Use the registry to account for every installed skill. For additional personal/plugin skills,
inspect their declared setup contract on demand and report unknown prerequisites honestly.
Many principles, writing, communication,
planning, and interview skills need no separate persistent initialization. For adopted workflows,
check relevant capabilities: scoped transcript access, Git identity/tracker auth, browsers/CLI
control, diagram rendering, video tools, Bun/Node helper packages, or formal-verification runtimes.
Prefer existing host tools and MCP connections. Do not install every optional package, alter
system settings, read chat histories, activate automations, or provision infrastructure to make
an all-green report. Honor filesystem/network approvals when installation is actually needed.

For each missing capability, give its affected workflows, concrete setup action, ownership,
and an honest verification limit. Defer optional capabilities that the user has not adopted.
Use each skill's own prerequisites and rendering/testing standards when verifying it.

## Finish and reruns

Return **Area | Scope | Status | Evidence | Next action / refresh trigger**, followed by changed
paths and remaining required choices. Name the current host and project scope explicitly.
Report actual commands/results, not merely created files. On rerun, observe the canonical
artifacts again, skip valid unchanged settings, and refresh only the relevant module.

Refresh brain after vault/primary context/contract changes; attribution after identity changes;
host wiring after installation/host changes; Matt after tracker/layout changes; pstack after
role/budget/host changes or unavailable models. A local capability failure is not permission
to rewrite shared project policy. Check mode ends with the same table and no mutations.
