def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input("Enter a number: "))
print("Even?", is_even(num))
