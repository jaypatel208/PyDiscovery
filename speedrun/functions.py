def calc_area(length=1, width=1):
    return length * width


print("Area of l=5 and w=5: ", calc_area(5, 5))
print("Default area: ", calc_area())


def describe_person(role, **kwargs):
    print("Role:", role)
    for k, v in kwargs.items():
        print(f"{k}: {v}")


describe_person("Author", name="Dhani", age=30)
