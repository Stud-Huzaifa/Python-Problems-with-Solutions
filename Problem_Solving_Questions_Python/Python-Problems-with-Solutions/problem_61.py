'''Write a program to find the maximum of the numbers in a list using the reduce
function.'''

from functools import reduce

l = [324234,123145,1411,1231245,131]
def greater(a,b):
    if (a > b):
     return a
    return b

print(reduce(greater,l))