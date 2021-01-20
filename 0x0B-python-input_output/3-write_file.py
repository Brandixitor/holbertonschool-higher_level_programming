#!/usr/bin/python3
"""
   function that writes a string to a text file (UTF8) and returns the number
   of characters written.
"""


def write_file(filename="", text=""):
    """
       function that writes a string to a text file (UTF8) and
       returns the number
       of characters written.
    """
    with open(filename, "w", encoding='utf8') as f:
        return f.write(text)
