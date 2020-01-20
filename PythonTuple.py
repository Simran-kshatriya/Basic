# Tuple is  ordered | indexed | unchangeable and uses () circular bracket
my_tuple = ("Mumbai", " Pune", "Nashik")
print(my_tuple)

print(my_tuple[1])
print(" ")
# when we give minus(-) indexed it starts from back
print(my_tuple[-1])

print(my_tuple[0:2]) # range

print("Printing using for loop")
for val in my_tuple:
    print(val)

print(len(my_tuple))

my_tuple_2 = ("Delhi",(1,2,3),["India","America","China"])
print(my_tuple_2)
print(my_tuple_2[2][1])

my_tuple_2[2][1] = "New York"
print(my_tuple_2)

print("Delhi"in my_tuple_2) # It gives True bcoz it is present in tuple
print("Cherry" in my_tuple_2) # It gives False bcoz it is not present in our tuple
