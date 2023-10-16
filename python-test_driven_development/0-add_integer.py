#!/usr/bin/python3
"""add_integer(a, b)
Add 2 numbers together
"""


def add_integer(a, b=98):
    """Adds 2 numbers (a and b)

    Returns: The sum a and b as an integer
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
