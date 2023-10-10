#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_same = set_1 & set_2
    for element in set_same:
        set_1.discard(element)
        set_2.discard(element)
    return set_1 | set_2