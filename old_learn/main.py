print("Hello world")
print("\nString related things")
word = 'Afreen Afreen'
print(len(word))
print("\nList related operations")
squares = [1, 2, 3, 4, 5]
print(squares)
print("First element of list", squares[0])
print("Second element of list", squares[1])
print("Last element of list", squares[-1])
print("Idk i am accessing something", squares[-2:])
print("I still don't know what to do with this", squares[2:45])
print("Shallow copy of list", squares[:])
print("Now let's concatenate list:  ")
rectangles = [6, 7, 8, 9, 10]
print(squares + rectangles)
print("List are immutable unlike string: ")
cubes = [3, 6, 9, 12, 15, 19]
print("Initial List", cubes)
cubes[5] = 18
print("List after fixing mistake: ", cubes)
print("Wait let's add few items in list or manager will not be happy with it :)")
cubes.append(21)
print("Let's figure out 8th element of list: ")
cubes.append(3 * 8)
print("List after adding 8th element: ", cubes)

print("\nAssignment to slices: ")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print("First let's see how it takes letters", letters)

print("Let's replace some items in letters: ")
letters[2:6] = ['C', 'D', 'E', 'F']
print(letters)
print("Yo boi what's the length of letter list??", len(letters))

print("\nNesting of lists:")
a = ['a', 'b', 'c']
n = ['1', '2', '3']
x = [a, n]

print("Print first element of list x: ", x)
print("Print second element of list x: ", n)
print("Accessing first element of first list: ", x[0][0])
print("Accessing last element of second list: ", x[1][-1])

print("3.2. First Steps Towards Programming: ")
