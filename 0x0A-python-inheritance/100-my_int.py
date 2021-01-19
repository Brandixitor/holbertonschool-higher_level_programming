#!/usr/bin/python3
"""
   class MyInt that inherits from int
"""


class MyInt(int):
    """
       class MyInt that inherits from int
    """
    def __eq__(self, value):
        """
            Reverse the initial __eq__ function
            if 1 == 1 return False
        """
        return super().__int__() != value

    def __ne__(self, value):
        """
            Reverse the initial __eq__ function
            if 1 != 1 return True
        """
        return super().__int__() == value
