#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    res = list(a_dictionary.keys())[0]
    score = a_dictionary[res]
    for k, v in a_dictionary.items():
        if v > score:
            score = v
            res = k
    return (res)
