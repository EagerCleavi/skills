# Personal skill catalog

32 primary workflows plus 53 required dependency copies. The ten pre-existing skills are documented in the root README.

Manual means explicit user invocation; passive eligible means selectable when relevant, not always running.

| Skill | Source | Role | What it does | Invocation |
|---|---|---|---|---|
| [architect](../skills/architect/SKILL.md) | pstack | dependency | Sketch types, signatures, and module structure before code, then stay in the loop while implementation fills in. | Manual |
| [arena](../skills/arena/SKILL.md) | pstack | dependency | Spawn N parallel candidates at the same task, pick a base, graft the strongest parts of the losers into it. | Manual |
| [ask-matt](../skills/ask-matt/SKILL.md) | mattpocock | primary | Ask which skill or flow fits your situation. | Manual |
| [automate-me](../skills/automate-me/SKILL.md) | pstack | primary | Use for "automate me", "create/update/refresh my -mode skill", "turn/capture my preferences or working style into a skill", or wanting agents to follow how the user works. | Manual |
| [benchmark-checklist](../skills/benchmark-checklist/SKILL.md) | pstack | dependency | Vet a perf measurement (limiter, tuning, limits, errors, repeatability, relevance, and whether the work happened) before you report or act on it. | Manual |
| [bro](../skills/bro/SKILL.md) | pstack | primary | Restate the last message in plain human language, with no jargon. | Manual |
| [code-review](../skills/code-review/SKILL.md) | mattpocock | dependency | Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes: Standards (does the code follow this repo's documented coding standards?) and Spec (does the code match what the originating issue/spec asked for?). | Passive eligible |
| [codebase-design](../skills/codebase-design/SKILL.md) | mattpocock | dependency | Shared vocabulary for designing deep modules. | Passive eligible |
| [control-cli](../skills/control-cli/SKILL.md) | cursor-team-kit | dependency | Build or adapt a local harness to drive, inspect, and profile an interactive CLI or TUI without external services. | Passive eligible |
| [control-ui](../skills/control-ui/SKILL.md) | cursor-team-kit | dependency | Build or adapt a local browser/CDP harness to drive and inspect a web, IDE, or Electron UI. | Passive eligible |
| [create-formal-verification-skill](../skills/create-formal-verification-skill/SKILL.md) | pstack | dependency | Generate a project-local skill that formally verifies the code where a bug costs the most and tests reach the least, in any language, with whichever verification tool fits. | Manual |
| [create-verification-skill](../skills/create-verification-skill/SKILL.md) | pstack | dependency | Generate a project-local verification skill that drives your app the way a user does — any language, framework, or platform. | Manual |
| [deslop](../skills/deslop/SKILL.md) | cursor-team-kit | dependency | Remove AI-generated code slop and clean up code style | Passive eligible |
| [diagnosing-bugs](../skills/diagnosing-bugs/SKILL.md) | mattpocock | primary | Diagnosis loop for hard bugs and performance regressions. | Passive eligible |
| [domain-modeling](../skills/domain-modeling/SKILL.md) | mattpocock | primary | Build and sharpen a project's domain model. | Passive eligible |
| [figure-it-out](../skills/figure-it-out/SKILL.md) | pstack | dependency | Design an auditable playbook when no narrower one fits: a large migration, an ambitious multi-part change, or work a human reviews after stepping away. | Manual |
| [grill-me](../skills/grill-me/SKILL.md) | mattpocock | primary | A relentless interview to sharpen a plan or design. | Manual |
| [grill-with-docs](../skills/grill-with-docs/SKILL.md) | mattpocock | primary | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go. | Manual |
| [grilling](../skills/grilling/SKILL.md) | mattpocock | primary | Grill the user relentlessly about a plan, decision, or idea. | Passive eligible |
| [handoff](../skills/handoff/SKILL.md) | mattpocock | primary | Compact the current conversation into a handoff document for another agent to pick up. | Manual |
| [how](../skills/how/SKILL.md) | pstack | dependency | Use for "how does X work", code walkthroughs before changing something, and placement / ownership / layering questions ("where should this live", "which package owns this", "is this the right layer"). | Manual |
| [implement](../skills/implement/SKILL.md) | mattpocock | primary | Implement a piece of work based on a spec or set of tickets. | Manual |
| [implement-spec](../skills/implement-spec/SKILL.md) | mattpocock | primary | Implement the result of /to-spec and /to-tickets in code. | Manual |
| [improve-codebase-architecture](../skills/improve-codebase-architecture/SKILL.md) | mattpocock | primary | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. | Manual |
| [in-your-own-words](../skills/in-your-own-words/SKILL.md) | pstack | dependency | Restate in your own words what you think the user's goals are and what problem they're trying to solve. | Manual |
| [interrogate](../skills/interrogate/SKILL.md) | pstack | dependency | Use for "interrogate", "adversarial review", "multi-model review", "challenge this", "stress test this code", "find blind spots", or "tear this apart". | Manual |
| [ketchup](../skills/ketchup/SKILL.md) | pstack | primary | Catch the user up on what changed in this chat since their last message, in plain words and small visuals. | Manual |
| [ketchup-video](../skills/ketchup-video/SKILL.md) | pstack | primary | Catch the user up like /ketchup, with a short subtitled video of slides for what happened and the waiting calls as text under it. | Manual |
| [maintain-formal-verification-skill](../skills/maintain-formal-verification-skill/SKILL.md) | pstack | dependency | Bring a project's formal verification back in line with the code after the code changes: find the commits that touched verified code, update the model, harness, or properties to describe the code as it is now, rerun, and say whether each failure is drift in the verification or a bug in the code. | Manual |
| [maintain-verification-skill](../skills/maintain-verification-skill/SKILL.md) | pstack | dependency | Periodic pass that keeps a project's verification skill and feature map honest: parallel source readers per feature, one live session driving every feature, at most one PR of proven corrections. | Manual |
| [no-comments](../skills/no-comments/SKILL.md) | pstack | dependency | Spawn Comment Sicko, fix accepted findings, and offer encodings for claimed constraints. | Manual |
| [poteto-mode](../skills/poteto-mode/SKILL.md) | pstack | dependency | poteto's agent style for concise, detailed responses, deliberate subagents, unslopped prose, simple code, and verified work. | Manual |
| [pr](../skills/pr/SKILL.md) | mattpocock | primary | Use when writing a PR body. | Passive eligible |
| [principle-attack-the-premise](../skills/principle-attack-the-premise/SKILL.md) | pstack | dependency | Apply when two or more fixes that share one premise have failed the same gate. | Manual |
| [principle-boundary-discipline](../skills/principle-boundary-discipline/SKILL.md) | pstack | dependency | Apply when wiring validation, error handling, or framework adapters. | Manual |
| [principle-build-the-lever](../skills/principle-build-the-lever/SKILL.md) | pstack | dependency | Apply to any non-trivial work, not just bulk work: edits, migrations, analyses, checks. | Manual |
| [principle-encode-lessons-in-structure](../skills/principle-encode-lessons-in-structure/SKILL.md) | pstack | dependency | Apply when you catch yourself writing the same instruction a second time, or notice a recurring correction. | Manual |
| [principle-exhaust-the-design-space](../skills/principle-exhaust-the-design-space/SKILL.md) | pstack | dependency | Apply when facing a novel UI interaction or architectural decision with no precedent in the codebase. | Manual |
| [principle-experience-first](../skills/principle-experience-first/SKILL.md) | pstack | dependency | Apply when product, UX, or feature-scope tradeoffs come up. | Manual |
| [principle-explain-the-number](../skills/principle-explain-the-number/SKILL.md) | pstack | dependency | Apply before you measure, and before you trust, report, or act on a number you measured: a speedup, a regression, a throughput, a latency, or an eval result. | Manual |
| [principle-fix-root-causes](../skills/principle-fix-root-causes/SKILL.md) | pstack | dependency | Apply when debugging. | Manual |
| [principle-foundational-thinking](../skills/principle-foundational-thinking/SKILL.md) | pstack | dependency | Apply before writing logic: choosing core types and data structures, sequencing scaffold-vs-feature work, asking what concurrent actors share. | Manual |
| [principle-guard-the-context-window](../skills/principle-guard-the-context-window/SKILL.md) | pstack | dependency | Apply when context is filling up: large outputs, long files, repeated reads, fan-out planning. | Manual |
| [principle-laziness-protocol](../skills/principle-laziness-protocol/SKILL.md) | pstack | dependency | Apply when refactoring, evaluating diff size, or tempted to add abstractions, layers, or signal threading. | Manual |
| [principle-make-operations-idempotent](../skills/principle-make-operations-idempotent/SKILL.md) | pstack | dependency | Apply when designing commands, lifecycle steps, or processing loops that run amid crashes, restarts, and retries. | Manual |
| [principle-migrate-callers-then-delete-legacy-apis](../skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md) | pstack | dependency | Apply when introducing a new internal API while old callers still exist. | Manual |
| [principle-minimize-reader-load](../skills/principle-minimize-reader-load/SKILL.md) | pstack | dependency | Apply when reviewing or shaping code that's hard to trace. | Manual |
| [principle-model-the-domain](../skills/principle-model-the-domain/SKILL.md) | pstack | dependency | Apply when writing stateful logic, or when code branches a lot or repeats a shape assumption across files. | Manual |
| [principle-never-block-on-the-human](../skills/principle-never-block-on-the-human/SKILL.md) | pstack | dependency | Apply when tempted to ask 'should I do X?' on reversible work. | Manual |
| [principle-outcome-oriented-execution](../skills/principle-outcome-oriented-execution/SKILL.md) | pstack | dependency | Apply during planned rewrites and migrations with explicit phase boundaries. | Manual |
| [principle-prove-it-works](../skills/principle-prove-it-works/SKILL.md) | pstack | dependency | Apply after completing a task, before declaring done. | Manual |
| [principle-redesign-from-first-principles](../skills/principle-redesign-from-first-principles/SKILL.md) | pstack | dependency | Apply when integrating a new requirement into an existing design. | Manual |
| [principle-separate-before-serializing-shared-state](../skills/principle-separate-before-serializing-shared-state/SKILL.md) | pstack | dependency | Apply when concurrent actors might write to the same file, branch, key, or state object. | Manual |
| [principle-sequence-verifiable-units](../skills/principle-sequence-verifiable-units/SKILL.md) | pstack | dependency | Apply to multi-step work (sweeps, migrations, runs of similar edits) and to how you stack commits and PRs. | Manual |
| [principle-subtract-before-you-add](../skills/principle-subtract-before-you-add/SKILL.md) | pstack | dependency | Apply when sequencing an addition, refactor, or rewrite. | Manual |
| [principle-test-behavior-not-implementation](../skills/principle-test-behavior-not-implementation/SKILL.md) | pstack | dependency | Apply when you write, change, or keep a test. | Manual |
| [principle-type-system-discipline](../skills/principle-type-system-discipline/SKILL.md) | pstack | dependency | Apply when designing types, reviewing a function signature, or writing code in any statically-typed language. | Manual |
| [prototype](../skills/prototype/SKILL.md) | mattpocock | primary | Build a throwaway prototype to answer a design question. | Passive eligible |
| [recall](../skills/recall/SKILL.md) | pstack | primary | Reconstruct your recent working context from your own chat history, live state, and the shared record (user reports, prior fixes, incidents), then hand back a tight current-state brief. | Manual |
| [reflect](../skills/reflect/SKILL.md) | pstack | dependency | Spawn three parallel review subagents over the active transcript, surface learnings, and route each to a concrete edit on an existing skill. | Manual |
| [research](../skills/research/SKILL.md) | mattpocock | primary | Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. | Passive eligible |
| [retro](../skills/retro/SKILL.md) | mattpocock | primary | Conduct a retrospective on a coding session. | Manual |
| [setup-matt-pocock-skills](../skills/setup-matt-pocock-skills/SKILL.md) | mattpocock | primary | Configure this repo for the engineering skills: set up its issue tracker, triage label vocabulary, and domain doc layout. | Manual |
| [setup-pstack](../skills/setup-pstack/SKILL.md) | pstack | dependency | Configure which models pstack uses per role and at what reasoning budget. | Passive eligible |
| [sharpen](../skills/sharpen/SKILL.md) | pstack | primary | Make a task deeper, not bigger, then rewrite the prompt. | Manual |
| [show-me-your-work](../skills/show-me-your-work/SKILL.md) | pstack | dependency | Keep a reviewable decision trail for long-running or unattended work: a TSV log with one row per decision (what, why, evidence, result). | Manual |
| [statechart](../skills/statechart/SKILL.md) | pstack | dependency | Check a TLA+ model of a system that moves between states, such as a product flow, a protocol, or a service, and draw it as a Mermaid statechart. | Manual |
| [swarm](../skills/swarm/SKILL.md) | pstack | dependency | Fan out N parallel workers, drain them, and return one report. | Manual |
| [tdd](../skills/tdd/SKILL.md) | mattpocock | dependency | Test-driven development. | Passive eligible |
| [technical-writing](../skills/technical-writing/SKILL.md) | pstack | dependency | Layered technical-writing standard: Diátaxis structure, Google developer style sentences, STE instruction rules, Global English syntax. | Manual |
| [to-questionnaire](../skills/to-questionnaire/SKILL.md) | mattpocock | primary | Turn a decision you can't fully answer into a questionnaire for someone else to fill in. | Manual |
| [to-spec](../skills/to-spec/SKILL.md) | mattpocock | primary | Turn the current conversation into a spec and publish it to the project issue tracker: no interview, just synthesis of what you've already discussed. | Manual |
| [to-tickets](../skills/to-tickets/SKILL.md) | mattpocock | primary | Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, published to the configured tracker (edges as text in one file per ticket locally, or native blocking links on a real tracker). | Manual |
| [triage](../skills/triage/SKILL.md) | mattpocock | primary | Move issues and external PRs through a state machine of triage roles, categorise, verify, grill if needed, and write agent-ready briefs. | Manual |
| [typescript-best-practices](../skills/typescript-best-practices/SKILL.md) | pstack | dependency | TypeScript best practices. | Manual |
| [unslop](../skills/unslop/SKILL.md) | pstack | dependency | Cut AI tells from any writing. | Manual |
| [verify-this](../skills/verify-this/SKILL.md) | cursor-team-kit | dependency | Verify a claim with fresh local evidence: restate it falsifiably, capture baseline and treatment, compare artifacts, and return VERIFIED, NOT VERIFIED, or INCONCLUSIVE. | Passive eligible |
| [wait-what](../skills/wait-what/SKILL.md) | mattpocock | primary | Stop. | Manual |
| [wayfinder](../skills/wayfinder/SKILL.md) | mattpocock | primary | Plan a huge chunk of work (more than one agent session can hold) as a shared map of decision tickets on your issue tracker, and resolve them one at a time until the way to the destination is clear. | Manual |
| [weekly-review](../skills/weekly-review/SKILL.md) | cursor-team-kit | primary | Produce a weekly synthesis of authored commits with highlights by bugfix, tech debt, and net-new work | Passive eligible |
| [what-did-i-get-done](../skills/what-did-i-get-done/SKILL.md) | cursor-team-kit | primary | Summarize authored commits over a user-specified time period into a concise update | Passive eligible |
| [why](../skills/why/SKILL.md) | pstack | dependency | Use for 'why does X work this way', 'why we picked Y', design rationale, regressions, postmortems, or data-backed thresholds. | Manual |
| [wizard](../skills/wizard/SKILL.md) | mattpocock | primary | Generate an interactive bash wizard that walks a human through steps only they can perform. | Passive eligible |
| [workflow-from-chats](../skills/workflow-from-chats/SKILL.md) | cursor-team-kit | primary | Extract durable working preferences from recent Cursor chats and convert them into skills, rules, or workflow docs. | Passive eligible |
| [writing-for-agents](../skills/writing-for-agents/SKILL.md) | mattpocock | primary | Writing documents for agents. | Passive eligible |
