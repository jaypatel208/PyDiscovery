random_string = (
    "Aashiqon mein jiskaa title Titanic O, aashiqon mein jiskaa "
    "title Titanic Muaa, kinaraa dikhaakar ke dubaa de gaya"
)

text = random_string.lower()

count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

for char in text:
    if char == 'a':
        count_a += 1
    elif char == 'e':
        count_e += 1
    elif char == 'i':
        count_i += 1
    elif char == 'o':
        count_o += 1
    elif char == 'u':
        count_u += 1

print("Count of A:", count_a)
print("Count of E:", count_e)
print("Count of I:", count_i)
print("Count of O:", count_o)
print("Count of U:", count_u)
