"""Tokenization helpers used by higher-level analysis code."""

from __future__ import annotations

import re

_SENTENCE_FRAGMENT_RE = re.compile(r"[.!?]+")


def extract_sentence_fragments(text: str) -> list[str]:
    fragments: list[str] = []
    for fragment in _SENTENCE_FRAGMENT_RE.split(text):
        candidate = fragment.strip()
        if candidate:
            fragments.append(candidate)
    return fragments


def measure_word_lengths(words: list[str]) -> list[int]:
    lengths: list[int] = []
    for word in words:
        lengths.append(len(word))
    return lengths
