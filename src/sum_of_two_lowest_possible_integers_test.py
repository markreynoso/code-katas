"""Test the code wars kata: Sum of Two Lowest Possible Integers."""
import pytest


tests = [
    ([5, 8, 12, 18, 22], 13),
    ([7, 15, 12, 18, 22], 19),
    ([25, 42, 12, 18, 22], 30),
    ([2, 267, 20, 8, 321], 10),
    ([250, 410, 120, 10000, 220], 340),
    ([1, 2, 8, 78, 54], 3),
    ([432, 4534352, 543265, 456424, 2], 434)
]


@pytest.mark.parametrize('numbers, result', tests)
def test_remove(numbers, result):
    """Sum of the two lowest integers of any given list."""
    from sum_of_two_lowest_possible_integers import sum_two_smallest_numbers
    assert sum_two_smallest_numbers(numbers) == result
