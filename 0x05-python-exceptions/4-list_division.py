#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for c in range(list_length):
        try:
            new_list.append(my_list_1[c] / my_list_2[c])
        except TypeError:
            new_list.append(0)
            print("wrong type")
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
        except IndexError:
            new_list.append(0)
            print("out of range")
        finally:
            pass
    return new_list
