file = open('test.txt')

#print(file.read(10))
#print(file.readline())

line = file.readline()

while line != '':
    print(line)
    line = file.readline()


file.close()
