def remove_exclamation_marks(s):
    sanitized_string = ""
    for i in s:
        if i != "!":
            sanitized_string += i

    return sanitized_string
