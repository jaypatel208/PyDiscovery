a, b = 0, 1
while a < 10:
    print(a, end=',')
    a, b = b, a+b

x = int(input("Please enter an integer: "))
if (x < 0):
    x = 0
    print("Negative changed to zero")
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

words = ['fruit', 'vegetable', 'objects']
for w in words:
    print(w, len(w))

users = {'Dhruvi': 'active', 'Pinky': 'inactive',
         'Parth': 'active', 'Nancy': 'active'}

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(active_users)

# 4.3 The range function
for i in range(5):
    print(i)