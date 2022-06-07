histrogram = dict()
name = input("Enter file: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)


lst = list()
for line in handle:
    if line.startswith('From '):
        words = line.split(':')
        hours = words[0].split()
        # print(hours[5])
        addingWord = str(hours[5])
        # print(addingWord)
        # print(addingWord)
        # for word in words:
        histrogram[hours[5]] = histrogram.get(hours[5],0) + 1

for key,val in histrogram.items():
    newtup = (key,val)
    lst.append(newtup)
lst = sorted(lst)

for key,val in lst:
    print(key,val)

# print(histrogram)

# print(bigWord, bigcount)
