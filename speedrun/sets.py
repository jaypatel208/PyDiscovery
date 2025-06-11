sentence_from_user = input("Type your lyrics: ")

words = sentence_from_user.split()

unique_words = set(words)

# Print results
print("Unique words:", unique_words)
print("Total unique words:", len(unique_words))
