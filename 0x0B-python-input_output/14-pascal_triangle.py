#!/usr/bin/python3
"""
   Returns a list of lists of integers representing the Pascal’s triangle of n:
"""


def pascal_triangle(n):
    if type(n) is not int:
        raise TypeError("n must be an integer")
    if (n <= 0):
        return []
    pascal = []
    i = 1
    while (i <= n):
        pascal.append([])
        for b in range(1, i + 1):
            val = b
            if b == i:
                val = 1
            if b > 1 and b != i and i > 3:
                val = pascal[i - 2][b - 1] + pascal[i - 2][b - 2]
            pascal[i - 1].append(val)
        i += 1
    return pascal
