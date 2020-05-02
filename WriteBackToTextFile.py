with open('test.txt', 'r') as filereadder:
    content = filereadder.readlines()
    reversed(content)
    with open('test.txt', 'w') as filewriter:
        for line in reversed(content):
            filewriter.write(line)

