#!/usr/bin/python3
def multiple_returns(sentence):
    lens = len(sentence)
    if (lens == 0):
        return (0, None)
    return (lens, sentence[0])
