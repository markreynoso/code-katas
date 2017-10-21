"""this file tests the code wars kata: Exclamation marks series #6."""

import pytest

tests = [
    ["Hi!", 1, "Hi"],
    ["Hi!", 100, "Hi"],
    ["Hi!!!", 1, "Hi!!"],
    ["Hi!!!", 100, "Hi"],
    ["!Hi", 1, "Hi"],
    ["!Hi!", 1, "Hi!"],
    ["!Hi!", 100, "Hi"],
    ["!!!Hi !!hi!!! !hi", 1, "!!Hi !!hi!!! !hi"],
    ["!!!Hi !!hi!!! !hi", 3, "Hi !!hi!!! !hi"],
    ["!!!Hi !!hi!!! !hi", 5, "Hi hi!!! !hi"],
    ["!!!Hi !!hi!!! !hi", 100, "Hi hi hi"],
    ["!!!Hi !!hi!!! !hi", 1000, "Hi hi hi"],
    ["!Hi! !hi! !hi!", 5, "Hi hi hi!"],
    ["!!!Hi !!hi!!! !hi !!!!!hi hi!!!!!", 10, "Hi hi hi !!!!hi hi!!!!!"],
    ["!!!Hi!!!!!!!!", 8, "Hi!!!"],
]

@pytest.mark.parametrize('s, n, result', tests)
def test_remove(s, n, result):
    """this tests whether remove() will remove n number of
        exclamation marks from s"""
    from exclamation_marks_series_6 import remove
    assert remove(s, n) == result