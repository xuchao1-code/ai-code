"""Command-line interface for ai-code."""

from __future__ import annotations

import argparse
from collections.abc import Sequence

from ai_code import __version__


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line argument parser."""
    parser = argparse.ArgumentParser(description="Run the ai-code Python application.")
    parser.add_argument(
        "--name",
        default="world",
        help="Name to include in the greeting.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the application."""
    parser = build_parser()
    args = parser.parse_args(argv)
    print(f"Hello, {args.name}!")
    return 0
