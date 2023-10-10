#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    results =  map(lambda mult: mult * number, my_list)
    return list(results)
