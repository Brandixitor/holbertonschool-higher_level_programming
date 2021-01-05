#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size >= 0:
            self.__size = size
        else:
            print("size must be >= 0", end="")
            raise ValueError

    def area(self):
        size = self.__size
        return size * size
