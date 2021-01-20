#!/usr/bin/python3
"""
   function that reads n lines of a text file (UTF8) and prints it to stdout:
"""


def read_lines(filename="", nb_lines=0):
    """
       function that reads n lines of a text file (UTF8)
       and prints it to stdout:
    """
    i = 0
    with open(filename, "r", encoding='utf-8') as f:
        f = list(f)
        nb_maxlines = len(f)
        if nb_lines <= 0 or nb_lines >= nb_maxlines:
            for i in f:
                print(i, end='')
        else:
            for i in range(nb_lines):
                print(f[i], end='')
