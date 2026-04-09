#!/usr/bin/env bash
pytest tests/test_core.py -q -k "test_most_common_words_strips_punctuation_before_counting"
