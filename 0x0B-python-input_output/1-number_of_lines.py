#!/usr/bin/python3
"""
   function that returns the number of lines of a text file:
"""


def number_of_lines(filename=""):
    """
       function that returns the number of lines of a text file:
    """
    with open(filename, "r") as f:
        return len(list(f))
