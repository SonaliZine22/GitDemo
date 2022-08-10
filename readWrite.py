with open("test.txt") as reader:
    #print(reader.read())
    #print(reader.read(6))
    #print(reader.readline())

    #line =reader.readline()
   # while line != "":
        #print(line)
        #line = reader.readline()

    for line in reader.readlines():
        print(line)



