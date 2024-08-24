'''Write a program to print the following star pattern.
* * *
* * for n = 3
* * *'''

n = 3  # Number of rows
for i in range(1, n + 1):
    if i % 2 == 0:
        print('* ' * (n - 1))
    else:
        print('* ' * n)
