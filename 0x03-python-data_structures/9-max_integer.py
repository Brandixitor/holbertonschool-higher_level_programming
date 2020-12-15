#!/usr/bin/python3
def max_integer(my_list=[]):
    lenl = len(my_list)
    if (lenl == 0):
        return None
    higher = my_list[0]
    for i in my_list:
        if i > higher:
            higher = i
    return (higher)
