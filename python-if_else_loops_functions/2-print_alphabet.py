#!/usr/bin/python3
values = ""
for i in range(26):
    char = chr(i + 97)
    values = values + char
print("{}".format(values), end="")
