#!/usr/bin/python3
"""Print a square."""


def print_square(size):
    """Print a square made of # with size as the length of the square"""
    # non int, including float
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    # negatives
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
