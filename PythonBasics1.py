print("Hello World...!!")

# Variables are case-sensitive, you can use letters(a-z), underscore, numbers(0-9)
x = 5
y = "python"
print(x)
print(y)

print("I Love " + y)  # concatenate

a = 10
b = 20
print("Sum is :", a + b)

print(" ")
# syntax
if 5 < 1:
    print("5 is greater than 1")
else:
    print("1 is less than 5")


# Function
def sum(p, q):
    print(p + q)


c = sum(50, 20)

print(" ")
print("Casting Examples-")
# Casting
e = int(2)  # It prints 2
f = int(1.5)  # It explicitly converts to the integer so it will print 1 bcoz datatype is int
g = float(1)  # This stores 1.0
h = str(10)  # this will Strore like this "10" as a string

print(e)
print(f)
print(g)
print(h)

# String operations in python

k = "Hello India..."
print(k[1])  # It prints the index position character, it will print e
print(k[6:11])  # It prints India which is starting from index position 6 until index postion 11
print(len(k))  # prints length of variable
print(k.lower())  # it wil print lower case letter
print(k.upper())  # It will print upper case letter

v = "  I am the Coder...!!  "
print(v)  # it will prints with all starting and ending spaces
print(v.strip())  # it has strip(remove) all staring and ending spacses it will just print "I am the coder...!!"
print(v.replace("Coder", "Developer"))  # It will replace Coder to Developer

# Get input
print("Enter Your Name:")
p = input()
print("Hello," + p)
