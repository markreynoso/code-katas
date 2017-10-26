"""Tests the code wars kata: Find the Odd Int."""
import pytest


tests = [
    ([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5], 5),
    ([1, 1, 1, 3, 5, 3, 6, 3, 3, 5, 6], 1),
    ([2, 2, 4, 4, 6], 6),
    ([8, 1, 1, 2, 4, 2, 4], 8),
    ([4, 5, 5], 4)
]


@pytest.mark.parametrize('num_list, result', tests)
def test_find_it(num_list, result):
    """Which integer appears an odd number of times in list."""
    from find_the_odd_int import find_it
    assert find_it(num_list) == result
