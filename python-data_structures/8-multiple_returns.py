#!/usr/bin/python3
def multiple_returns(sentence):
    length = None
    first_Char = ''
    if len(sentence) > 0:
        length = len(sentence)
        first_Char = sentence[0]
    return (length, first_Char)
