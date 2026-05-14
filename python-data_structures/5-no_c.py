#!/usr/bin/python3
def no_c(my_string):
    c_removed_list = ""
    for letter in my_string:
        if letter not in "cC":
            c_removed_list += letter
    return c_removed_list
