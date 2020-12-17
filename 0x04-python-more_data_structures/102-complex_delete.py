#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if (a_dictionary is None or len(a_dictionary) == 0):
        return a_dictionary
    del_items = []
    for a, b in a_dictionary.items():
        if (b == value):
            del_items.append(a)
    for i in del_items:
        del a_dictionary[i]
    return a_dictionary
