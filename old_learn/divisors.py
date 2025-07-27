def divisors(n):
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            count += 1 if i == n // i else 2
        i += 1
    return count
