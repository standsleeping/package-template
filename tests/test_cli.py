"""Tests for the command-line interface."""

from mypackage.cli import parse_args, main


def test_parse_args() -> None:
    """Test argument parsing."""
    args = parse_args(["1", "2"])
    assert args.a == 1.0
    assert args.b == 2.0
    assert args.format == "text"

    args = parse_args(["1", "2", "--format", "json"])
    assert args.format == "json"

    args = parse_args(["1.5", "2.5", "-f", "json"])
    assert args.a == 1.5
    assert args.b == 2.5
    assert args.format == "json"


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
