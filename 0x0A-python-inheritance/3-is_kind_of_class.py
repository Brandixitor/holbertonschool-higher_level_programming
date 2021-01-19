#!/usr/bin/python3
"""
    function that returns True if the object is an instance of, or if the
    object is an instance of a class that inherited from, the specified
    class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
        function that returns True if the object is an instance of, or if the
        object is an instance of a class that inherited from, the specified
        class ; otherwise False.
    """
    return issubclass(type(obj), a_class)
