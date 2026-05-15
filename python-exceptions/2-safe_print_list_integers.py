#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    count = 0

    for i in range(x):
        try:
            value = my_list[i]
            try:
                print("{:d}".format(value), end="")
                count += 1
            except (ValueError, TypeError):
                pass
        except IndexError:
            break

    print()
    return count
