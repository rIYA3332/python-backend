class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        self.balance += amount
        self.transactions.append(f"Deposited: Rs.{amount}")
        print(f"Rs.{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return
        if amount > self.balance:
            print("Insufficient balance.")
            return
        self.balance -= amount
        self.transactions.append(f"Withdrawn: Rs.{amount}")
        print(f"Rs.{amount} withdrawn successfully.")

    def get_balance(self):
        print(f"\nAccount Owner: {self.owner}")
        print(f"Current Balance: Rs.{self.balance}")

    def get_transactions(self):
        if not self.transactions:
            print("No transactions yet.")
            return
        print(f"\nTransaction History for {self.owner}:")
        for t in self.transactions:
            print(f"  - {t}")


# Main program
print("Welcome to the Bank System")

name = input("Enter account owner name: ").strip()

# Validate initial balance
while True:
    try:
        initial = float(input("Enter initial balance: Rs."))
        if initial < 0:
            print("Initial balance cannot be negative.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a number.")

account = BankAccount(name, initial)

while True:
    print("\nWhat would you like to do?")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter choice (1-5): ").strip()

    if choice == "1":
        try:
            amount = float(input("Enter deposit amount: Rs."))
            account.deposit(amount)
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice == "2":
        try:
            amount = float(input("Enter withdrawal amount: Rs."))
            account.withdraw(amount)
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice == "3":
        account.get_balance()

    elif choice == "4":
        account.get_transactions()

    elif choice == "5":
        print("Thank you for banking with us. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")