#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    unique_list = dict(zip(my_list, ['unique'] * len(my_list))).keys()
    for integer in unique_list:
        sum += integer
    return (sum)
