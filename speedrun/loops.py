numbers = [22, 7, 2002, 20, 8, 2002]
for number in numbers:
    print(number)

evens = [n for n in numbers if n % 2 == 0]
print("Even numbers:", evens)

count = sum(1 for n in numbers if n > 50)
print("Count > 50:", count)

print("total numbers greater than 50:", count)
