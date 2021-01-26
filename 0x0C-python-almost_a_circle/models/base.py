#!/usr/bin/python3
"""
   This class will be the “base” of all other classes in this project.
   The goal of it is to manage id attribute in all your future classes
   and to avoid duplicating the same code
"""
import json


class Base:
    """
       This class will be the “base” of all other classes in this project.
       The goal of it is to manage id attribute in all your future classes
       and to avoid duplicating the same code
    """

    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
           returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
           writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        l = []
        with open(filename, "w") as f:
            if list_objs is not None:
                for i in list_objs:
                    l.append(i.to_dictionary())
            l = cls.to_json_string(l)
            f.write(l)

    def from_json_string(json_string):
        """
           returns the list of the JSON string representation json_string
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
           returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            instance = cls(1, 2)
        else:
            instance = cls(1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """
            returns a list of instances
        """
        instance = []
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                content = f.read()
                myobj = cls.from_json_string(content)
                for i in myobj:
                    instance.append(cls.create(**i))
            return instance
        except:
            return []
