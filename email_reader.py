finalList = list()
fname = input("Enter file name")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    # lineWithoutSpaces = line
    if line.startswith('From '):
        newWords = line.split()
        # print(newWords)
        addingWord = newWords[1]
        # print(addingWord)
        # print(newWords)
        finalList.append(addingWord)
        count = count + 1

for items in finalList:
    print(items)
# print(finalList)
print("There were", count, "lines in the file with From as the first word")
