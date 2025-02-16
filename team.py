def count_solvable_problems():
    n = int(input())
    count = 0

    for _ in range(n):
        problem = list(map(int, input().split))

        if sum(problem) >= 2:
            count += 1

            print(count)


count_solvable_problems()
