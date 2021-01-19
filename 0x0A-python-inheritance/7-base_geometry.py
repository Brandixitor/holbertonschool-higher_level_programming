#!/usr/bin/python3
"""
   class BaseGeometry (based on 6-base_geometry.py).
"""


class BaseGeometry:
    """
        class BaseGeometry (based on 6-base_geometry.py).
    """
    def area(self):
        """
           raises an Exception : area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
           name is always a string
           if value is not an integer: raise a TypeError exception
           if value is less or equal to 0: raise a ValueError exception
        """
        if type(name) is not str:
            raise TypeError("{} must be a string".format(name))
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-base_geometry.txt")
