#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        """
        Test if the biggest number is printed
        """
        self.assertEqual(max_integer([1, 2, 5, 6, 50, 2]), 50)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([-5, -50, -1, -3, -4]), -1)
        self.assertEqual(max_integer([-2]), -2)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([50, 1, 2, 3]), 50)
        self.assertEqual(max_integer([1, 2, 3, 4, 50]), 50)
