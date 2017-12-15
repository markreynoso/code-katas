"""Test proper parenthetics."""
from parenthetics import proper_parenthetics

import pytest


def test_proper_parenthetics_raises_type_error_if_not_string():
    """Test proper parenthetics raises type error."""
    with pytest.raises(TypeError):
        proper_parenthetics(12345)


def test_proper_parenthetics_returns_error_msg_if_no_parens():
    """Test proper parens returns error msg if no parens in string."""
    out = proper_parenthetics('string')
    assert out == 'There are no parenthesis in this string.'


def test_proper_parens_returns_zero_for_balanced_string():
    """Test proper parens if balanced."""
    assert proper_parenthetics('(())') == 0


def test_proper_parents_returns_neg_if_broken():
    """Test proper parens returns -1 if broken parens."""
    assert proper_parenthetics('))((') == -1


def test_proper_parens_returns_one_if_unclosed():
    """Test proper parens returns one if unclosed."""
    assert proper_parenthetics('(()))') == -1


def test_proper_parens_balanced_with_letters():
    """Test proper parens when balanced has letters."""
    assert proper_parenthetics('(bala(n)ced())') == 0


def test_proper_parens_broken_with_letters():
    """Test proper parens when broken has letters."""
    assert proper_parenthetics('(bala(n)c)(ed()))(') == -1


def test_proper_parens_unclosed_with_letters():
    """Test proper parens when unclosed has letters."""
    assert proper_parenthetics('(bala(n)c)(ed()') == 1


def test_proper_parens_all_left_parens():
    """Test proper parens if all parens are left."""
    assert proper_parenthetics('((((((') == 1


def test_proper_parens_all_right_parens():
    """Test proper aprens if all parens are right."""
    assert proper_parenthetics('))))))') == -1
