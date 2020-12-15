#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for i in range(len(my_list)):
        new_list.append(False) if my_list[i] % 2 else new_list.append(True)
    return (new_list)
