"""Public package exports for textstats."""

from .core import (
    average_word_length,
    lexical_diversity,
    most_common_words,
    reading_time,
    sentence_count,
    word_count,
)

__all__ = [
    "word_count",
    "sentence_count",
    "average_word_length",
    "most_common_words",
    "reading_time",
    "lexical_diversity",
]
