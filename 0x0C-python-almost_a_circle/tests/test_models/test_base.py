#!/usr/bin/python3
""" Test case for the module base """

""" Importing class from Base Module """
import unittest
from models.base import Base

class TestMainOutput(unittest.TestCase):
    def test_main(self):
        """ Test if the result is as excepted in the example """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)
    def test_none(self):
        """ Test if id is incrementing when the value is none """
        b1 = Base()
        self.assertEqual(b1.id, 5)
        b2 = Base()
        self.assertEqual(b2.id, 6)
        b3 = Base()
        self.assertEqual(b3.id, 7)
        b4 = Base()
        self.assertEqual(b4.id, 8)
        b5 = Base()
        self.assertEqual(b5.id, 9)
    def test_case1(self):
        """ Testing differents values """
        b1 = Base(10)
        self.assertEqual(b1.id, 10)
        b2 = Base(20)
        self.assertEqual(b2.id, 20)
        b3 = Base(-25)
        self.assertEqual(b3.id, -25)
        self.assertEqual(b2.id, 20)

