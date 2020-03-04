ItemsInCart = 0
#2 items will be added to cart

if ItemsInCart != 2:  #raise Exception("Products cart count not matching")
    pass

assert(ItemsInCart == 0)

try:
    with open('Test.txt','r') as reader:
        reader.read()

except:
    print("I reached this block because there is failure in try block")

try:
    with open('Test.txt','r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("Cleaning up records")