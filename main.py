# Program to calculate the total number of digits in a number

# Get input from the user
number = input("Enter a number: ")

# Remove any negative sign if present
if number.startswith('-'):
    number = number[1:]

# Calculate the number of digits
total_digits = len(number)

# Output the result
print(f"The total number of digits is: {total_digits}")
