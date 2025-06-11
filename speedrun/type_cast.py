def safe_add(x, y):
    try:
        num1 = float(x)
        num2 = float(y)
        return num1+num2
    except ValueError:
        return "Both inputs must be numbers"
