def count_sheep(n):
    output = ""
    sheep_extra = " sheep..."
    for c in range(1, n + 1):
        output += str(c) + sheep_extra
    return output