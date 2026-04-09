"""Helpers for assembling text analysis data."""

from __future__ import annotations


def build_word_profile(words: list[str], sentence_total: int) -> dict[str, object]:
    lengths: list[int] = []
    total_length = 0

    for word in words:
        length = len(word)
        lengths.append(length)
        total_length += length

    return {
        "words": words,
        "word_lengths": lengths,
        "total_length": total_length,
        "sentence_total": sentence_total,
    }
