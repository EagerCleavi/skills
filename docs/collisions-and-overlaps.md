# Personal skill import review

Compared against `EagerCleavi/skills` main at `99122ae` before import. The 32 additions
come from the accepted personal selection in `EagerCleavi/mesh-engineering-skills`.
There were **zero exact directory or frontmatter-name collisions** with the ten existing
skills. Dependency expansion now adds 53 shared engineering skills, for 95 discoverable skills total. No existing skill was removed or renamed.

## Routing and ownership boundaries

| Overlap | Route by intent | Placement / handling |
|---|---|---|
| `recall` vs `brain-recall` / `brain-contextualize` | Explicit `/recall` reconstructs recent work from chats and shared records. `brain-recall` retrieves bounded existing vault knowledge; contextualize loads startup context. | Keep both. Do not auto-run pstack recall at startup or treat it as the brain operator. |
| `workflow-from-chats` vs `automate-me` vs `skill-creator` | Workflow-from-chats extracts evidence-backed preferences; automate-me explicitly creates a personal mode; skill-creator authors/evaluates an arbitrary skill. | Use one entry point for the intent. Existing skill-creator is the Codex authoring equivalent of Cursor's `create-skill`. |
| Those preference workflows vs `brain-remember` | Workflow guidance belongs in a skill/rule/project doc. Brain retains safe durable memory owned by the vault. | Avoid recording the same instruction in both; keep the existing brain ownership/retention contract. |
| `research` vs `brain-build` | Research answers a bounded question from primary sources and writes project findings. Brain-build creates or substantially refreshes a durable memory node. | Research is not implicit vault onboarding and does not replace ordinary repository investigation. |
| `handoff` vs brain checkpoints | Handoff makes a portable session transfer; brain checkpoints retain durable facts. | Do not store entire handoffs or transient task status as brain memory. |
| `retro` vs `brain-synthesize` / `brain-consolidate` | Retro reviews a coding session's environment. Brain synthesis promotes verified repeated memory patterns; consolidation maintains vault structure. | Retro does not authorize vault repair or global pattern promotion. |
| `weekly-review` vs `what-did-i-get-done` | Weekly-review adds a weekly category breakdown. What-did-i-get-done summarizes a specified date range. | Keep both. Use the specific time-range tool when dates are specified; avoid duplicate summaries. |
| `bro` vs `wait-what` vs `ketchup` | Bro simplifies the last message; wait-what re-pitches it with context; ketchup summarizes progress since the last user message. | Explicit user choices; ketchup-video adds an optional rendered-video variant. |
| `pr` vs existing `attribution` | PR controls the description structure; attribution adds the required agent signoff to tracker content. | Apply both. Configure attribution first; do not invent an identity or skip the attribution gate. |
| `writing-for-agents` vs `skill-creator` | Writing-for-agents supplies writing mechanics; skill-creator handles the full authoring/evaluation lifecycle. | Reference and workflow are complementary; imported upstream text remains unchanged. |
| `excalidraw` vs imported writing/prototype/PR visuals | Excalidraw is the existing editable technical-diagram workflow. A PR sketch or throwaway UI prototype is not automatically an Excalidraw task. | Preserve the existing diagram/render workflow when a technical canvas is requested. |

## Required dependencies are included

The user explicitly authorized duplicating required skills across personal and project sets.
Primary ownership still controls where project facts and conventions live; it no longer prevents
installing a required supporting skill on both sides. The import now includes **32 primary
personal skills and 53 shared dependencies**, plus the ten pre-existing skills.

`imports/personal-skills.lock.json` records the required graph. Missing required skills fail
validation. The closure includes Matt's `tdd`, `code-review`, and `codebase-design`; pstack's
`why`, `unslop`, `poteto-mode`, and its design/review/control/writing/verification workflows;
and all 24 leaf principles used by those playbooks. This is intentionally transitive: copying
only direct callees would leave the broader playbooks incomplete.

`create-skill` is a host capability, mapped to the existing `skill-creator` on Codex/Claude.
The original pstack `poteto-agent` and `comment-sicko` definitions and harness adapters travel
inside `poteto-mode/support/`. When a host lacks those native agent types, read the matching
support definition and supply it to the host's subagent tool. Use only available models and
honor project instructions and user authorization over upstream default autonomy language.

The project set also duplicates `bro`, `ketchup`, and `setup-matt-pocock-skills`. Shared
skill copies must stay at the same recorded revisions. When both project and personal copies
are installed, inspect host precedence; a name match is intentional only when the implementation
and source revision match. Do not use a global copy to override customized project policy.

Pure router menus and conditional "is installed" checks do not add required dependencies.
Matt's `ask-matt` includes an optional `/teach` reference to his unselected educational workflow;
pstack's different `teach` remains unimported here. Do not silently substitute it. The grilling
family remains personal and is not pulled into project repos by the dependency graph.

The collection is complete for recorded **skill** dependencies. Transcript access, video rendering,
authentication, verified model choices, runtime packages, and project tracker/TDD setup remain
separate capabilities and must not be claimed ready from installation alone.

## Host integration

Read this routing document from personal host instructions after installing the collection.
Keep the existing brain bootstrap. Use the active host's native skill loader and actual tools;
translate Cursor-specific paths to the active host's known discovery/history locations.
For Codex, project-generated skills belong in `.agents/skills/`, personal-generated skills in
the configured personal discovery root. Do not guess a transcript API or broad-scan home
directories. Model roles must use supported models or the parent model; upstream model
names are not evidence of local availability.

Manual-only imports retain `disable-model-invocation: true`. Pstack explicit-only imports also receive
separate `agents/openai.yaml` policy adapters, because their upstream snapshot supplied no
Codex policy file. Those adapters disable implicit invocation; upstream skill text is unchanged.
User-only Matt skills must not be invoked by another skill. Merely mentioning their names in
a router is a suggestion to the user, not authorization to execute them.

Do not run personal setup merely because the skills are installed. Project initialization,
current task TDD seam agreement, runtime tools, and personal brain/attribution configuration
are separate prerequisites. This import does not edit installed user configurations or the vault.

## Provenance and updates

`imports/personal-skills.lock.json` records exact source revisions, per-file hashes, generated
policy adapters, and external skill dependencies. Every imported skill carries its upstream
license as `LICENSE.upstream`, so attribution travels with single-skill installations.
Preserve Matt's embedded Humanlayer credit in `pr`. Review snapshot and manifest changes
together; do not silently modify imported instructions to resolve semantic overlap.
