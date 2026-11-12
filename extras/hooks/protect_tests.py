#!/usr/bin/env python3
"""preToolUse hook: the agent may ADD test files, but may not EDIT committed ones.

The harness runs this script before every tool call and sends the call as JSON
on stdin. If the call would change a test file that Git already tracks, we print
a "deny" decision and the harness blocks the call.
"""
import json
import subprocess
import sys
from pathlib import Path


def paths_in(value):
    """Collect every file path mentioned in the tool arguments."""
    if isinstance(value, str):
        try:
            value = json.loads(value)
        except ValueError:
            return []
    found = []
    if isinstance(value, dict):
        for key, item in value.items():
            if key in ("path", "file_path", "filePath") and isinstance(item, str):
                found.append(item)
            else:
                found += paths_in(item)
    elif isinstance(value, list):
        for item in value:
            found += paths_in(item)
    return found


event = json.load(sys.stdin)
tool = event.get("toolName") or event.get("tool_name") or ""
args = event.get("toolArgs") or event.get("tool_input") or {}
cwd = event.get("cwd") or "."

for path in paths_in(args):
    rel = Path(path)
    if rel.is_absolute():
        try:
            rel = rel.relative_to(Path(cwd).resolve())
        except ValueError:
            continue
    tracked = subprocess.run(["git", "ls-files", "--error-unmatch", str(rel)],
                             cwd=cwd, capture_output=True).returncode == 0
    if rel.parts[:1] == ("tests",) and tracked:
        reason = f"{rel} is a committed test: tests are read-only for the agent."
        print(json.dumps({"permissionDecision": "deny",
                          "permissionDecisionReason": reason}))
        sys.exit(0)

sys.exit(0)  # no output: the call goes ahead
