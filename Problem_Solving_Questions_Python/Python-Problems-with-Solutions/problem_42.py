#4. Write a recursive function to calculate the sum of first n natural numbers.


def sum_of_natural_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_natural_numbers(n - 1)

# Example usage
print(sum_of_natural_numbers(5))  # Output will be 15 (1+2+3+4+5)
