def alphabet_position(text):
    result = []
    for c in text:
        if c.lower().isalpha():
            position = ord(c.lower()) - ord('a') + 1
            result.append(str(position))

    return ' '.join(result)