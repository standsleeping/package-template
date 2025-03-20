"""Tests for the format_result function."""

import json
from mypackage.app import format_result


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