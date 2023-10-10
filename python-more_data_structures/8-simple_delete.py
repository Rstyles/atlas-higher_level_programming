#!/usr/bin/python3
def simple_delete(a_dictionary: dict, key=""):
    key_exists = False
    for k in a_dictionary:
        if k == key:
            key_exists = True
    if key_exists:
        del a_dictionary[key]
    return a_dictionary
