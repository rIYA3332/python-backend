# Backend Internship - Namlo Technologies

Weekly assignments completed during the Backend Internship program at Namlo Technologies Pvt. Ltd. Each week covers a specific area of backend development, starting from Python fundamentals and progressing through Django, REST APIs, and databases.

---

## Prerequisites
- Python 3.10 or higher

## Usage

```bash
# Clone the repository
git clone https://github.com/rIYA3332/<repo-name>.git
cd <repo-name>

# Run any file directly
python week1/day1_calculator.py
```

---

## Weekly Assignments

### Week 1 - Python Fundamentals

---

#### Day 1 - Python Basics
**Concepts Covered:** Variables, Data Types, Input/Output, Conditions

**Practice Task: Even/Odd Checker**
Takes a number as input and determines whether it is even or odd using the modulo operator (`%`). If the remainder when divided by 2 is 0, the number is even, otherwise it is odd.

**Assignment: Calculator Program**
A fully interactive calculator that supports addition, subtraction, multiplication, and division.

Key implementation details:
- Input validation using `try/except` to handle non-numeric input gracefully
- Operator validation to ensure only `+`, `-`, `*`, `/` are accepted
- Division by zero check with a clear error message
- Output formatting that removes unnecessary decimal points, so `5.0` displays as `5`
- Continuous loop that allows the user to perform multiple calculations and exit when done

---

#### Day 2 - Collections
**Concepts Covered:** List, Tuple, Set, Dictionary

**Practice Task: Remove Duplicates from List**
Removes duplicate values from a list while preserving the original insertion order.

Key implementation details:
- Uses a `set` to track already-seen values for fast lookup
- Uses a separate `list` to store unique results in their original order
- Chosen over the simpler `list(set())` approach because `set()` does not guarantee order

**Assignment: Student Marks Dictionary**
An interactive program that stores student names and their marks in a dictionary, assigns letter grades, and displays summary statistics.

Key implementation details:
- Uses a dictionary with student name as the key and marks as the value
- Nested `while` loop with `try/except` ensures marks input is always a valid number between 0 and 100
- Grade assignment using `if/elif` chain covering A through F
- Summary statistics display highest, lowest, and average marks using built-in `max()`, `min()`, and `sum()` functions
- Continues accepting students until the user explicitly types `no`, with `.strip().lower()` to handle varied input casing

  
---


#### Day 3 - Functions
**Concepts Covered:** Functions, Lambda, Map, Filter

**Practice Task: Factorial Function**
Calculates the factorial of a given number using recursion.

Key implementation details:
- Uses a recursive function where `n! = n × (n-1)!`
- Base case stops recursion when `n` is 0 or 1
- Input validation to reject negative numbers and non-integer input
- Recursion is preferred here for its clarity and mathematical elegance

**Assignment: Prime Number Checker**
Checks whether a given number is prime and allows repeated checks in a loop.

Key implementation details:
- Only checks divisors up to the square root of `n` for efficiency
- Numbers less than 2 are explicitly handled as non-prime
- Input validation using `try/except` to handle non-numeric input
- Continuous loop allows the user to check multiple numbers and exit when done
