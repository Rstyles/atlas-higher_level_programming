#!/usr/bin/python3
def best_score(a_dictionary: dict):
    biggest: str = None
    if a_dictionary is not None:
        for key in a_dictionary:
            if biggest == None or a_dictionary[key] > a_dictionary[biggest]:
                biggest = key
    return biggest
