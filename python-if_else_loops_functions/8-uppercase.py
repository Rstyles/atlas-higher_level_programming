#!/usr/bin/python3
def uppercase(str):
    output = ""
    for char in str:
        if ord(char) > 90 and ord(char) <= 122:
            char = chr(ord(char) - 32)
        output += char
    print("{}".format(output))
