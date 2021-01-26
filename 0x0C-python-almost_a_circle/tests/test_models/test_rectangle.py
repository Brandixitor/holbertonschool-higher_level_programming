#!/usr/bin/python3
""" Test case for the module base """

""" Importing class from Base Module """
import unittest
from models.rectangle import Rectangle


class TestRectangleOutput(unittest.TestCase):
    def test_main(self):
        """ [Rectangle] Rest if the result is as excepted in the example """
        if __name__ == "__main__":
            r1 = Rectangle(10, 2)
            self.assertEqual(r1.id, 1)
            r2 = Rectangle(2, 10)
            self.assertEqual(r2.id, 2)
            r3 = Rectangle(10, 2, 0, 0, 12)
            self.assertEqual(r3.id, 12)
            r4 = Rectangle(10, 2, 0, 0, 3)
            self.assertEqual(r4.id, 3)

    def test_validate_types(self):
        """ [Rectangle] Types validators """
        with self.assertRaises(TypeError) as cm:
            r1 = Rectangle("test", 1) 
        self.assertEqual(cm.exception.args[0], "width must be an integer")

        with self.assertRaises(TypeError) as cm:
            r1 = Rectangle(1, "test") 
        self.assertEqual(cm.exception.args[0], "height must be an integer")
        
        with self.assertRaises(TypeError) as cm:
            r1 = Rectangle(1, 1, "t") 
        self.assertEqual(cm.exception.args[0], "x must be an integer")
        
        with self.assertRaises(TypeError) as cm:
            r1 = Rectangle(1, 1, 2, "t") 
        self.assertEqual(cm.exception.args[0], "y must be an integer") 

    def test_validate_positive(self):
        """ [Rectangle] Positive validators """
        with self.assertRaises(ValueError) as cm:
            r1 = Rectangle(-5, 1) 
        self.assertEqual(cm.exception.args[0], "width must be > 0")

        with self.assertRaises(ValueError) as cm:
            r1 = Rectangle(1, -2) 
        self.assertEqual(cm.exception.args[0], "height must be > 0")
        
        with self.assertRaises(ValueError) as cm:
            r1 = Rectangle(1, 1, -2, 0) 
        self.assertEqual(cm.exception.args[0], "x must be >= 0")
        
        with self.assertRaises(ValueError) as cm:
            r1 = Rectangle(1, 1, 2, -2) 
        self.assertEqual(cm.exception.args[0], "y must be >= 0") 
 
