#!/usr/bin/python3


class Rectangle:
    "This is my custom class for Rectangle"
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        area_1 = rect_1.width * rect_1.height
        area_2 = rect_2.width * rect_2.height
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (area_1 >= area_2):
            return (rect_1)
        return (rect_2)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        p = (self.width + self.height) * 2
        if self.width == 0 or self.height == 0:
            p = 0
        return p

    def __repr__(self):
        return 'Rectangle(%s, %s)' % (self.width, self.height)

    def __str__(self):
        string = ""
        for i in range(self.height):
            string += (str(self.print_symbol) * self.width + "\n")
        return string[:-1]

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
