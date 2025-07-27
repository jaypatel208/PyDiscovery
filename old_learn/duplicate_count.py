def duplicate_count(text):
    count = 0
    unique_char = []
    counted_duplicates = []
    for c in text:
        c_lower = c.lower()
        if c_lower in unique_char and c_lower not in counted_duplicates:
            count += 1
            counted_duplicates.append(c_lower)
        elif c_lower not in unique_char:
            unique_char.append(c_lower)

    return count
