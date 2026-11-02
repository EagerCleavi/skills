# Project setup modules

These modules run within an explicit `/setup-personal --project <path>` request. Read the
corresponding installed setup contract and templates as source references; do not invoke
human-only skills through the Skill tool. This is a user-authorized unified workflow with
its own entry point. Keep the original confirmation and draft-review steps.

## Matt Pocock

1. Read `setup-matt-pocock-skills/SKILL.md` through the resolved available-skill resource.
   Inspect project remotes, existing instructions, tracker docs, glossary/domain layout,
   and whether triage is actually installed/adopted. Discover before asking.
2. Reuse `docs/agents/issue-tracker.md` and `docs/agents/domain.md` when current. The
   triage label file and instruction sub-block are conditional on triage adoption.
   An agent merely installing `tdd` does not need tracker provisioning.
3. For missing/changed decisions, collect tracker and any needed vocabulary/layout choices
   using the upstream sequence. Default to a single glossary/ADR context unless actual
   monorepo evidence warrants alternatives. Do not switch a working tracker silently.
4. Present the concrete instruction block and docs drafts. After confirmation, update the
   project's existing instruction file and docs in place. Respect the source's file-selection
   rules: prefer an existing CLAUDE.md, otherwise existing AGENTS.md, ask if neither exists.
   Do not create duplicate competing instruction files.
5. Reuse the setup skill's local tracker/domain templates. If adopting a remote tracker,
   verify its existing identity/access; show any missing remote wiring before changing it.
   Create agreed missing triage labels only when applicable. No sample issues or PRs.

Existing tracker/domain docs are not proof of access. Report authentication/runtime checks
separately. Ordinary fact edits do not require restarting setup; tracker switches or a
deliberate restart are the upstream reasons to rerun the full flow.

## pstack / Cursor-family workflows

Read `setup-pstack/SKILL.md` and the active host adapter. Reuse current project configuration.
Enumerate only actual available models and settings from the session/tool schema. Collect the
upstream budget and role choices when missing or changing; preserve supported aliases, full
role names, and panel lengths. Show the table and confirm before writing.

Use the project-local destinations in `host-integration.md`, replacing the source's global
model paths. For non-Cursor hosts omit Cursor frontmatter and add the project instruction
pointer. Verify syntax and model availability; do not query accounts or choose a paid model
as a side effect of listing capabilities. Unsupported families use an agreed supported
fallback or remain blocked, with a lost multi-model comparison disclosed.

Report the reload requirement. Offer behavioral/formal verification only when relevant and
missing; do not create it as a default setup dependency. Do not execute poteto-mode, swarm,
reviews, or an autonomous development run just to test that the role configuration exists.

## Per-task agreements remain per task

Matt's `tdd` needs public-seam agreement before tests for the current work. A project setup
record is not blanket authorization for future seams. Project artifacts, quality gates,
domain facts, and verification harnesses remain owned by the project even when a personal
setup entry point creates them.
