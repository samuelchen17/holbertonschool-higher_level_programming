#!/usr/bin/python3


"""This module contains a class Student"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            result = {}

            for key in attrs:
                if hasattr(self, key):
                    value = getattr(self, key)
                    result[key] = value
            return result

        return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
