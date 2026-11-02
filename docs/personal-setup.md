# Unified personal setup

Use `/setup-personal` after installing the collection. This is the single explicit setup
entry point; it is never a startup hook. Creating or installing the skill does not execute it.

| Command | Behavior |
|---|---|
| `/setup-personal` | Inspect and configure missing personal foundations for the active host; ask only for required unknown choices. |
| `/setup-personal --check` | Read-only readiness report and concrete next actions; no setup, tool installation, or configuration writes. |
| `/setup-personal --project /path` | Also configure adopted Matt tracker/domain workflows and pstack model roles in that named project. |
| `/setup-personal --refresh brain` | Reassess only the selected area; preserve working data and unchanged choices. Other areas: attribution, host, matt, pstack, runtimes. |

Combine check or refresh with a project target where appropriate. Project modules never silently
treat the skills source repository or current directory as the intended consuming project.

## What it owns

| Area | Scope | Initial work | Repeat when |
|---|---|---|---|
| Brain suite | Personal deployment | Verify the complete compatible seven-skill suite. | Installing/upgrading the suite or changing host. |
| Brain vault and config | Personal | Reuse a chosen initialized vault or scaffold an explicitly chosen empty vault, configure canonical location, run read-only strict audit. | Vault, primary context, contract, or graph-node configuration changes. |
| Attribution | Active personal skill deployment | Collect agent name and emoji, configure the active skill's private identity, verify a local sample signoff. | Identity changes or installation loses its private configuration. |
| Host instructions | Personal per host | Merge the small brain bootstrap and routing pointer without overwriting unrelated instructions. | Host/instruction mechanism or skill installation changes. |
| Matt tracker/domain conventions | Named project | Reuse or configure issue tracker, glossary/ADR layout, and triage labels only when adopted. | Tracker switches, changed layout/labels, or a deliberate restart. |
| pstack/Cursor role configuration | Named project | Validate available models and chosen budget/roles, write project-local configuration and instruction wiring. | Roles/budget/host change or configured models become unavailable. |
| Tool capabilities | Conditional | Check adopted Git/auth, scoped transcripts, browser/CLI, diagram/video, helper-package, and formal-verification paths. | A workflow adopts or changes that capability. |
| TDD public seams | Per task | Agreement before tests for the current behavior. | New unconfirmed seams or changed task/interface. Never a global setup waiver. |

The skill consults `skills/setup-personal/references/setup-contract.json` to account for every
shipped skill. Many interview, writing, communication, and principle skills need no persistent
configuration. Optional tools are not universal setup requirements. No readiness database is
maintained alongside the actual configuration files.

## Safe reuse and honest evidence

The helper only observes canonical artifacts and exact native-loader resource directories.
It does not search for vaults, scan personal history, query accounts, run tests against a live
vault, install runtimes, repair notes, or write configuration. Existing files are reported as
present/unverified. The orchestrator performs relevant verification and records actual results
before describing an area as verified in the current run.

Missing attribution identity requires real user choices. A missing brain config requires an
explicit vault name/path/primary context; no guessed defaults. Existing nonempty or legacy
vaults follow brain-consolidate audit/repair safeguards rather than receiving a fresh scaffold.
No sample issue, PR, comment, automation, or write to a real vault is used as a readiness test.

Matt and pstack modules are integrated directly into this explicitly requested workflow using
their original contracts/templates. The user need not fire each setup command separately.
The orchestrator does not automatically invoke another human-only skill through the Skill tool,
and it keeps the original confirmation/draft-review requirements.

Model setup uses the consuming project's host-specific location, including `.agents/pstack-models.md`
for Codex and `.cursor/rules/pstack-models.mdc` for Cursor. It does not silently mutate global
model defaults or activate poteto-mode. A local model-access problem does not authorize changing
shared project policy. Runtime prerequisites and paid-account access stay explicit.

## Status report

The output lists area, scope, status, evidence, and next action/refresh trigger. Statuses distinguish
missing, incomplete, present/unverified, verified this run, unknown/blocked, not applicable, and
deliberately deferred. It ends with changed paths and any remaining required choices. A rerun
rechecks canonical artifacts and skips unchanged setup; check mode produces no mutations.

## Development verification

```sh
npm run test:personal-setup
npm run skills:validate:setup-personal
```

The fixture tests never use the live vault or user configuration. Scenario evaluations cover
check-only startup, existing personal setup with missing project model roles, and a legacy vault
that must not be overwritten. The evaluation corpus lives beside the skill; generated workspaces
stay outside this repository.
