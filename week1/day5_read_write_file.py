filename = "notes.txt"

# Write to file
with open(filename, "w") as file:
    file.write("Hello, this is line 1.\n")
    file.write("This is line 2.\n")
    file.write("This is line 3.\n")

print("File written successfully.")

# Read from file
print("\nReading file contents:")
with open(filename, "r") as file:
    contents = file.read()
    print(contents)

# Append to file
with open(filename, "a") as file:
    file.write("This is an appended line.\n")

print("Line appended successfully.")

# Read again to confirm append
print("\nFile after appending:")
with open(filename, "r") as file:
    for line in file:
        print(line.strip())