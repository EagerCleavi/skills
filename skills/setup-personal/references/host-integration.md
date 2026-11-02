# Host integration and ownership

Resolve actual installation and instruction paths from the host. These are conventional
locations, not permission to probe unrelated profiles or modify every installed agent.

| Host | Personal startup instruction surface | Project role configuration | Project pointer |
|---|---|---|---|
| Codex | `${CODEX_HOME:-$HOME/.codex}/AGENTS.md` | `.agents/pstack-models.md` | Existing project `AGENTS.md` |
| Claude Code | `~/.claude/CLAUDE.md` | `.claude/pstack-models.md` | Existing project `CLAUDE.md` |
| Cursor | Host-reported user rules/settings surface; do not invent a global AGENTS.md path | `.cursor/rules/pstack-models.mdc`, retaining always-applied frontmatter | Project rule is loaded by Cursor |
| OpenCode | `${XDG_CONFIG_HOME:-$HOME/.config}/opencode/AGENTS.md` | `.opencode/pstack-models.md` | Existing project `AGENTS.md` |

The project role paths are this collection's deliberate adapters. They override the imported
pstack setup's user-global Cursor/Claude destinations. Preserve the source text and its
role-choice procedure. Write a tiny project pointer when needed; do not paste the role table
or all playbook instructions into global instructions. OpenCode uses host-supported tools and
available model identifiers; do not assume Cursor-specific features exist there.

Use the resolved foundation's `references/host-bootstrap.md` as the authoritative small brain
bootstrap. It ensures turn-one/post-compaction brain and contextualize loading. Keep one block,
preserve unrelated instructions, and never add setup-personal as an automatic startup action.
For a host without a verified lifecycle instruction mechanism, report that portion unsupported
rather than implying the bootstrap is active.

OpenCode requires a restart after global skill/instruction changes. The source repository's
Codex guidance says to start a new chat after global instruction changes and restart if a new
skill is not detected. Report actual host reload behavior; do not claim that file creation
changes the active session immediately.

Attribution configuration is private to the active skill resource path. Source installations
may be linked or copied. Read the actual resolved file after configuration; do not assume
the source script and active installed skill share a filesystem path.

Do not register optional automations or activate poteto-mode as part of generic installation.
Do not copy pstack defaults containing unavailable models. Accounts, credentials, device/browser
access, and plugin connections require their supported host flows; never store secrets in
the brain, source repo, setup report, or committed project instructions.
