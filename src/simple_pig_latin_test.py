"""Test the code wars kata: List Filtering."""
import pytest


tests = [
    ('Pig latin is cool', 'igPay atinlay siay oolcay'),
    ('This is my string', 'hisTay siay ymay tringsay'),
    ('There once', 'hereTay nceoay'),
    ('was a man', 'asway aay anmay'),
    ('from nantucket', 'romfay antucketnay'),
    ('all the words', 'llaay hetay ordsway')
]


@pytest.mark.parametrize('words, result', tests)
def test_pig_it(words, result):
    """Move 1st letter to end and 'ay' is added."""
    from simple_pig_latin import pig_it
    assert pig_it(words) == result
