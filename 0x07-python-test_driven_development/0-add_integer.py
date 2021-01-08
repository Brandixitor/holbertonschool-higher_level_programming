#!/usr/bin/python3
""" This is the "0-add_integer" module.
The example module supplies one function, add_integer().  For example,
>>> add_integer(1,2)
3
"""


def add_integer(a, b=98):
    """
    Return the sum of a and b
    """
    types = (int, float)
    l = (isinstance(a, types), isinstance(b, types))
    if (l[0] is False):
        raise TypeError("a must be an integer")
    if (l[1] is False):
        raise TypeError("b must be an integer")
    res = a + b
    if res < 0:
        res = -res
    if res == float("inf"):
        raise ValueError("float overflow")
    return (int(a) + int(b))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
