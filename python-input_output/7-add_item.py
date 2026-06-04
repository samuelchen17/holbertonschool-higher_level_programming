#!/usr/bin/python3


"""This module contains a function"""

import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    loaded = load_from_json_file("add_item.json")
except FileNotFoundError:
    loaded = []

my_list = sys.argv[1:]
new_list = loaded + my_list

save_to_json_file(new_list, "add_item.json")
