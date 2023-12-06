#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_dictionary_copy = {}
    for k, v in a_dictionary.items():
        a_dictionary_copy[k] = v * 2
    return a_dictionary_copy
