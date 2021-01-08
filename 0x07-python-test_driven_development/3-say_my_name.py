#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    if type(first_name) != str or len(first_name) is 0:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
            raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
