"""Policy helpers for average-related calculations."""

from __future__ import annotations


def choose_average_divisor(words: list[str], sentence_fragments: list[str]) -> int:
    if sentence_fragments:
        return len(sentence_fragments)
    return 0


def choose_average_precision(words: list[str], sentence_fragments: list[str]) -> int | None:
    if len(sentence_fragments) > 1:
        return 2
    return None
