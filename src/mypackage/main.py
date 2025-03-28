import logging
import sys
from typing import List, Optional

from .app import add_numbers, format_result
from .logger import setup_logger
from mypackage.cli import parse_args


def main(args: Optional[List[str]] = None) -> int:
    """Main entry point for the CLI.

    Args:
        args: Command-line arguments (defaults to sys.argv[1:])

    Returns:
        Exit code
    """
    parsed_args = parse_args(args)

    # Set up logging with the specified level
    log_level = getattr(logging, parsed_args.log_level)
    logger = setup_logger(level=log_level)

    try:
        logger.debug(f"Processing arguments: {parsed_args}")
        result = add_numbers(parsed_args.a, parsed_args.b)
        output = format_result(parsed_args.a, parsed_args.b, result, parsed_args.format)
        print(output)
        return 0
    except Exception as e:
        logger.error(f"Error during execution: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
