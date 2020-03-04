file = open('test.txt')
# print(file.read(5))      #Read all contents of file

# Read one single line at a time readline()
# print(file.readline())
# print(file.readline())

# print line by line using readline method
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

# readlines returns list containing each line in the file as a list item
# print(file.readlines())

for line in file.readlines():
    print(line)

file.close()