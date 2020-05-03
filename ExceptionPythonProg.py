ItemInCart = 0

if ItemInCart != 2:
    #raise Exception("Products cart count not matching!")
    pass

assert (ItemInCart == 0)

try:
    with open('check.txt', 'r') as reader:
        reader.readlines()

except Exception as e:
    print(e)
    print("Try blocks condition failed")

finally:
    print("Finally will always run")

