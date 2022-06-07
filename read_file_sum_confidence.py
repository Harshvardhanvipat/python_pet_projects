fileName = input("Enter file name: ")
fileHandle = open(fileName)
counter = 0
total = 0
for line in fileHandle:
    line = line.rstrip()
    if "X-DSPAM-Confidence:" in line:
        indexOfSpecialCharacter = line.find(":")
        stringWithSpaces = (line[indexOfSpecialCharacter+1:30])
        stringWithoutSpaces = stringWithSpaces.strip()
        total = float(stringWithoutSpaces) + float(total)
        counter = counter + 1


average = total / counter
average = round(average, 12)
print("Average spam confidence:",average)
