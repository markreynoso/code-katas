"""Test the code wars kata: What's the Real Floor."""
import pytest


tests = [
    (1, 0),
    (5, 4),
    (15, 13),
    (100, 98),
    (-3, -3),
    (0, 0),
    (120, 118),
    (45, 43),
    (-12, -12),
]


@pytest.mark.parametrize('floor, result', tests)
def test_get_real_floor(floor, result):
    """Get actual floor of american standard labels."""
    from whats_the_real_floor import get_real_floor
    assert get_real_floor(floor) == result
