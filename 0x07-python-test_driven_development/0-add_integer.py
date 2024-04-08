#!/usr/bin/python3

"""Defines a function that return the addition."""


def add_integer(a, b=98):
    """Return integer addition of a and b = 98.
    The value a and b must be integer or float.
    Raises:
        TypeError: If a and b is not integer or not float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
