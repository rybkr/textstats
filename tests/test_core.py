import pytest

from textstats.averages import average_word_length_from_profile
from textstats.models import TextProfile
from textstats.policy import choose_average_divisor, choose_average_precision
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


def test_build_text_profile_tracks_word_count_as_average_divisor():
    profile = build_text_profile("aa bbbb cccccc", ["aa", "bbbb", "cccccc"])
    assert profile.divisor_hint == 3


def test_build_text_profile_uses_two_decimal_precision_for_average():
    profile = build_text_profile("a aa aa.", ["a", "aa", "aa"])
    assert profile.precision == 2


def test_average_policy_uses_word_count_instead_of_sentence_fragments():
    assert choose_average_divisor(["aa", "bbbb", "cccccc"], ["aa bbbb cccccc"]) == 3


def test_average_policy_always_rounds_to_two_decimals_for_non_empty_words():
    assert choose_average_precision(["a", "aa", "aa"], ["a aa aa"]) == 2


def test_average_word_length_from_profile_uses_profile_contract():
    profile = TextProfile(
        words=["a", "aa", "aa"],
        sentence_fragments=["a aa aa"],
        word_lengths=[1, 2, 2],
        total_length=5,
        divisor_hint=3,
        precision=2,
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
