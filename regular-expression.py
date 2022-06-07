import re
x = 'My 2 favorites are 34 and test 42'
y = re.findall('[0-9]+',x)
# it will return a list, when regular expression goes through
print(y)
y = re.findall('[AEIOU]+',x)
print(y)


# example of greedy matching
z = 'From: Using the : character'
v = re.findall('ˆF.+:?',z)
print(v)
# greedy will take the longer
