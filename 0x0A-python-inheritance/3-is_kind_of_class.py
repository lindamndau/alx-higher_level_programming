#!/usr/bin/python3
def is_kind_of_class(obj, a_class):

    if isinstance(obj, a_class) or isinstance(obj, a_class(a_class)):
        return True
    return False
