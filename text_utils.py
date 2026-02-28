"""
text_utils.py - A collection of text processing utilities.
"""

import re
from collections import Counter


def word_count(text):
    """Return the number of words in the given text."""
    if not text or not text.strip():
        return 0
    return len(text.split())


def char_frequency(text):
    """Return a dictionary of character frequencies, ignoring whitespace."""
    return dict(Counter(c for c in text if not c.isspace()))


def truncate(text, max_length, suffix="..."):
    """Truncate text to max_length characters, appending suffix if truncated."""
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)] + suffix


def is_palindrome(s):
    """Return True if s is a palindrome (ignoring case and non-alphanumeric chars)."""
    cleaned = re.sub(r"[^a-z0-9]", "", s.lower())
    return cleaned == cleaned[::-1]


def count_vowels(text):
    """Return the number of vowel characters in text (case-insensitive)."""
    # TODO: implement vowel counting for a, e, i, o, u
    pass


def title_case(text):
    """Convert text to title case, but leave small words (a, an, the, of, in, on, etc.) lowercase."""
    # TODO: implement title case conversion that lowercases common small words
    pass


def reverse_words(text):
    """Return text with the order of words reversed."""
    # TODO: split on whitespace, reverse the word list, and rejoin
    pass


def slugify(text):
    """Convert text to a URL-friendly slug (lowercase, hyphens instead of spaces, no special chars)."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text
