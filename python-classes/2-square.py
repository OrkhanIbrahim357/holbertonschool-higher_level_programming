#!/usr/bin/python3
"""Function"""


class Square:
    """class Square that defines a square:"""
    def __init__(self, size=0):
        if size < 0:
            raise ValueError("size must be >= 0")
        elif isinstance(size, int):
            raise TypeError("size must be an integer")
        self.__size = size
