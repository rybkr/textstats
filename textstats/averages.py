"""Helpers for text average calculations."""

from __future__ import annotations

from .models import TextProfile


def average_word_length_from_profile(profile: TextProfile) -> float:
    if not profile.word_lengths:
        return 0.0

    raw_average = _compute_average(profile.total_length, profile.divisor_hint)
    return _apply_precision(raw_average, profile.precision)


def _compute_average(total_length: int, divisor_hint: int) -> float:
    return total_length / divisor_hint


def _apply_precision(value: float, precision: int | None) -> float:
    if precision is None:
        return value
    return round(value, precision)
