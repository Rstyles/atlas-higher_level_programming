#!/usr/bin/python3
def uppercase(str):
    print_string = ""
    for char in str:
        if ord(char) > 90 and ord(char) < 122:
            char = chr(ord(char) - 32)
        print_string += char
    print(print_string)
