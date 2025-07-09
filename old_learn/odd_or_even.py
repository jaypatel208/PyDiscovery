def odd_or_even(arr):
    sum_of_array = sum(arr)
    if sum_of_array % 2 == 0:
        return "even"
    else:
        return "odd"
