# Brain onboarding

This is the initialization path, not a migration or maintenance shortcut. Load the exact
resolved brain foundation and read its vault contract before mutation. Use its canonical
configuration location and suite manifest; do not search for alternate deployments.

## Required inputs and safe reuse

Collect or reuse the vault name, absolute vault path, and vault-relative primary context.
The graph palette is optional and must name an existing Markdown node if supplied.
Do not derive the user's identity from a path or choose a vault location silently.

Inspect a chosen existing directory before writing. An initialized vault should be audited
read-only and reused. If it contains notes but is incomplete/legacy, route to brain-consolidate;
do not treat partial setup as an empty vault. If the user explicitly chose a new empty vault,
show the proposed root skeleton and primary-context record before creating them. Preserve
existing files and refuse to overwrite them during initialization.

## Empty vault skeleton

Create these nine root routers:

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

`index.md` links the other eight routers with Obsidian wiki links and ends in `#index`.
Class routers use `## Active`, `## Dormant`, and `## Archived`, followed by `#index`.
Root atomic-record routers have an appropriate title and `#index`; empty collections
are allowed. Include dates only where the current vault contract calls for them.

Create the user-approved primary entry point with the contract's current date metadata,
`status: active`, a minimal context statement grounded in supplied facts, and the proper
final owner tag. For `wikis/<slug>/_<slug>.md`, use `#wiki/<slug>` and register its exact
path in `wikis.md`. Do not invent biography, preferences, history, or project membership.
If the user chooses another node class, follow that class's contract instead.

Run `<brain-base>/scripts/configure-brain.ts` with the explicit selected inputs after
the paths exist. Reuse the actual runtime invocation supported by the host/source checkout.
Do not pass a noncanonical deployment config path outside isolated tests.

## Verification

Run the foundation's strict audit against the configured vault. Any warning/error is an
open finding; do not repair it automatically to get a green result. Verify suite resources
through native loader results and the suite manifest. Run the suite verifier with a common
installed root only when that root is explicitly known; otherwise state the limitation.

Merge the short brain bootstrap into the active host instructions. Never run a write operator,
pattern promotion, or a test note write in the real vault merely to prove setup works.
