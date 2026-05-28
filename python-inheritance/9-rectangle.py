#!/usr/bin/python3
"""Module that defines Rectangle class."""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class."""

    def __init__(self, width, height):
        """Initialize rectangle."""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns rectangle description."""
        return f"[Rectangle] {self.__width}/{self.__height}"
