user_data = {
   "name": "Dhruvi",
   "age": 24,
   "hobbies": ["Travel", "Badminton"],
   "location": ("Ahmedabad", "India"),
   "is_active": False
}


def analyze_user_profile(user):
    name = user["name"]
    print("Name (upper):", name.upper())

    age = user["age"]
    age += 1
    print("Age next year:", age)

    hobbies = user["hobbies"]
    hobbies.append("Photography")
    print("Updated hobbies:", hobbies)
    print("Total hobbies:", len(hobbies))

    unique_hobbies = set(hobbies)
    print("Unique hobbies:", unique_hobbies)

    location = user["location"]
    city, country = location
    print("City:", city)
    print("Country:", country)
    is_active = user["is_active"]
    print("Active user?", "Yes" if is_active else "No")

    print("Type of name:", type(name))
    print("Type of age:", type(age))
    print("Type of hobbies:", type(hobbies))
    print("Type of location:", type(location))
    print("Type of is_active:", type(is_active))


analyze_user_profile(user_data)
