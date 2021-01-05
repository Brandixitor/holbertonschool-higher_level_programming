#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value >= 0:
            self.__size = value
        else:
            print("size must be >= 0", end="")
            raise ValueError

    def area(self):
        size = self.size
        return size * size
