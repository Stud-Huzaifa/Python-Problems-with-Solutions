'''Write a program to calculate the grade of a student from his marks from the
following scheme:
90 – 100 => Ex
80 – 90 => A
70 – 80 => B
60 – 70 =>C
50 – 60 => D
<50 => F


# Taking marks as input from the user
marks = float(input("Enter your marks: "))'''


# Taking marks as input from the user
marks = float(input("Enter your marks: "))

# Determining the grade
if 90 <= marks <= 100:
    grade = "Ex"
elif 80 <= marks < 90:
    grade = "A"
elif 70 <= marks < 80:
    grade = "B"
elif 60 <= marks < 70:
    grade = "C"
elif 50 <= marks < 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")
