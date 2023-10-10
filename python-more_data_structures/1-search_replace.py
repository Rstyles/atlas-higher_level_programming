#!/usr/bin/python3
def search_replace(my_list, search, replace):
    output = []
    for i in range(len(my_list)):
        if my_list[i] != search:
            output.append(my_list[i])
        else:
            output.append(replace)
    return output
