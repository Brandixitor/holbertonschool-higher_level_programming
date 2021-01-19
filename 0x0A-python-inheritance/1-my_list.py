#!/usr/bin/python3
"""
    class MyList that inherits from list
"""


class MyList(list):
    """
        prints the list, but sorted (ascending sort)
        all the elements of the list will be of type <int>
    """
    def print_sorted(self):
        print(sorted(self))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
