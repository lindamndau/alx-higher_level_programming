#!/usr/bin/pythong3
def no_c(my_string):
    result = ""
    for character in my_string:
        if character != 'c' or character != 'C':
            result += character
    return result
