#!/usr/bin/python3
"""
   Square that inherits from Rectangle (9-rectangle.py).
   (task based on 10-square.py).
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
       Square that inherits from Rectangle (9-rectangle.py).
       (task based on 10-square.py).
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def __str__(self):
        """
           return a string with "[Square] size/size"
        """
        return "[Square] %d/%d" % (self.__size, self.__size)
