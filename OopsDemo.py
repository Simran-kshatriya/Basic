#Classes are nothing but user defined blueprint or prototype
# sum, multiplication, addition, constant
# Basically class will have methods, variables, instant variables, constructor etc
# Self keyword is mandatory for calling variable names into method
# instance and class variables have whole different purpose
# Constructor name should be __init__
# new keyword is not required when you create object
class Calculator:
    # Whatever variable you define immediately inside the class is called as class variable
    num = 100    # Class variables
    #default constructor
    def __init__(self, a, b):
        #This two are instance variable
        self.firstNumber = a
        self.secondNumber = b

        print("Constructor call atomatically when object is created")

    def getData(self):
        print("Let's Execute method")

    def Summation(self):
        return self.firstNumber + self.secondNumber + self.num


obj = Calculator(2, 3) # Syntax to create object in python
obj.getData()
print(obj.Summation())


obj1 = Calculator(4, 5) # Syntax to create object in python
obj1.getData()
print(obj1.Summation())
