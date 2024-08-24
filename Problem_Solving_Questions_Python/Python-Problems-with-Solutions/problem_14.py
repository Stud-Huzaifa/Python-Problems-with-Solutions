#Check that a tuple type cannot be changed in python
# Create a tuple
my_tuple = (1, 2, 3, 4, 5)

# Try to modify an element of the tuple (this will raise an error)
try:
    my_tuple[0] = 10
except TypeError as e:
    print("Error:", e)
    print("This confirms that tuples are immutable and cannot be changed.")



