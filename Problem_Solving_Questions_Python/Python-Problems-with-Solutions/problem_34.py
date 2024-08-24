#. Write a program to calculate the factorial of a given number using for loop.
num = int(input("Enter youR Number: "))
factorial = 1 
for i in range(1 , num):
    factorial *= i

print(f"The Factorial of {num} is {factorial}")    
    
