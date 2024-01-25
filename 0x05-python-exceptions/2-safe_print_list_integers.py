#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    for x in my_list:
        try:
            print("{:d}".format(x))
            return my_list[x]
        except IndexError:
            print()
