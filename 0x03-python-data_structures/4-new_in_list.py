#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    for idx in my_list:
        new_list = my_list.copy()
        if idx < 0 or idx > len(my_list):
            return my_list2
        return my_list
        new_list.pop([idx])
        new_list.insert(idx, element)
        return new_list
