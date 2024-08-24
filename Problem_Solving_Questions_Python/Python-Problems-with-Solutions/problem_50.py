'''Create a class with a class attribute a; create an object from it and set ‘a’
directly using ‘object.a = 0’. Does this change the class attribute?'''

class Myclass:
    a = 0


obj = Myclass
obj.a = 10

print(obj.a)
print(Myclass.a)