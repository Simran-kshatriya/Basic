if 5 > 3:
    print(" 5 is grater than 3")

num = 0
if num > 0:
    print("This is a positive number")
elif num == 0:
    print("Number is zero")
else:
    print("This is a negative number")

num1 = [1, 2, 3, 4, 5]
sum = 0
for val in num1:
    sum +=val
print("Total is ", sum)

languages = ["Python", "Java","Ruby","PHP"]
for val in languages:
    print(val)
else:
    print("No Languages left ")

print("Enter a number:")
num2 = int(input())
sum1 = 0
i = 1

while i < num2:
    sum1 = sum1 +i
    i = i + 1
print("Total is :", sum1)