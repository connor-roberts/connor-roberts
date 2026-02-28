"""Tests for text_utils.py"""

import pytest
from text_utils import (
    word_count,
    char_frequency,
    truncate,
    is_palindrome,
    count_vowels,
    title_case,
    reverse_words,
    slugify,
)


def test_word_count():
    assert word_count("hello world") == 2
    assert word_count("") == 0
    assert word_count("   ") == 0
    assert word_count("one") == 1


def test_char_frequency():
    freq = char_frequency("aab")
    assert freq["a"] == 2
    assert freq["b"] == 1


def test_truncate():
    assert truncate("hello world", 8) == "hello..."
    assert truncate("hi", 10) == "hi"
    assert truncate("hello world", 11) == "hello world"


def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("A man a plan a canal Panama") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("Was it a car or a cat I saw") is True


def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("AEIOU") == 5
    assert count_vowels("rhythm") == 0
    assert count_vowels("") == 0


def test_title_case():
    assert title_case("the quick brown fox") == "The Quick Brown Fox"
    assert title_case("a tale of two cities") == "A Tale of Two Cities"
    assert title_case("lord of the rings") == "Lord of the Rings"


def test_reverse_words():
    assert reverse_words("hello world") == "world hello"
    assert reverse_words("one two three") == "three two one"
    assert reverse_words("single") == "single"


def test_slugify():
    assert slugify("Hello World!") == "hello-world"
    assert slugify("  spaces  ") == "spaces"
    assert slugify("múltiple---hyphens") == "mltiple-hyphens"
