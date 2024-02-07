#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, encoding= "UTF-8") as f:
        if not filename:
            open(filename, text)
        if is filename:
            with open(filename, w) as f:
                f.write()
        else:
            num_characters = f.write(text)
            return num_characters
