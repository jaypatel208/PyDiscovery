user_data = {
    "name": "pvtbyjd",
    "password": 1234
}


def ask_credentials():
    username = input("Enter username: ")
    try:
        password = int(input("Enter password (digits only): "))
    except ValueError:
        print("Password must be digits!")
        return None, None
    return username, password


def login(user_data):
    attempts = 3
    while attempts > 0:
        username, password = ask_credentials()

        if username == user_data["name"] and password == user_data["password"]:
            print("Login successful!")
            return True
        else:
            attempts -= 1
            print(f"Incorrect credentials. Attempts left: {attempts}")
              
    print("🔒 Account locked due to too many failed attempts.")
    return False


# Run the login
login(user_data)
