#!/usr/bin/env python3
"""Validate imported provenance, invocation policies, and unique skill names."""

import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import yaml


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "quick_validate", ROOT / "skills/skill-creator/scripts/quick_validate.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


def main():
    manifest = json.loads((ROOT / "imports/personal-skills.lock.json").read_text())
    errors = []
    names = {}
    for path in sorted((ROOT / "skills").glob("*/SKILL.md")):
        meta = yaml.safe_load(path.read_text().split("---", 2)[1])
        name = meta.get("name")
        if name != path.parent.name or name in names:
            errors.append(f"Skill name collision or directory mismatch: {path}")
        names[name] = path
    local_path = ROOT / "local-skills.json"
    local = json.loads(local_path.read_text()) if local_path.is_file() else {}
    for name, record in local.items():
        result = validator.validate_skill(ROOT / record["path"])
        if not result[0]:
            errors.append(f"{name}: {result[1]}")
        for dependency in record["requires"]:
            if dependency not in names:
                errors.append(f"Missing local skill dependency: {name} -> {dependency}")
    for collection in ("sha256", "generated_metadata"):
        for relative, expected in manifest[collection].items():
            path = ROOT / relative
            if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
                errors.append(f"Imported file differs from recorded snapshot: {relative}")
    if manifest["version"] != 2:
        errors.append("Expected dependency-aware import manifest version 2")
    for name, dependencies in manifest["requires"].items():
        if name not in manifest["skills"]:
            errors.append(f"Unknown workflow in dependency graph: {name}")
        for dependency in dependencies:
            if dependency not in names:
                errors.append(f"Missing required skill: {name} -> {dependency}")
    for capability, provider in manifest["host_capabilities"].items():
        if provider not in names:
            errors.append(f"Missing host capability provider: {capability} -> {provider}")
    for name, record in manifest["skills"].items():
        path = ROOT / "skills" / name
        result = validator.validate_skill(path)
        if not result[0]:
            errors.append(f"{name}: {result[1]}")
            continue
        meta = yaml.safe_load((path / "SKILL.md").read_text().split("---", 2)[1])
        if meta.get("disable-model-invocation"):
            policy_path = path / "agents/openai.yaml"
            policy = yaml.safe_load(policy_path.read_text()) if policy_path.is_file() else {}
            if policy.get("policy", {}).get("allow_implicit_invocation") is not False:
                errors.append(f"Explicit-only skill lacks Codex policy: {name}")
        tracked = {str((ROOT / relative).relative_to(path))
                   for collection in ("sha256", "generated_metadata")
                   for relative in manifest[collection] if (ROOT / relative).is_relative_to(path)}
        actual = {str(p.relative_to(path)) for p in path.rglob("*")
                  if p.is_file() and not {"__pycache__", "node_modules"}.intersection(p.parts)}
        if actual != tracked:
            errors.append(f"Unrecorded or missing imported files for {name}: {sorted(actual ^ tracked)}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Verified {len(manifest['skills'])} imported skills, {len(names)} unique installed names, "
          "upstream hashes, and explicit-only policies.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
