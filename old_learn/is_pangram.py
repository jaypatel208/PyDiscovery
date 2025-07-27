def is_pangram(st):
    letters_found = set()
    for char in st.lower():
        if char.isalpha():
            letters_found.add(char)

    return len(letters_found) == 26