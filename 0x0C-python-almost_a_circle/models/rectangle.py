#!/usr/bin/python3
"""
   Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
       Rectangle that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__()
        if id is not None and type(id) is int:
            self.id = id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setters """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setters """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setters """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setters """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the area value of the Rectangle instance. """
        return self.width * self.height

    def display(self):
        """ prints in stdout the Rectangle instance with the character # """
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """ Str output """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
            **kwargs must be skipped if *args exists and is not empty
            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute
        """
        lena = len(args)
        if lena != 0:
            if lena >= 1:
                self.id = args[0]
            if lena >= 2:
                self.width = args[1]
            if lena >= 3:
                self.height = args[2]
            if lena >= 4:
                self.x = args[3]
            if lena >= 5:
                self.y = args[4]
            return
        for i in kwargs:
            setattr(self, i,  kwargs[i])

    def to_dictionary(self):
        """
            returns the dictionary representation of a Rectangle
        """
        dicta = {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
        return dicta
