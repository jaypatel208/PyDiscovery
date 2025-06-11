def safe_divide(a, b):
    try:
        result = float(a) / float(b)
        print("A / B =", result)
    except ValueError:
        print("Invalid input: Please enter numbers.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")


try:
    a_input = input("Enter value of a: ")
    b_input = input("Enter value of b: ")
    safe_divide(a_input, b_input)
except Exception as e:
    print("Unexpected error:", e)
