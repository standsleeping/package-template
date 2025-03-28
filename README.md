# MyPackage

A simple Python package template with standard structure and best practices.

## Features

- Standard Python package structure
- CLI interface
- Can be run as a module
- Standard logging configuration
- Type checking with MyPy
- Linting and formatting with Ruff
- Testing with pytest

## Installation

This step is required for the tests to run without import errors, and to run as a module from the root directory (see below).

```bash
uv pip install -e .
```

This creates a link to your source code, making the package importable from anywhere, including your tests.

(Note: the path is also configured in conftest.py, as well as in pyproject.toml under the [tool.pytest.ini_options] section).

## Usage

### As a Command-Line Tool

```bash
# Basic usage
python -m mypackage 1 2

# JSON output
python -m mypackage 1 2 --format json

# With custom log level
python -m mypackage 1 2 --log-level DEBUG
```

