"""Tests for the command-line interface."""

from mypackage.cli import parse_args


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
