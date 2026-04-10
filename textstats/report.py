"""Helpers for building and rendering text summaries."""

from __future__ import annotations

from .core import most_common_words, sentence_count, word_count

DEFAULT_TOP_N = 5


def build_report(text: str, top_n: int = DEFAULT_TOP_N) -> dict[str, object]:
    if top_n <= 0:
        raise ValueError("top_n must be greater than 0")

    return {
        "word_count": word_count(text),
        "sentence_count": sentence_count(text),
        "top_words": most_common_words(text),
    }


def render_text_report(report: dict[str, object]) -> str:
    lines = [
        f"Words: {report['word_count']}",
        f"Sentences: {report['sentence_count']}",
        "Top words:",
    ]
    for word, count in report["top_words"]:
        lines.append(f"- {word}: {count}")
    return "\n".join(lines)
