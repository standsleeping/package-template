"""Tests for the add_numbers function."""

from mypackage.app import add_numbers


def test_add_numbers_integers() -> None:
    """Test adding two integers."""
    assert add_numbers(1, 2) == 3
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0


def test_add_numbers_floats() -> None:
    """Test adding floating point numbers."""
    assert add_numbers(1.5, 2.5) == 4.0
    assert add_numbers(-1.5, 1.5) == 0.0