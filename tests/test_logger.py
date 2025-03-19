"""Tests for the logger module."""

import logging
import sys
from unittest.mock import patch, MagicMock

from mypackage.logging.logger import configure_logging, get_logger


def test_configure_logging() -> None:
    """Sets up the root logger correctly."""
    # Capture the handlers before we run the test
    root_logger = logging.getLogger()
    old_handlers = root_logger.handlers.copy()
    old_level = root_logger.level

    try:
        # Clear handlers for clean test
        for handler in root_logger.handlers[:]:
            root_logger.removeHandler(handler)

        # Test with default level
        configure_logging()

        assert root_logger.level == logging.INFO
        assert len(root_logger.handlers) == 1
        assert isinstance(root_logger.handlers[0], logging.StreamHandler)
        assert root_logger.handlers[0].stream == sys.stderr

        # Test with custom level
        for handler in root_logger.handlers[:]:
            root_logger.removeHandler(handler)

        configure_logging(level=logging.DEBUG)
        assert root_logger.level == logging.DEBUG
    finally:
        # Restore original handlers
        for handler in root_logger.handlers[:]:
            root_logger.removeHandler(handler)

        for handler in old_handlers:
            root_logger.addHandler(handler)

        root_logger.setLevel(old_level)


def test_get_logger_with_name() -> None:
    """Uses an explicit name."""
    logger = get_logger("test_logger")
    assert logger.name == "test_logger"


@patch("inspect.currentframe")
def test_get_logger_with_auto_name(mock_currentframe) -> None:
    """Infers module name correctly when name is not provided."""
    # Create mock frame with a module
    mock_module = MagicMock()
    mock_module.__name__ = "test_inferred_module"

    mock_frame = MagicMock()
    mock_frame_back = MagicMock()
    mock_currentframe.return_value = mock_frame
    mock_frame.f_back = mock_frame_back

    with patch("inspect.getmodule", return_value=mock_module):
        logger = get_logger()
        assert logger.name == "test_inferred_module"


@patch("inspect.currentframe")
def test_get_logger_fallback(mock_currentframe) -> None:
    """Fallback to default name when inference fails."""
    # Return None to simulate failure to get frame
    mock_currentframe.return_value = None
    logger = get_logger()
    assert logger.name == "mypackage"
