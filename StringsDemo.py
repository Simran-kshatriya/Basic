str = "simrankshatriya18@gmail.com"
str1 = " Email Address"
str2 = "simrankshatriya"


print(str[1]) # it prints the index position of string, it will print i

print(str[0:6])  # it will print simran index position starts with zero

print(str + str1)

print(str2 in str)  # Checks Substring

var = str.split(".")

print(var)

print(var[1])

str3 = " Amazing "
print(str3.strip())  # It will remove the white spaces
print(str3.rstrip())   # it will remove right side white space similarly it also work for left side space using lstrip() function
print((str3.lstrip()))  # remove left side white space
