"""Tests for core functionality."""

import json
from mypackage.core import add_numbers, format_result


def test_add_numbers_integers() -> None:
    """Test adding two integers."""
    assert add_numbers(1, 2) == 3
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0


def test_add_numbers_floats() -> None:
    """Test adding floating point numbers."""
    assert add_numbers(1.5, 2.5) == 4.0
    assert add_numbers(-1.5, 1.5) == 0.0


def test_format_result_text() -> None:
    """Test text formatting of results."""
    assert format_result(1, 2, 3, "text") == "1 + 2 = 3"
    assert format_result(1.5, 2.5, 4.0, "text") == "1.5 + 2.5 = 4.0"


def test_format_result_json() -> None:
    """Test JSON formatting of results."""
    json_output = format_result(1, 2, 3, "json")
    data = json.loads(json_output)

    assert data["operation"] == "addition"
    assert data["inputs"]["a"] == 1
    assert data["inputs"]["b"] == 2
    assert data["result"] == 3
