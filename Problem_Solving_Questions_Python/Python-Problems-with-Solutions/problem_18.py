'''Write a program to input eight numbers from the user and display all the unique
numbers (once).'''

# Initialize an empty list to store user inputs
numbers = []

# Taking eight numbers as input from the user
for i in range(1, 9):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)

# Converting the list to a set to get unique numbers
unique_numbers = set(numbers)

# Displaying the unique numbers
print("\nThe unique numbers are:")
for num in unique_numbers:
    print(num)
