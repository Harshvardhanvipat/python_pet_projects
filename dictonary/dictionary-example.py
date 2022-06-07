histrogram = dict()
name = input("Enter file: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

for line in handle:
    if line.startswith('From '):
        words = line.split()
        addingWord = words[1]
        # print(addingWord)
        # for word in words:
        histrogram[addingWord] = histrogram.get(addingWord,0) + 1

bigcount = None
bigWord = None
for word,count in histrogram.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigWord = word

print(bigWord, bigcount)
