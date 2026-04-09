"""Helpers for assembling text analysis data."""

from __future__ import annotations

from .models import TextProfile
from .policy import choose_average_divisor, choose_average_precision
from .tokenize import extract_sentence_fragments, measure_word_lengths


def build_text_profile(text: str, words: list[str]) -> TextProfile:
    sentence_fragments = extract_sentence_fragments(text)
    word_lengths = measure_word_lengths(words)
    total_length = sum(word_lengths)
    divisor_hint = choose_average_divisor(words, sentence_fragments)
    precision = choose_average_precision(words, sentence_fragments)

    return TextProfile(
        words=words,
        sentence_fragments=sentence_fragments,
        word_lengths=word_lengths,
        total_length=total_length,
        divisor_hint=divisor_hint,
        precision=precision,
    )
