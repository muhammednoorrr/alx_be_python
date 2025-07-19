# pattern_drawing.py

# Prompt user for a positive integer
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop using while to handle rows
while row < size:
    # Inner loop using for to handle columns
    for col in range(size):
        print("*", end="")  # Print asterisk without newline
    print()  # Newline after each row
    row += 1
