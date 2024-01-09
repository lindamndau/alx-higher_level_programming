#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == 0:
        return None
    MAX = 0
    for num in my_list[1:]:
        if num > MAX:
            MAX = num
    return MAX
