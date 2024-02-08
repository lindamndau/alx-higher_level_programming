#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """check if object is instance of
    args:
        obj: object argument
        a_class: class to check
    Return:
        True or False
    """
    return isinstance(obj, a_class)
