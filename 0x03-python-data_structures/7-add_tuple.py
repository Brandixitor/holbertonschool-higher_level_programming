#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lena = len(tuple_a)
    lenb = len(tuple_b)
    if lena < 2:
        if lena == 0:
            tuple_a = (0, 0)
        else:
            tuple_a = (tuple_a[0], 0)
    if lenb < 2:
        if lenb == 0:
            tuple_b = (0, 0)
        else:
            tuple_b = (tuple_b[0], 0)
    a = tuple_a[0] + tuple_b[0]
    b = tuple_a[1] + tuple_b[1]
    tuple_c = (a, b)
    return tuple_c
