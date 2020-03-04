greeting = "Good Morning,,Have a Good day...!!!"

if greeting == "Good Morning,,Have a Good day...!!!":
    # IF you add just good morning instead of Good Morning,,Have a Good day...!!! it will print Condition do not match
    print("Condition Matches")
else:
    print("Condition do not match")

print(" ")

# For loop
obj = [11, 12, 13, 14]
for val in obj:
    print(val+2)

# sum of first natural number 1+2+3+4+5 = 15
sum = 0
for j in range(1,6): # range(i,j) -> i to j-1
    print(j)

    sum = sum + j
print(sum)

print("____________________________________________________")

for k in range(1, 10, 5):
    print(k)  # It will print 1 and 6 with the difference of 5