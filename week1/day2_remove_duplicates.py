numbers = [1, 3, 2, 5, 3, 1, 7, 2, 8, 5]

# Track numbers we have already encountered
seen = set()

# Store unique numbers in their original order
unique = []

for num in numbers:
    # Only process numbers we have not seen before
    if num not in seen:
        # Mark this number as seen so duplicates are skipped
        seen.add(num)
        # Add to result list, preserving original order
        unique.append(num)

print("Original list:", numbers)
print("Without duplicates:", unique)
