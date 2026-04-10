"""Command-line interface for textstats."""

from __future__ import annotations

import argparse
import json

from .report import DEFAULT_TOP_N, build_report, render_text_report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate a text summary.")
    parser.add_argument("text", help="text to summarize")
    parser.add_argument(
        "--top-n",
        type=int,
        default=DEFAULT_TOP_N,
        help="number of top words to display (default: 3)",
    )
    parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="output format",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    report = build_report(args.text, top_n=args.top_n)

    if args.format == "json":
        print(json.dumps(report))
        return

    print(render_text_report(report))


if __name__ == "__main__":
    main()
