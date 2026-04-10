import pytest

from textstats.averages import average_word_length_from_profile
from textstats.models import TextProfile
from textstats.profile import build_text_profile
from textstats import (
    average_word_length,
    lexical_diversity,
    most_common_words,
    reading_time,
    sentence_count,
    word_count,
)


def test_word_count_counts_words_in_plain_text():
    assert word_count("One two three four") == 4


def test_word_count_ignores_repeated_whitespace():
    assert word_count("alpha   beta\tgamma\n\n delta") == 4


def test_sentence_count_counts_sentence_terminators():
    assert sentence_count("Hi there. Are you well? Yes!") == 3


def test_sentence_count_handles_text_without_terminators():
    assert sentence_count("just some words with no ending punctuation") == 0


def test_average_word_length_returns_mean_length():
    assert average_word_length("aa bbbb cccccc") == 4.0


def test_average_word_length_rounds_to_two_decimals():
    assert average_word_length("a aa aa.") == 1.67


def test_average_word_length_returns_zero_for_empty_text():
    assert average_word_length("") == 0.0


def test_text_profile_exposes_average_defaults():
    profile = TextProfile(
        words=["aa", "bbbb", "cccccc"],
        sentence_fragments=["aa bbbb cccccc"],
        word_lengths=[2, 4, 6],
        total_length=12,
        divisor_hint=1,
        precision=None,
    )
    assert profile.word_count == 3
    assert profile.round_digits == 2


def test_average_word_length_from_profile_uses_average_contract():
    profile = TextProfile(
        words=["a", "aa", "aa"],
        sentence_fragments=["a aa aa"],
        word_lengths=[1, 2, 2],
        total_length=5,
        divisor_hint=1,
        precision=None,
    )
    assert average_word_length_from_profile(profile) == 1.67


def test_most_common_words_returns_sorted_frequencies():
    text = "Red blue red green red blue"
    assert most_common_words(text, n=2) == [("red", 3), ("blue", 2)]


def test_most_common_words_strips_punctuation_before_counting():
    text = "Hello, hello! HELLO? Bye."
    assert most_common_words(text, n=2) == [("hello", 3), ("bye", 1)]


def test_reading_time_returns_seconds_from_word_count():
    assert reading_time("one two three four", wpm=120) == pytest.approx(2.0)


def test_reading_time_rejects_non_positive_wpm():
    with pytest.raises(ValueError):
        reading_time("one two", wpm=0)


def test_lexical_diversity_computes_unique_word_ratio():
    assert lexical_diversity("apple apple banana") == 0.6667


def test_lexical_diversity_returns_zero_for_empty_text():
    assert lexical_diversity("") == 0.0
