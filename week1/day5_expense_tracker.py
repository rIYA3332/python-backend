# Tracks expenses using file handling, exception handling, and decorators

import os
from datetime import datetime

FILENAME = "expenses.txt"

# Decorator to log each action performed
def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Running: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_action
def add_expense(category, amount, description):
    """Add a new expense to the file."""
    try:
        amount = float(amount)
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        with open(FILENAME, "a") as file:
            file.write(f"{datetime.now().strftime('%Y-%m-%d')},{category},{amount:.2f},{description}\n")
        print(f"Expense added: {category} - Rs.{amount:.2f} ({description})")
    except ValueError:
        print("Invalid amount. Please enter a number.")

@log_action
def view_expenses():
    """Read and display all expenses from the file."""
    if not os.path.exists(FILENAME):
        print("No expenses recorded yet.")
        return
    try:
        with open(FILENAME, "r") as file:
            lines = file.readlines()
        if not lines:
            print("No expenses recorded yet.")
            return
        print("\n--- Expense History ---")
        total = 0
        for line in lines:
            date, category, amount, description = line.strip().split(",")
            print(f"{date} | {category} | Rs.{amount} | {description}")
            total += float(amount)
        print(f"\nTotal Spent: Rs.{total:.2f}")
    except Exception as e:
        print(f"Error reading file: {e}")

@log_action
def clear_expenses():
    """Clear all expenses from the file."""
    if not os.path.exists(FILENAME):
        print("No expenses to clear.")
        return
    with open(FILENAME, "w") as file:
        pass
    print("All expenses cleared.")


# Main program
print("Simple Expense Tracker")

while True:
    print("\nWhat would you like to do?")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Clear All Expenses")
    print("4. Exit")

    choice = input("Enter choice (1-4): ").strip()

    if choice == "1":
        category = input("Enter category (e.g. Food, Transport): ").strip()
        if not category:
            print("Category cannot be empty.")
            continue
        amount = input("Enter amount: Rs.")
        description = input("Enter description: ").strip()
        if not description:
            print("Description cannot be empty.")
            continue
        add_expense(category, amount, description)

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        confirm = input("Are you sure you want to clear all expenses? (yes/no): ").strip().lower()
        if confirm == "yes":
            clear_expenses()
        else:
            print("Clear cancelled.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")