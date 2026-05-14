#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    div_2_bool = []
    for i in range(len(my_list)):
        div_2_bool.append(my_list[i] % 2 == 0)
    return div_2_bool
