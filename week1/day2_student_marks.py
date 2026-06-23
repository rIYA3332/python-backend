# Stores student names and marks in a dictionary with grade calculation

# Initialize empty dictionary to store student name and marks as key-value pairs
students = {}

print("Student Marks System")

# Keep accepting student entries until the user chooses to stop
while True:
    name = input("Enter student name: ")

    # Validate marks input — retry until a valid numeric value between 0 and 100 is entered
    while True:
        try:
            marks = float(input(f"Enter marks for {name}: "))
            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100. Try again.")
            else:
                break
        except ValueError:
            # Handles case where user enters a non-numeric value
            print("Invalid input. Please enter a number for marks.")

    # Store the validated marks against the student's name
    students[name] = marks

    # Ask user whether to continue adding more students
    continue_input = input("Do you want to add another student? (yes/no): ").strip().lower()
    if continue_input == "no":
        print("Goodbye!")
        break

# Display results only if at least one student was added
if students:
    print("\n--- Student Marks ---")

    for name, marks in students.items():
        # Assign grade based on marks range
        if marks >= 90:
            grade = "A"
        elif marks >= 80:
            grade = "B"
        elif marks >= 70:
            grade = "C"
        elif marks >= 60:
            grade = "D"
        else:
            grade = "F"

        print(f"{name}: {marks} - Grade {grade}")

    # Display summary statistics
    print(f"\nHighest marks: {max(students.values())}")
    print(f"Lowest marks: {min(students.values())}")
    print(f"Average marks: {sum(students.values()) / len(students):.2f}")