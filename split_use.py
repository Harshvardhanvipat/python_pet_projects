finalList = list()
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    lineWithoutSpaces = line.rstrip()
    newWords = lineWithoutSpaces.split()
    for words in newWords:
        if words not in finalList:
            finalList.append(words)
            # print(words)
        finalList.sort()

print(finalList)
