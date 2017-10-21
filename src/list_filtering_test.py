"""this file tests the code wars kata: List Filtering."""

import pytest

tests = [
    ([1, 2, 'a', 'b'], [1, 2]),
    ([1, 'a', 'b', 0, 15], [1, 0, 15]),
    ([1, 2, 'aasf', '1', '123', 123], [1, 2, 123]),
    ([5, 98, 'hello', 'world', 432], [5, 98, 432]),
    ([9, 8, 'why', '23', 'ugh', 4], [9, 8, 4]),
    ([6, 'g', '12', 'NOOOO'], [6]),
    (['blah', 'wine', 'burger', '5', '123'], [])
]

@pytest.mark.parametrize('a_list, result', tests)
def test_filter_list(a_list, result):
    """this tests whether filter_list() will return a list
        containing only integers."""
    from list_filtering import filter_list
    assert filter_list(a_list) == result