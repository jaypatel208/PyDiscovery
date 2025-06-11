def solve_problem(w):
    if w > 2 and w % 2 == 0:
        return "YES"
    else:
        return "No"


w = int(input())
print(solve_problem(w))


def abbrv_word(word):
    if len(word) > 10:
        return word[0] + str(len(word)-2) + word[-1]
    return word
