class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 60:
            return "D"
        else:
            return "F"

    def display(self):
        print(f"\nName: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.get_grade()}")

# Store all students
students = []

print("Student Management System")

while True:
    name = input("\nEnter student name: ").strip()
    if not name:
        print("Name cannot be empty. Try again.")
        continue

    # Validate age
    while True:
        try:
            age = int(input(f"Enter age for {name}: "))
            if age <= 0:
                print("Age must be a positive number. Try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a whole number for age.")

    # Validate marks
    while True:
        try:
            marks = float(input(f"Enter marks for {name}: "))
            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100. Try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number for marks.")

    # Create and store student object
    student = Student(name, age, marks)
    students.append(student)
    student.display()

    again = input("\nDo you want to add another student? (yes/no): ").strip().lower()
    if again == "no":
        print("\nGoodbye!")
        break

# Display all students at the end
if students:
    print("\n--- All Students ---")
    for s in students:
        s.display()
        print("---")