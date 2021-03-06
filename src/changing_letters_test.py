"""This file tests the code wars kata: Changing Letters."""
import pytest


tests = [
    ("Basic Tests", "BAsIc TEsts"),
    ("HelloWorld!", "HEllOWOrld!"),
    ("Sunday", "SUndAy"),
    ("poop", "pOOp"),
    ("stick", "stIck"),
    ("rhythm", "rhythm"),
    ("aeiou", "AEIOU")
]


@pytest.mark.parametrize('words, result', tests)
def test_pig_it(words, result):
    """Test if swap() returns string with every vowel cap."""
    from changing_letters import swap
    assert swap(words) == result
