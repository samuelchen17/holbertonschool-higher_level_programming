#!/usr/bin/python3
"""Function that prints text with 2 new lines after '.', '?' and ':'."""


def text_indentation(text):
    """Print text with indentation.

    Two new lines are printed after each occurrence of '.', '?' and ':'.
    Leading and trailing spaces are removed from each printed line.
    """

    # if arg is not string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line = True

    for char in text:
        if char == " " and new_line:
            continue

        if char in ".?:":
            print(char)
            print()
            new_line = True
        else:
            print(char, end="")
            new_line = False
