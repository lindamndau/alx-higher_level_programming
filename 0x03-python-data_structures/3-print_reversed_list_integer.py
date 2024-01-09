#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for num in my_list:
        numbers = my_list[::-1]
        print("{num}".format(numbers))
