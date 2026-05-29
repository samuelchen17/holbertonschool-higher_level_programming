from abc import ABC, abstractmethod
import math

"""Module that defines shapes"""


class Shape(ABC):
    """Shape class"""

    @abstractmethod
    def area(self):
        """area of shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """perimeter of shape"""
        pass


class Circle(Shape):
    """Circle class"""

    def __init__(self, radius):
        """Initialize circle"""
        self.__radius = abs(radius)

    def area(self):
        """return area of circle"""
        return math.pi * (self.__radius**2)

    def perimeter(self):
        """return perimeters of circle"""
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """Rectangle class"""

    def __init__(self, width, height):
        """Initialize square."""
        self.__width = width
        self.__height = height

    def area(self):
        """return area of Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """return perimeters of Rectangle"""
        return (self.__width + self.__height) * 2


def shape_info(shape):
    """Print shape information"""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
