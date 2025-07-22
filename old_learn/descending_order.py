def descending_order(num):
    num_list = []
    num_str = str(num)
    for d in num_str:
        num_list.append(d)

    num_list.sort(reverse=True)
    result = "".join(num_list)
    return int(result)
