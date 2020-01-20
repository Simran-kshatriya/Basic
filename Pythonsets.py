# Set   {}  :  unordered | unindexed |no duplicates
my_set = {"Table", "Chair", "Bench"}
print(my_set)
print(" ")

for x in my_set:
    print(x)

print(" ")

# It checks whether the particular value is present or not
print("Table" in my_set)

my_set.add("Bed")
print(my_set)

my_set.update(["Stool","Sofa set"])
print(my_set)

print(len(my_set))

my_set.remove("Stool")
print(my_set)

my_set.discard("Bench")
print(my_set)

my_set.pop()
my_set.clear()
print(my_set)

print(" ")

set1 = {"Black", 1,2,(3,4,5,6)}
print(set1)

my_list = [1,2,3]
print(my_list)

my_list_1 = set(my_list)
print(my_list_1)
print(" ")

# UNION | INTERSECTION | DIFF | SYMMENTRIC DIFF

A = { 'A', 'B', 'C', 1, 2, 3}
B = { 'B', 'C', 3, 4, 5}
print(" ")
print("UNION IS :")
print(A.union(B))
print(A | B)

print(" ")
print("INTERSECTION IS")
print(A.intersection(B))
print(A & B)

print(" ")
print("DIFFERENCE IS :")
print(A.difference(B))
print(A - B)

print(" ")
print("SYMMENTRIC DIFFERENCE IS :")
print(A.symmetric_difference(B))
print(A ^ B)