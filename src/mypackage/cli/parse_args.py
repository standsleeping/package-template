import argparse
from typing import List, Optional

from mypackage.logging import get_logger

# Get module-specific logger using __name__
logger = get_logger(__name__)


def parse_args(args: Optional[List[str]] = None) -> argparse.Namespace:
    """Parse command-line arguments.

    Args:
        args: Command-line arguments (defaults to sys.argv[1:])

    Returns:
        Parsed arguments namespace
    """
    logger.debug("Parsing command line arguments")
    parser = argparse.ArgumentParser(
        prog="mypackage",
        description="Add two numbers together",
    )

    parser.add_argument(
        "a",
        type=float,
        help="First number",
    )

    parser.add_argument(
        "b",
        type=float,
        help="Second number",
    )

    parser.add_argument(
        "--format",
        "-f",
        choices=["text", "json"],
        default="text",
        help="Output format (default: text)",
    )

    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="INFO",
        help="Set the logging level (default: INFO)",
    )

    return parser.parse_args(args)
