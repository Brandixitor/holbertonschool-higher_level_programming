#!/usr/bin/python3
"""
   class Student that defines a student by:
   - first_name
   - last_name
   - age
"""


class Student:
    """
       class Student that defines a student by:
       - first_name
       - last_name
       - age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
           retrieves a dictionary representation of a Student instance
        """
        if (type(attrs) is list):
            new_dict = {}
            for i in attrs:
                if i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
            return new_dict
        return self.__dict__
