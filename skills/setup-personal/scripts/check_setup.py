#!/usr/bin/env python3
"""Observe personal setup artifacts. No writes, subprocesses, network, or vault repairs."""

import argparse
import json
import os
from pathlib import Path
import re


BRAIN_SUITE = ['brain', 'brain-contextualize', 'brain-recall', 'brain-remember',
               'brain-consolidate', 'brain-synthesize', 'brain-build']
ROUTERS = ['index.md', 'wikis.md', 'projects.md', 'workspaces.md', 'tools.md',
           'decisions.md', 'gotchas.md', 'codestyle.md', 'improvements.md']
MODEL_PATHS = {'codex': '.agents/pstack-models.md', 'claude': '.claude/pstack-models.md',
               'cursor': '.cursor/rules/pstack-models.mdc', 'opencode': '.opencode/pstack-models.md'}


def read(path):
    try:
        return path.read_text(encoding='utf-8')
    except (OSError, UnicodeError):
        return None


def file_status(path):
    try:
        exists = path.exists()
    except OSError:
        return 'unknown'
    if not exists:
        return 'missing'
    value = read(path)
    if value is None:
        return 'unknown'
    if not value.strip() or re.search(r'\b(TODO|TBD|FIXME)\b', value):
        return 'incomplete'
    return 'present-unverified'


def relative_markdown(value):
    return (isinstance(value, str) and bool(value) and not Path(value).is_absolute()
            and '..' not in value.replace('\\', '/').split('/') and value.lower().endswith('.md'))


def inspect_setup(*, home, config_home, host, brain_dir=None, attribution_dir=None,
                  project=None, host_instructions=None, triage_installed=False, codex_home=None):
    rows = []

    def add(area, scope, status, evidence, next_action):
        rows.append({'area': area, 'scope': scope, 'status': status,
                     'evidence': evidence, 'next_action': next_action})

    if brain_dir:
        manifest = read(Path(brain_dir) / 'references/suite-manifest.json')
        try:
            manifest = json.loads(manifest or '{}')
            valid = (manifest.get('suiteVersion') == 2 and manifest.get('contractVersion') == 2
                     and manifest.get('foundation') == 'brain' and manifest.get('skills') == BRAIN_SUITE)
        except (ValueError, AttributeError):
            valid = False
        add('brain_suite', 'personal', 'present-unverified' if valid else 'incomplete',
            'Manifest at the exact supplied brain resource directory',
            'Resolve all seven operators through the native loader and verify one suite/contract version.')
    else:
        add('brain_suite', 'personal', 'unknown', 'No native-loader brain directory supplied',
            'Resolve brain through the host catalog; do not search parent skill directories.')

    config_path = Path(config_home) / 'agent-brain/config.json'
    status = file_status(config_path)
    config, valid = {}, False
    if status == 'present-unverified':
        try:
            config = json.loads(read(config_path))
            vault = config.get('vault', {})
            startup = config.get('startup', {})
            palette = config.get('graph', {}).get('paletteNode')
            valid = (config.get('contractVersion') == 2 and isinstance(vault.get('name'), str)
                     and bool(vault['name'].strip()) and isinstance(vault.get('path'), str)
                     and Path(vault['path']).is_absolute()
                     and relative_markdown(startup.get('primaryContext'))
                     and (palette is None or relative_markdown(palette)))
        except (ValueError, TypeError, AttributeError):
            valid = False
        if not valid:
            status = 'incomplete'
    add('brain_config', 'personal', status, str(config_path),
        'Reuse valid configuration; otherwise collect vault name/path and primary context, then configure brain.')
    if valid:
        vault = Path(config['vault']['path'])
        expected = ROUTERS + [config['startup']['primaryContext']]
        if config.get('graph', {}).get('paletteNode'):
            expected.append(config['graph']['paletteNode'])
        missing = [p for p in expected if not (vault / p).is_file()]
        escaping = [p for p in expected if not (vault / p).resolve().is_relative_to(vault.resolve())]
        state = 'incomplete' if missing or escaping else 'present-unverified'
        evidence = ('Missing: ' + ', '.join(missing)) if missing else 'Configured root routers and context are present'
        if escaping:
            evidence += '; configured paths escape the vault'
        add('brain_vault', 'personal', state, evidence,
            'Run the read-only strict brain audit; use brain-consolidate for existing-vault repair. No automatic migration.')
    else:
        add('brain_vault', 'personal', 'needs-input', 'No valid configured vault to inspect',
            'Choose a vault explicitly; never infer or create one from nearby directories.')

    if host_instructions:
        instruction = Path(host_instructions)
    elif host == 'codex':
        instruction = Path(codex_home or Path(home) / '.codex') / 'AGENTS.md'
    elif host == 'claude':
        instruction = Path(home) / '.claude/CLAUDE.md'
    elif host == 'opencode':
        instruction = Path(config_home) / 'opencode/AGENTS.md'
    else:
        instruction = None
    if instruction:
        status = file_status(instruction)
        value = read(instruction) or ''
        if status == 'present-unverified' and not all(
                term in value for term in ('brain', 'brain-contextualize', 'compaction')):
            status = 'incomplete'
        add('host_bootstrap', 'personal', status, str(instruction),
            'Merge the short brain startup bootstrap and personal routing pointer; preserve unrelated instructions.')
    else:
        add('host_bootstrap', 'personal', 'unknown', 'Host instruction surface not supplied',
            'Inspect the host-supported user instruction surface; do not invent a Cursor global-file path.')

    if attribution_dir:
        identity = Path(attribution_dir) / 'references/attribution-config.md'
        status = file_status(identity)
        value = read(identity) or ''
        name = re.search(r'^Agent name:\s*`([^`]+)`', value, re.M)
        emoji = re.search(r'^Emoji:\s*`([^`]+)`', value, re.M)
        if status == 'present-unverified' and (not name or not emoji
                or name.group(1).strip() in {'', 'Your Agent Name', 'Agent Name'}
                or emoji.group(1).strip() in {'', 'symbol', 'emoji'}):
            status = 'incomplete'
        add('attribution', 'personal', status, 'Config at the active attribution resource directory',
            'Ask for agent name and emoji only if absent/changing, then run its configure script against the active copy.')
    else:
        add('attribution', 'personal', 'unknown', 'No native-loader attribution directory supplied',
            'Resolve attribution through the active host catalog before configuring its identity.')

    if project is None:
        for area in ('matt_project', 'pstack_project'):
            add(area, 'project', 'not-applicable', 'No explicit --project target',
                'Supply a project path when adopting these project workflows; do not configure the current directory implicitly.')
    else:
        project = Path(project)
        documents = ['docs/agents/issue-tracker.md', 'docs/agents/domain.md']
        if triage_installed:
            documents.append('docs/agents/triage-labels.md')
        states = [(name, file_status(project / name)) for name in documents]
        status = 'present-unverified' if all(s == 'present-unverified' for _, s in states) else 'incomplete'
        add('matt_project', 'project', status, '; '.join(f'{n}: {s}' for n, s in states),
            'Reuse current tracker/domain choices; create missing setup or refresh only the changed project settings.')
        model_file = project / MODEL_PATHS[host]
        add('pstack_project', 'project', file_status(model_file), str(model_file),
            'Validate supported model roles/budget and project instruction wiring; configuration presence does not prove access.')
    add('runtime_capabilities', 'conditional', 'unknown',
        'Accounts, transcripts, diagrams, browsers, Bun/Node/Java, media tools and helper packages were not exercised',
        'Check only capabilities needed by adopted workflows; do not install every optional runtime.')
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--host', required=True, choices=tuple(MODEL_PATHS))
    parser.add_argument('--brain-dir', type=Path)
    parser.add_argument('--attribution-dir', type=Path)
    parser.add_argument('--project', type=Path)
    parser.add_argument('--host-instructions', type=Path)
    parser.add_argument('--triage-installed', action='store_true')
    args = parser.parse_args()
    if args.project and not args.project.is_dir():
        parser.error('--project must name an existing project directory')
    home = Path.home()
    config_home = Path(os.environ.get('XDG_CONFIG_HOME') or home / '.config')
    rows = inspect_setup(home=home, config_home=config_home, host=args.host, brain_dir=args.brain_dir,
                         attribution_dir=args.attribution_dir, project=args.project,
                         host_instructions=args.host_instructions, triage_installed=args.triage_installed,
                         codex_home=os.environ.get('CODEX_HOME'))
    print(json.dumps({'mode': 'check-only', 'checks': rows}, indent=2))


if __name__ == '__main__':
    main()
