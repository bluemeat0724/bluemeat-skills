"""Run with: python3 agents_md/test_install.py (no network or real home writes)."""

import os
from pathlib import Path
import subprocess
import tempfile


with tempfile.TemporaryDirectory() as temporary:
    root = Path(temporary)
    # Redirect only the script's destination paths; leave HOME unchanged.
    script = Path(__file__).with_name("install.sh").read_text().replace(
        '"$HOME/', '"$TEST_INSTALL_ROOT/'
    )
    curl = root / "curl"
    curl.write_text(
        '#!/bin/sh\n'
        'while [ "$1" != "-o" ]; do shift; done\n'
        'if [ "$TEST_DOWNLOAD" = empty ]; then : > "$2"; exit 0; fi\n'
        'printf "%s\\n" "$TEST_DOWNLOAD" > "$2"\n'
        '[ "$TEST_DOWNLOAD" != failed ]\n'
    )
    curl.chmod(0o755)
    env = dict(os.environ, PATH=f"{root}:{os.environ['PATH']}", TEST_INSTALL_ROOT=str(root))
    targets = [root / directory / "AGENTS.md" for directory in (".agent", ".codex")]

    for mode in ("first", "second", "third", "failed", "empty"):
        result = subprocess.run(
            ["sh"], input=script, text=True, capture_output=True,
            env=dict(env, TEST_DOWNLOAD=mode),
        )
        assert (result.returncode == 0) == (mode not in ("failed", "empty")), result.stderr
        for target in targets:
            assert target.read_text() == (mode if mode in ("first", "second", "third") else "third") + "\n"
            backups = sorted(p.read_text() for p in target.parent.glob("AGENTS.md.bak.*"))
            assert backups == {"first": [], "second": ["first\n"]}.get(mode, ["first\n", "second\n"])
            assert not list(target.parent.glob(".AGENTS.md.*"))

    targets[1].unlink()
    targets[1].symlink_to(targets[0])
    result = subprocess.run(
        ["sh"], input=script, text=True, capture_output=True,
        env=dict(env, TEST_DOWNLOAD="fourth"),
    )
    assert result.returncode != 0
    assert targets[0].read_text() == "third\n"
    assert targets[1].is_symlink()

print("install checks passed")
