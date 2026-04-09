#!/usr/bin/env bash
pytest tests/test_core.py -q -k "test_word_count_ignores_repeated_whitespace"
