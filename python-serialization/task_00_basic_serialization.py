"""this module contains functions related to serialization and deserialization"""

import json


def serialize_and_save_to_file(data, filename):
    """function that serializes and saves to file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """function that loads a file then deserializes"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
