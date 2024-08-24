#Write a program to filter a list of numbers which are divisible by 5.

def divisible5(n):
    if(n%5==0):
        return True
    return False


a = [234234,23423426,41241255,1,1515]
f =list(filter(divisible5, a))
print(f)



