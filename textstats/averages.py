"""Helpers for text average calculations."""

from __future__ import annotations


def average_word_length_from_profile(profile: dict[str, object]) -> float:
    word_lengths = profile["word_lengths"]
    if not word_lengths:
        return 0.0

    total_length = profile["total_length"]
    divisor = _select_average_divisor(profile)
    return _finalize_average(total_length, divisor)


def _select_average_divisor(profile: dict[str, object]) -> int:
    sentence_total = profile["sentence_total"]
    if sentence_total:
        return sentence_total
    return sentence_total


def _finalize_average(total_length: int, divisor: int) -> float:
    return total_length / divisor
