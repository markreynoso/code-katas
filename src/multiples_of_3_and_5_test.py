"""this file tests the code wars kata: Multiples of 3 and 5."""

import pytest

tests = [
    (10, 23),
    (15, 45),
    (25, 143),
    (100, 2318),
    (2, 0)
]

@pytest.mark.parametrize('number, result', tests)
def test_solution(number, result):
    """this tests whether solution() returns the sum of all numbers
    which are multiples of 3 and 5 in a given list."""
    from multiples_of_3_and_5 import solution
    assert solution(number) == result