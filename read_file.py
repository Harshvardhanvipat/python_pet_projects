fileName = input("Enter file name: ")
fileHandle = open(fileName)

for line in fileHandle:
    line = line.rstrip().upper()
    print(line);
