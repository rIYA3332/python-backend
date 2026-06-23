def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n × (n-1)!
    return n * factorial(n - 1)

# Get input from user
while True:
    try:
        num = int(input("Enter a number to find its factorial: "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print(f"{num}! = {factorial(num)}")
            break
    except ValueError:
        print("Invalid input. Please enter a whole number.")