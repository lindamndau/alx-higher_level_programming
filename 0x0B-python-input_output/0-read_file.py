#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, encoding="UTF8") as file:
        read_data = file.read()
        print(read_data, end = " ")
