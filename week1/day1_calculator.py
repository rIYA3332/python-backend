def format_num(n):
    return int(n) if n == int(n) else n

while True:
    print("\nSimple Calculator")
    print("Operations: +, -, *, /")

    # number 1 validation
    try:
        num1 = float(input("Enter first number: "))
    except ValueError:
        print("Error: Please enter a valid number!")
        continue

    # operator validation
    operator = input("Enter operator (+, -, *, /): ")
    if operator not in ["+", "-", "*", "/"]:
        print("Error: Invalid operator! Use +, -, * or /")
        continue

    # number 2 validation
    try:
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Please enter a valid number!")
        continue

    result = None

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            result = num1 / num2

    if result is not None:
        print(f"Result: {format_num(num1)} {operator} {format_num(num2)} = {format_num(result)}")

    again = input("\nDo you want to calculate again? (y/n): ")
    if again.lower() != "y":
        print("Goodbye!")
        break