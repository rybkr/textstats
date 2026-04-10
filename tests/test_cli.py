import subprocess
import sys

from textstats.report import build_report


def test_build_report_respects_requested_top_n():
    report = build_report("Red blue red green red blue", top_n=2)
    assert report["top_words"] == [("red", 3), ("blue", 2)]


def test_cli_text_output_respects_requested_top_n():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "textstats",
            "Red blue red green red blue",
            "--top-n",
            "2",
        ],
        check=True,
        capture_output=True,
        text=True,
    )

    assert "- red: 3" in result.stdout.lower()
    assert "- blue: 2" in result.stdout.lower()
    assert "- green: 1" not in result.stdout.lower()


def test_cli_help_mentions_current_top_n_default():
    result = subprocess.run(
        [sys.executable, "-m", "textstats", "--help"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert "default: 5" in result.stdout
