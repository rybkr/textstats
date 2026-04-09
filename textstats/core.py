"""Core text statistics helpers."""

from __future__ import annotations

import re
import string
from collections import Counter

_WORD_RE = re.compile(r"\b[\w']+\b")
_SENTENCE_RE = re.compile(r"[.!?]+")


def _words(text: str) -> list[str]:
    return _WORD_RE.findall(text)


def _normalized_words(text: str) -> list[str]:
    words: list[str] = []
    for token in text.lower().split():
        normalized = token.strip(string.punctuation)
        if normalized:
            words.append(normalized)
    return words


def word_count(text: str) -> int:
    """Return the number of words in *text*."""
    return len(text.split())


def sentence_count(text: str) -> int:
    """Return the number of sentences split on ., !, and ?."""
    return len(_SENTENCE_RE.findall(text))


def average_word_length(text: str) -> float:
    """Return the mean word length rounded to two decimal places."""
    words = _words(text)
    if not words:
        return 0.0
    average = sum(len(word) for word in words) / len(words)
    return round(average, 2)


def most_common_words(text: str, n: int = 5) -> list[tuple[str, int]]:
    """Return the *n* most common lowercase words with punctuation stripped."""
    if n <= 0:
        return []
    counts = Counter(_normalized_words(text))
    return counts.most_common(n)


def reading_time(text: str, wpm: int = 200) -> float:
    """Return estimated reading time in seconds."""
    if wpm <= 0:
        raise ValueError("wpm must be greater than 0")
    return (word_count(text) / wpm) * 60.0


def lexical_diversity(text: str) -> float:
    """Return the ratio of unique words to total words rounded to four decimals."""
    words = _normalized_words(text)
    if not words:
        return 0.0
    diversity = len(set(words)) / len(words)
    return round(diversity, 4)
