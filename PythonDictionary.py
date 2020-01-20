# Dictionary {K:V} : unordered | indexed | changeable | no duplicates

my_dic = {
    "Class" : "Car",
    "Name"  : "Toyota",
    "Price" :  450000
}
print(my_dic)
print(my_dic["Class"])

print(my_dic.get("Name"))
print(my_dic.values())
print(" ")
for val in my_dic:
    print(my_dic[val])

for x,y in my_dic.items():  # This will get both key and values
    print(x, y)

my_dic["Name"] = "Swift"    # It updates the value
print(my_dic)

my_dic["Color"] = "Black"   # to add new element we use the same thing
print(my_dic)

my_dic.pop("Color")
print(my_dic)
my_dic.popitem()
print(my_dic)

del my_dic["Class"]
print(my_dic)

my_dic.clear()
print(my_dic)

del my_dic
