def count(s):
    dictionary = {}
    for c in s:
        if c in dictionary:
            dictionary[c] += 1
        else:
            dictionary[c] = 1
    return dictionary