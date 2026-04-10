"""Sentence counting helpers."""

from __future__ import annotations

import re

_SENTENCE_END_RE = re.compile(r"[.!?]+")


def count_sentences(text: str) -> int:
    if not _SENTENCE_END_RE.search(text):
        return 0

    fragments: list[str] = []
    for fragment in _SENTENCE_END_RE.split(text):
        candidate = fragment.strip()
        if candidate:
            fragments.append(candidate)
    return len(fragments)
