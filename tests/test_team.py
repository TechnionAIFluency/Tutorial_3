"""CI check for the team folder: every number must be computed, not guessed."""
import unittest
from pathlib import Path

from cooling import minutes_to_cool

TEAM = Path(__file__).resolve().parent.parent / "team"


def read_entry(path):
    """'key: value' lines -> dict."""
    entry = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            entry[key.strip()] = value.strip()
    return entry


class TestTeam(unittest.TestCase):
    def test_every_entry(self):
        files = sorted(TEAM.glob("*.txt"))
        self.assertTrue(files, "team/ has no .txt files")
        for path in files:
            with self.subTest(file=path.name):
                entry = read_entry(path)
                for field in ("name", "start", "minutes"):
                    if field not in entry:
                        self.fail(f"{path.name}: missing the line '{field}: ...'")
                try:
                    start, written = float(entry["start"]), float(entry["minutes"])
                except ValueError:
                    self.fail(f"{path.name}: start and minutes must be numbers")
                if not 70 <= start <= 95:
                    self.fail(f"{path.name}: start must be from 70 to 95, not {start:g}")
                real = minutes_to_cool(start, 60)
                if abs(written - real) > 0.005:
                    self.fail(f"{path.name}: you wrote minutes = {written:g}, but cooling.py says "
                              f"{real:.2f} for start = {start:g}.\n"
                              f"Compute it: python3 cooling.py --start {start:g}")


if __name__ == "__main__":
    unittest.main()
