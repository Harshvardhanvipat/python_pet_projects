text = "X-DSPAM-Confidence:    0.8475";
newText = text.find(":")
#print(newText)
indexOfSpecialCharacter = newText + 1
stringWithSpaces = (text[indexOfSpecialCharacter:30])
stringWithoutSpaces = stringWithSpaces.strip()
print(float(stringWithoutSpaces))
