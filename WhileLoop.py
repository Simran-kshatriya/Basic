it = 4

while it > 1:
    if it != 3:  # It will not print 3
        print(it)

    it = it - 1

print("___________________________________________________")

a = 4
while a > 1:
    if a == 3:
        break
    print(a)

    a = a - 1

print("__________________________________________________")

b = 10

while b > 1:
    if b == 9:
        continue
    if b == 3:
        break
    print(b)

    b = b - 1

print("While Loop executes successfully")