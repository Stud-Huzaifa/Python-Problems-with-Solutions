#Write a program to store seven fruits in a list entered by the user

# Initialize an empty list to store the fruits
fruits = []

# Loop to take input of 7 fruits from the user
for i in range(7):
    fruit = input(f"Enter the name of fruit {i+1}: ")
    fruits.append(fruit)

# Display the list of fruits
print("The list of fruits is:", fruits)
