'''Write a program to print multiplication table of n using for loops in reversed
order.'''
# Taking a number as input from the user
number = int(input("Enter a number to print its multiplication table in reverse: "))

# Printing the multiplication table in reverse order
for i in range(10, 0,):
    print(f"{number} x {i} = {number * i}")
