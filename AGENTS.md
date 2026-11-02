# Skills source maintenance

Read `docs/collisions-and-overlaps.md` before changing imported personal workflows.
Preserve imported skill names, upstream instructions, licenses, and recorded hashes.
`imports/personal-skills.lock.json` owns the 85 imported primary/dependency skills and their required dependency graph.
Existing brain-suite skills remain one deployment unit; do not replace their routing contract.

Run `npm run skills:validate`, `npm test`, and `npm run typecheck` for changes.
Never use the live brain vault for mutating tests. Keep generated evaluation workspaces outside
this repository. Source directories are not permission to alter installed personal skills.
