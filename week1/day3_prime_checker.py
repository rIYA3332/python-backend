
def is_prime(n):
    # Numbers less than 2 are not prime
    if n < 2:
        return False
    # Check divisibility from 2 up to square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Get input from user
while True:
    try:
        num = int(input("Enter a number to check if it is prime: "))
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
        
        again = input("Check another? (y/n): ").strip().lower()
        if again == "n":
            print("Goodbye!")
            break
    except ValueError:
        print("Invalid input. Please enter a whole number.")