#!/usr/bin/env bash
pytest tests/test_core.py -q -k "test_average_word_length_returns_mean_length or test_average_word_length_rounds_to_two_decimals"
