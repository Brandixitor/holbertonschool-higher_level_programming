#!/usr/bin/python3
"""
   Square that inherits from Rectangle (9-rectangle.py)
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
       Square that inherits from Rectangle (9-rectangle.py)
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size
