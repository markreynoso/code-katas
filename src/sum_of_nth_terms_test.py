"""this file tests the code wars kata: Sum of nth Terms."""

import pytest

tests = [
    (1, '1.00'),
    (2, '1.25'),
    (3, '1.39'),
    (4, '1.49'),
    (5, '1.57'),
    (6, '1.63'),
    (7, '1.68'),
    (8, '1.73'),
    (200, '2.81')
]

@pytest.mark.parametrize('a_num, result', tests)
def test_series_sum(a_num, result):
    """this tests whether series_sum() returns a decimal represented as
    a string for the sum of 1 / 1 and add 3 to denominator n number of times."""
    from sum_of_nth_terms import series_sum
    assert series_sum(a_num) == result