#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        alph = chr(i)
    else:
        alph = chr(i-32)
    print("{}".format(alph), end="")
