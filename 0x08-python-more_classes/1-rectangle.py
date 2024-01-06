#!/usr/bin/python3

"""Define a class Rectangle."""


class Rectangle:
    """Represent a rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer.")
        if width < 0:
            raise ValueError("width must be >= 0")

        self.__width = width
        
        if not isinstance(height, int):
            raise TypeError("height must be an integer.")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__height = height

    def width(self):
        """Width getter."""
        return self.__width

    def width(self, value):
        """Width setter."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer.")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        """Height getter."""
        return self.__height

    def height(self, value):
        """Height setter."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer.")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
