#!/usr/bin/python3
"""
    class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
       class Square that inherits from Rectangle
       super class with id, x, y, width and height
    """
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(self.size, self.size, x, y, id)

    def __str__(self):
        """
           Str output
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        size setter
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
            args is the list of arguments - no-keyworded arguments
              1st argument should be the id attribute
              2nd argument should be the size attribute
              3rd argument should be the x attribute
              4th argument should be the y attribute
           *kwargs is skipped if *args exists and is not empty
        """
        lena = len(args)
        largs = ('id', 'size', 'x', 'y')
        for i in range(lena):
            setattr(self, largs[i], args[i])
        if lena == 0:
            for i in kwargs:
                setattr(self, i, kwargs[i])

    def to_dictionary(self):
        """
           returns the dictionary representation of a Square
        """
        dicta = {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
        return dicta
