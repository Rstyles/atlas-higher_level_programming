#!/usr/bin/python3
def multiple_returns(sentence):
    length = 0
    first_Char = 'None'
    if len(sentence) > 0:
        length = len(sentence)
        first_Char = sentence[0]
    return (length, first_Char)
