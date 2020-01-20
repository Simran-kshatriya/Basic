class MyClass:
    name = "Simran"  # now name is the property of my class
 # to craete a function we use the keyword def
# In python every class has built in function called as __init__ and you can also explicitly defined it

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sum(self, a, b): # self is the variable use as the very first parameter and arguement you can name it as anything...
        print (a+b)


x = MyClass("Kushal", 40)
print(x.name)
x.sum(4,5)
del x.name
print(x.age)

