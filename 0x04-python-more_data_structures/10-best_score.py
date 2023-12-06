#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        max_score = a_dictionary[list(a_dictionary.keys())[0]]
        max_key = None
        for key, value in a_dictionary.items():
            if value > max_score:
                max_score = value
                max_key = key
        return max_key
