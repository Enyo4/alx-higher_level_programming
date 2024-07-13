#!/usr/bin/python3
"""
square.py

This module defines a Square class.
"""


class Square:
    """A class used to represent a square

    Args:
        size (int): The size of the square (private attribute)

    Attributes:
       size (int): The size of the square (private attribute)

    """

    def __init__(self, size):
        self.__size = size
