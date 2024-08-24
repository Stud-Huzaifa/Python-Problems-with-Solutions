#Write a program to find the greatest of four numbers entered by the user

# Taking four numbers as input from the user

num1 = int(input("Enter Your First Number : "))
num2 = int(input("Enter Your Second Number : "))
num3 = int(input("Enter Your Third Number : "))
num4 = int(input("Enter Your Forth Number : "))

greatest = max(num1, num2, num3 ,num4)
print("tHE Greatest Number  is : " ,greatest)