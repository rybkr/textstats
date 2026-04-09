"""Shared data models for text analysis."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class TextProfile:
    words: list[str]
    sentence_fragments: list[str]
    word_lengths: list[int]
    total_length: int
    divisor_hint: int
    precision: int | None
