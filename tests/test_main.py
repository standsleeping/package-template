"""Tests for the main function."""

from mypackage.main import main


def test_main(capsys) -> None:
    """Test the main function with captured stdout."""
    # Test with text output
    exit_code = main(["1", "2"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.strip() == "1.0 + 2.0 = 3.0"

    # Test with JSON output
    exit_code = main(["1", "2", "--format", "json"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert '"operation": "addition"' in captured.out
    assert '"result": 3.0' in captured.out
