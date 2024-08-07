#!/usr/bin/python3
"""
square.py

This module defines a Square class.
"""


class Square:
    """A class used to represent a square

    Args:
        size (int): The size of the square (private attribute)
    """

    def __init__(self, size=0):
        """Defines the size of the square

        Args:
            size (int): The size of the square (default is 0)

        Raise:
            TypeError: If size is not an integer.

            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
