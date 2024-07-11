#!/usr/bin/python3

"""
Module 7-base_geometry

Contains BaseGeometry
with public instance method area and integer_validation
"""


class BaseGeometry:
    """
    Methods:
        area(self)
        integer_validator(self, name, value)
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

import unittest
from models.base_geometry import BaseGeometry

class TestBaseGeometry(unittest.TestCase):
    def setUp(self):
        self.bg = BaseGeometry()

    def test_area(self):
        with self.assertRaises(Exception) as context:
            self.bg.area()
        self.assertEqual(str(context.exception), "area() is not implemented")

    def test_integer_validator_valid(self):
        # Test valid integer input
        try:
            self.bg.integer_validator("test", 5)
        except (TypeError, ValueError):
            self.fail("integer_validator raised unexpected exception for valid input")

    def test_integer_validator_type_error(self):
        # Test type error for non-integer input
        with self.assertRaises(TypeError) as context:
            self.bg.integer_validator("test", "string")
        self.assertEqual(str(context.exception), "test must be an integer")

    def test_integer_validator_value_error(self):
        # Test value error for non-positive integer input
        with self.assertRaises(ValueError) as context:
            self.bg.integer_validator("test", 0)
        self.assertEqual(str(context.exception), "test must be greater than 0")

if __name__ == "__main__":
    unittest.main()

