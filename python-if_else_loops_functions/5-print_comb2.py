#!/usr/bin/python3
for i in range(100):
    if i <= 98:
        print("{:0d}, ".format(i), end="")
    else:
        print("{:0d}".format(i))
