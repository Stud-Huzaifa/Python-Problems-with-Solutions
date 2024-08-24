'''. Write a program to accept marks of 6 students and display them in a sorted
manner.'''


marks = []

for i in range(6):
    mark = int(input("Enter marks  of student : "))
    marks.append(mark)

marks.sort()

print("The Sorted list of marks is : ", marks)

