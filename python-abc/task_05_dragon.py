"""Module that defines Dragon class and mixin."""


class SwimMixin:
    """SwimMixin class"""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """FlyMixin class"""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")


draco = Dragon()

draco.fly()
draco.swim()
draco.roar()
