def remove_smallest(numbers):
    if not numbers:
        return []

    smallest = min(numbers)

    smallest_index = numbers.index(smallest)

    result = numbers[:smallest_index] + numbers[smallest_index + 1 :]

    return result


print(remove_smallest([5, 3, 2, 1, 4]))
