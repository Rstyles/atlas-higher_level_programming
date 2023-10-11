#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    output = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            output += 1
        except:
            print("")
            return output
    print("")
    return output