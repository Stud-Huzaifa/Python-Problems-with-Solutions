#Write a program to sum a list with 4 numbers.

numbers = []

for i in range(4):
     number = int(input("Enter Your Numbers: "))
     numbers.append(number)
total_sum = sum(numbers)

#Display
print("The sum of the numebers: " ,total_sum)



