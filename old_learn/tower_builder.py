def tower_builder(n_floors):
    result = []
    for i in range(n_floors):
        stars = '*' * (2 * i + 1)
        spaces = ' ' * (n_floors - i - 1)
        line = spaces + stars + spaces
        result.append(line)
    return result
