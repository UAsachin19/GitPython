print("Hello World!")

a = 5
print(a)

myList = [2, 3.45, "Sachin", "Jakhotiya"]
print(myList)
myList.append("mylist")
print(myList)
myList.insert(0, 31)
print(myList)

b = myList[3]
print(b)

# Empty Dictionary
dict1 = {}
dict1["FirstName"] = "Sachin"
dict1["LastName"] = "Jakhotiya"
print(dict1)

greetings = "Hello World!"

if greetings == "Hello":
    print("Matches")
else:
    print("Not matches")
print("If else completed!")

# For loop

obj = [2, 3, 5, 7, 9]
for i in obj:
    print(i)
summation = 0

for j in range(1, 6, 2):
    summation = summation + j

print(summation)

# While Loop
it = 4
while it > 1:
    print(it)
    it = it - 1
