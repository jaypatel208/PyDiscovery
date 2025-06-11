expenses = []


def show_menu():
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. Show Total Spent")
    print("3. Show Expenses by Category")
    print("4. Show High Expenses (> ₹100)")
    print("5. Exit")


def add_expense():
    try:
        amount = float(input("Enter amount: ₹"))
        category = input("Enter category (e.g. food, travel, etc): ").lower()
        expenses.append({"amount": amount, "category": category})
        print("Expense added.")
    except ValueError:
        print("Please enter a valid number.")


def show_total():
    total = sum(item["amount"] for item in expenses)
    print(f"Total spent: ₹{total:.2f}")


def show_by_category():
    category_totals = {}
    for item in expenses:
        cat = item["category"]
        category_totals[cat] = category_totals.get(cat, 0) + item["amount"]

    print("--- Totals by Category ---")
    for cat, total in category_totals.items():
        print(f"{cat.capitalize()}: ₹{total:.2f}")


def show_high_expenses():
    print("--- High Expenses (Over ₹100) ---")
    for item in expenses:
        if item["amount"] > 100:
            print(f"{item['category'].capitalize()}: ₹{item['amount']}")


while True:
    show_menu()
    choice = input("Choose an option (1–5): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_total()
    elif choice == "3":
        show_by_category()
    elif choice == "4":
        show_high_expenses()
    elif choice == "5":
        print("Goodbye! Tracking ended.")
        break
    else:
        print("Invalid choice. Please try again.")
