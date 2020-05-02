file = open('test.txt')

#print(file.read(10))
#print(file.readline())

values = file.readlines()

for i in values:
    print(i)

#line = file.readline()

#while line != '':
#    print(line)
#    line = file.readline()



file.close()
