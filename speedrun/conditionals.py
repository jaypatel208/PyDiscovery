def grade(score):
    if score >= 90:
        return "A"
    elif 80 < score < 90:
        return "B"
    elif 70 < score < 80:
        return "C"
    else:
        return "F"


print("My grade: ", grade(82))
