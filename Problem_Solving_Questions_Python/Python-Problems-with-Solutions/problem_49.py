''''Write a class “Calculator” capable of finding square, cube and square root of a
number.
'''

class Calculator:
    def square(self , n):
        return n **2
    
    def cube(self , n):
        return n**3

    def square_root(self , n): 
   
    @staticmethod
    def greet ():
        print("Hello Welcome to the Calculator")


calc = Calculator()
Calculator.greet()        
print(calc.square(4))       # Output will be 16
print(calc.cube(3))         # Output will be 27
print(calc.square_root(16)) # Output will be 4.0