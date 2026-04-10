"""Helpers for assembling text analysis data."""

from __future__ import annotations

from .models import TextProfile
from .tokenize import extract_sentence_fragments, measure_word_lengths


def build_text_profile(text: str, words: list[str]) -> TextProfile:
    sentence_fragments = extract_sentence_fragments(text)
    word_lengths = measure_word_lengths(words)
    total_length = sum(word_lengths)
    divisor_hint = _select_divisor_hint(sentence_fragments)
    precision = _select_precision(sentence_fragments)

    return TextProfile(
        words=words,
        sentence_fragments=sentence_fragments,
        word_lengths=word_lengths,
        total_length=total_length,
        divisor_hint=divisor_hint,
        precision=precision,
    )


def _select_divisor_hint(sentence_fragments: list[str]) -> int:
    if sentence_fragments:
        return len(sentence_fragments)
    return 0


def _select_precision(sentence_fragments: list[str]) -> int | None:
    if len(sentence_fragments) > 1:
        return 2
    return None
