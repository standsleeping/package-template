"""Core functionality for the package."""

from typing import Union, Dict, Any, Literal
import json

from .logger import logger

OutputFormat = Literal["text", "json"]


def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        The sum of the two numbers
    """
    logger.debug(f"Adding {a} and {b}")
    return a + b


def format_result(
    a: Union[int, float],
    b: Union[int, float],
    result: Union[int, float],
    output_format: OutputFormat = "text",
) -> str:
    """Format the calculation result.

    Args:
        a: First number
        b: Second number
        result: The calculation result
        output_format: The desired output format ("text" or "json")

    Returns:
        A formatted string representing the calculation
    """
    if output_format == "json":
        data: Dict[str, Any] = {
            "operation": "addition",
            "inputs": {"a": a, "b": b},
            "result": result,
        }
        return json.dumps(data, indent=2)
    else:
        return f"{a} + {b} = {result}"
