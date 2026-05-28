from abc import ABC

"""Module that defines animals"""


class Animal(ABC):
    """Animal class"""

    @abstractmethod
    def sound(self):
        """Sound of animal"""
        pass


class Dog(Animal):
    """Dog class"""

    def sound(self):
        """return sound of dog as string"""
        return "Bark"


class Cat(Animal):
    """Cat class"""

    def sound(self):
        """return sound of cat as string"""
        return "Meow"
