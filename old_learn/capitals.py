def capitals(word):
    result = []
    for i, c in enumerate(word):
        if c.isupper():
            result.append(i)

    return result


print(capitals("DhRuvi"))
