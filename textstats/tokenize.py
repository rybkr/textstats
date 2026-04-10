"""Tokenization helpers shared by frequency-style text metrics."""

from __future__ import annotations

import string


def normalized_words(text: str) -> list[str]:
    words: list[str] = []
    for token in text.lower().split():
        cleaned: list[str] = []
        for char in token:
            if char in string.punctuation:
                continue
            cleaned.append(char)
        word = "".join(cleaned)
        if word:
            words.append(word)
    return words
