"""
Small helpers for producing readable console output.

Examples:
    >>> from custom_print import print_heading, print_bullets
    >>> print_heading("Shopping list")
    Shopping list
    -------------
    >>> print_bullets(["Apples", "Bread"])
    • Apples
    • Bread

All functions write to standard output by default. Pass ``file=`` to write to
another text stream, just as you would with :func:`print`.
"""

from collections.abc import Iterable
from typing import TextIO


def print_separator(
    width: int = 40,
    char: str = "-",
    *,
    file: TextIO | None = None,
) -> None:
    """Print a horizontal separator of *width* repetitions of *char*."""
    if width < 0:
        raise ValueError("width must be zero or greater")
    if len(char) != 1:
        raise ValueError("char must be exactly one character")
    print(char * width, file=file)


def print_heading(
    text: object,
    char: str = "-",
    *,
    file: TextIO | None = None,
) -> None:
    """Print a heading followed by an underline the same length as its text."""
    heading = str(text)
    if len(char) != 1:
        raise ValueError("char must be exactly one character")
    print(heading, file=file)
    print(char * len(heading), file=file)


def print_box(
    text: object,
    padding: int = 1,
    *,
    file: TextIO | None = None,
) -> None:
    """Print text inside a simple ASCII box, preserving multiple lines."""
    if padding < 0:
        raise ValueError("padding must be zero or greater")

    lines = str(text).splitlines() or [""]
    content_width = max(map(len, lines))
    inner_width = content_width + padding * 2
    border = "+" + "-" * (inner_width + 2) + "+"

    print(border, file=file)
    for line in lines:
        padded = " " * padding + line.ljust(content_width) + " " * padding
        print(f"| {padded} |", file=file)
    print(border, file=file)


def print_bullets(
    items: Iterable[object],
    bullet: str = "•",
    *,
    file: TextIO | None = None,
) -> None:
    """Print each item on its own line with a bullet marker."""
    for item in items:
        print(f"{bullet} {item}", file=file)


def print_numbered_list(
    items: Iterable[object],
    start: int = 1,
    *,
    file: TextIO | None = None,
) -> None:
    """Print each item on its own line with consecutive numbers."""
    if start < 0:
        raise ValueError("start must be zero or greater")
    for number, item in enumerate(items, start=start):
        print(f"{number}. {item}", file=file)


__all__ = [
    "print_bullets",
    "print_box",
    "print_heading",
    "print_numbered_list",
    "print_separator",
]
