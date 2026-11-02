"""Isolated personal setup observation tests; no live configs or vaults."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).with_name('check_setup.py')
spec = importlib.util.spec_from_file_location('check_setup', SCRIPT)
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)


class SetupChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.home = self.root / 'home'
        self.config = self.root / 'config'
        self.home.mkdir()
        self.brain = self.root / 'brain-skill'
        self.attribution = self.root / 'attribution-skill'
        (self.brain / 'references').mkdir(parents=True)
        (self.attribution / 'references').mkdir(parents=True)
        (self.brain / 'references/suite-manifest.json').write_text(json.dumps({
            'suiteVersion': 2, 'contractVersion': 2, 'foundation': 'brain',
            'skills': check.BRAIN_SUITE}))

    def inspect(self, **kwargs):
        return {row['area']: row for row in check.inspect_setup(
            home=self.home, config_home=self.config, host='codex',
            brain_dir=self.brain, attribution_dir=self.attribution, **kwargs)}

    def write_config(self, primary='wikis/test/_test.md'):
        vault = self.root / 'vault'
        vault.mkdir(exist_ok=True)
        for name in check.ROUTERS:
            (vault / name).write_text('# Router\n')
        path = vault / 'wikis/test/_test.md'
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text('---\nstatus: active\n---\n# Test\n')
        config = self.config / 'agent-brain/config.json'
        config.parent.mkdir(parents=True, exist_ok=True)
        config.write_text(json.dumps({'contractVersion': 2, 'vault': {'name': 'Test', 'path': str(vault)},
                                     'startup': {'primaryContext': primary}, 'graph': {'paletteNode': None}}))
        return vault, config

    def test_empty_environment_is_missing_and_project_setup_is_not_assumed(self):
        rows = self.inspect()
        self.assertEqual(rows['brain_config']['status'], 'missing')
        self.assertEqual(rows['attribution']['status'], 'missing')
        self.assertEqual(rows['matt_project']['status'], 'not-applicable')
        self.assertEqual(rows['pstack_project']['status'], 'not-applicable')
        self.assertFalse((self.config / 'agent-brain/config.json').exists())

    def test_presence_is_not_success_and_inspection_is_read_only(self):
        self.write_config()
        target = self.attribution / 'references/attribution-config.md'
        target.write_text('# Attribution Config\nAgent name: `Test Agent`\nEmoji: `*`\n')
        before = {str(p): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        first = self.inspect()
        second = self.inspect()
        self.assertEqual(first, second)
        self.assertEqual(first['brain_config']['status'], 'present-unverified')
        self.assertEqual(first['brain_vault']['status'], 'present-unverified')
        self.assertEqual(first['attribution']['status'], 'present-unverified')
        self.assertEqual(before, {str(p): p.read_bytes() for p in self.root.rglob('*') if p.is_file()})

    def test_invalid_config_and_escaping_context_are_rejected(self):
        _, config = self.write_config(primary='../private.md')
        self.assertEqual(self.inspect()['brain_config']['status'], 'incomplete')
        config.write_text('{ broken')
        self.assertEqual(self.inspect()['brain_config']['status'], 'incomplete')
        _, _ = self.write_config()
        payload = json.loads(config.read_text())
        payload['vault']['path'] = {'invalid': 'type'}
        config.write_text(json.dumps(payload))
        self.assertEqual(self.inspect()['brain_config']['status'], 'incomplete')

    def test_partial_vault_is_reported_without_repair(self):
        vault, _ = self.write_config()
        (vault / 'projects.md').unlink()
        rows = self.inspect()
        self.assertEqual(rows['brain_vault']['status'], 'incomplete')
        self.assertIn('projects.md', rows['brain_vault']['evidence'])
        self.assertFalse((vault / 'projects.md').exists())

    def test_project_setup_is_scoped_and_placeholders_are_not_configured(self):
        project = self.root / 'app'
        (project / 'docs/agents').mkdir(parents=True)
        (project / 'docs/agents/issue-tracker.md').write_text('TODO select tracker\n')
        (project / 'docs/agents/domain.md').write_text('Use GLOSSARY.md and docs/adr/.\n')
        (project / '.agents').mkdir()
        (project / '.agents/pstack-models.md').write_text('feature, refactoring: inherit-parent\n')
        rows = self.inspect(project=project, triage_installed=True)
        self.assertEqual(rows['matt_project']['status'], 'incomplete')
        self.assertEqual(rows['pstack_project']['status'], 'present-unverified')
        self.assertFalse((self.home / '.cursor/rules/pstack-models.mdc').exists())

    def test_bootstrap_requires_both_foundation_and_contextualize(self):
        instruction = self.home / '.codex/AGENTS.md'
        instruction.parent.mkdir()
        instruction.write_text('Use brain.\n')
        self.assertEqual(self.inspect()['host_bootstrap']['status'], 'incomplete')
        instruction.write_text('At turn 1 and after compaction invoke brain then brain-contextualize.\n')
        self.assertEqual(self.inspect()['host_bootstrap']['status'], 'present-unverified')

    def test_template_identity_and_mismatched_suite_are_not_ready(self):
        (self.attribution / 'references/attribution-config.md').write_text(
            'Agent name: `Your Agent Name`\nEmoji: `symbol`\n')
        self.assertEqual(self.inspect()['attribution']['status'], 'incomplete')
        (self.brain / 'references/suite-manifest.json').write_text(json.dumps({'suiteVersion': 1}))
        self.assertEqual(self.inspect()['brain_suite']['status'], 'incomplete')

    def test_registry_covers_the_collection_and_dependencies_exist(self):
        source = Path(__file__).resolve().parents[3]
        registry = json.loads((source / 'skills/setup-personal/references/setup-contract.json').read_text())
        names = {p.parent.name for p in (source / 'skills').glob('*/SKILL.md')}
        self.assertEqual(set(registry['skills']), names)
        local = json.loads((source / 'local-skills.json').read_text())['setup-personal']
        required = {n for values in registry['preconditions'].values() for n in values}
        self.assertEqual(set(local['requires']), required)
        self.assertTrue(required <= names)
        self.assertEqual(registry['ownership']['matt'], 'project')
        self.assertEqual(registry['ownership']['pstack'], 'project')


if __name__ == '__main__':
    unittest.main()
