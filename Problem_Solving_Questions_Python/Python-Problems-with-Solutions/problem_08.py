'''Write a program to fill in a letter template given below with name and date.
letter = '''

# Template for the letter
letter = '''
Dear {name},
You are selected!
Date: {date}
'''
# Taking user input for name and date
name = input("Enter your name: ")
date = input("Enter the date: ")
 
## Filling the template
filled_letter = letter.format(name = name, date = date )

#Displaying the Letter

print(filled_letter)