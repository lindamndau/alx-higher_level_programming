#!/usr/bin/python3
def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    else:
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
    for row in range(size):
        for row2 in range(size):
            print("#", end = "")
        print()
