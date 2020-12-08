#!/usr/bin/python3
def remove_char_at(str, n):
    cpy = ""
    c = 0
    for i in str:
        if(c != n):
            cpy += i
        c += 1
    return (cpy)
