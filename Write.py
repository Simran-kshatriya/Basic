# Read the file and store all the line in list
# reverse the list
# write the list back to the file
with open('Test.txt','r') as reader:
    content = reader.readlines()  # readlines() uses to get all content into list

    reversed(content)
    with open('Test.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)
