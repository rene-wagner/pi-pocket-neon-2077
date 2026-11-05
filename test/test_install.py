"""Exercise install.sh without touching live Pi Pocket data."""

import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


REPOSITORY = Path(__file__).resolve().parents[1]
THEME_FILES = ("theme.json", "colors.toml", "interface.css", "theme.css")


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="neon-2077-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "theme source"
        self.source.mkdir()
        for name in (*THEME_FILES, "install.sh", "fonts.css"):
            shutil.copy2(REPOSITORY / name, self.source / name)
        self.home = self.root / "test home"
        self.home.mkdir()
        self.env = os.environ.copy()
        self.env["HOME"] = str(self.home)
        self.env.pop("PI_POCKET_DIR", None)

    def install(self, pocket_dir=None, check=True):
        env = self.env.copy()
        if pocket_dir is not None:
            env["PI_POCKET_DIR"] = str(pocket_dir)
        return subprocess.run(
            ["bash", str(self.source / "install.sh")],
            cwd=self.root,
            env=env,
            capture_output=True,
            text=True,
            check=check,
        )

    def assert_theme_files(self, destination):
        for name in THEME_FILES:
            with self.subTest(file=name):
                self.assertEqual(
                    (destination / name).read_bytes(),
                    (self.source / name).read_bytes(),
                )
        self.assertEqual(
            {path.name for path in destination.iterdir()},
            {*THEME_FILES, "fonts.css"},
        )

    def test_default_location_from_another_working_directory(self):
        result = self.install()
        destination = self.home / ".pi-pocket" / "themes" / "neon-2077"
        self.assert_theme_files(destination)
        self.assertIn(str(destination), result.stdout)
        self.assertEqual((destination / "fonts.css").read_bytes(), b"")

    def test_custom_location_with_spaces(self):
        pocket = self.root / "custom pocket data"
        self.install(pocket)
        self.assert_theme_files(pocket / "themes" / "neon-2077")
        self.assertFalse((self.home / ".pi-pocket").exists())

    def test_relative_custom_location(self):
        self.install("relative pocket data")
        self.assert_theme_files(
            self.root / "relative pocket data" / "themes" / "neon-2077"
        )

    def test_empty_override_uses_default_location(self):
        self.install("")
        self.assert_theme_files(self.home / ".pi-pocket" / "themes" / "neon-2077")

    def test_update_replaces_theme_files_and_preserves_personal_files(self):
        pocket = self.root / "custom pocket data"
        self.install(pocket)
        destination = pocket / "themes" / "neon-2077"
        personal_fonts = b":root { --sans: system-ui !important; }\n"
        (destination / "fonts.css").write_bytes(personal_fonts)
        (destination / "notes.txt").write_text("Keep this file.\n")
        for name in THEME_FILES:
            (destination / name).write_text("old version\n")
        self.install(pocket)
        for name in THEME_FILES:
            self.assertEqual(
                (destination / name).read_bytes(), (self.source / name).read_bytes()
            )
        self.assertEqual((destination / "fonts.css").read_bytes(), personal_fonts)
        self.assertEqual((destination / "notes.txt").read_text(), "Keep this file.\n")

    def test_repeated_install_is_idempotent(self):
        self.install()
        destination = self.home / ".pi-pocket" / "themes" / "neon-2077"
        before = {path.name: path.read_bytes() for path in destination.iterdir()}
        self.install()
        after = {path.name: path.read_bytes() for path in destination.iterdir()}
        self.assertEqual(before, after)

    def test_missing_source_fails_before_changing_installation(self):
        for name in THEME_FILES:
            with self.subTest(file=name):
                source = self.source / name
                content = source.read_bytes()
                source.unlink()
                try:
                    result = self.install(check=False)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn(name, result.stderr)
                    self.assertFalse((self.home / ".pi-pocket").exists())
                finally:
                    source.write_bytes(content)


if __name__ == "__main__":
    unittest.main()
