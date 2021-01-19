#!/usr/bin/python3
"""
   Rectangle that inherits from BaseGeometry (7-base_geometry.py).
   (task based on 8-rectangle.py)
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
       Rectangle that inherits from BaseGeometry (7-base_geometry.py).
       (task based on 8-rectangle.py)
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
           area of the triangle = width * height
        """
        return self.__width * self.__height

    def __str__(self):
        """
           return [Rectangle] <width>/<height>
        """
        return "[Rectangle] %d/%d" % (self.__width, self.__height)
