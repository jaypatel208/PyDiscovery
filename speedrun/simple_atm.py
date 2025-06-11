current_balance = 1000


def show_menu():
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")


while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        print(f"Your current balance is ₹{current_balance}")

    elif choice == "2":
        amount = float(input("Enter deposit amount: ₹"))
        if amount > 0:
            current_balance += amount
            print(f"Deposited ₹{amount}")
        else:
            print("Invalid deposit amount.")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: ₹"))
        if 0 < amount <= current_balance:
            current_balance -= amount
            print(f"Withdrawn ₹{amount}")
        else:
            print("Insufficient balance or invalid amount.")

    elif choice == "4":
        print("Thank you! Exiting ATM.")
        break

    else:
        print("Invalid choice. Please select 1–4.")
