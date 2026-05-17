#!/usr/bin/python3
"""Module for printing full name."""


def say_my_name(first_name, last_name=""):
    """Takes first and last name as arguments and prints the full name."""
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError(
            "first_name must be a string or last_name must be a string"
        )

    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")
