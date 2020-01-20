# List []  = Ordered collection | indexed | changeble |duplicates

my_list = ["Black" , " Red" , "Blue"]
print(my_list)
print(my_list[2])

my_list[2] = "Pink"
print(my_list)

for color in my_list:
    print(color)

print(len(my_list))

my_list.append("Green")
print(my_list)

my_list.insert(3,"White")
print(my_list)

my_list.remove("Pink")
print(my_list)

my_list.pop()
print(my_list)

my_list.pop(1)
print(my_list)

del my_list[1]
print(my_list)

my_list.clear()
print(my_list)

fruits = ["Apple", "Orange", "Cherry"]
print(fruits)
fruits.reverse()
print((fruits))
print(" ")

list_2 = ["Simran", 1,2,3.0]
print(list_2)
list_3 = ["Simran", [1,2, 3.4],['x','y','z']] # nested list(list within list)
print(list_3[1][2])