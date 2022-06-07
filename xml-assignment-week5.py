import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

from urllib.request import urlopen



totalSum = list()
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
data = urlopen(url, context=ctx).read()
print("Retrieving ", url)
print('Retrieved', len(data), 'characters')

# here the data type is byte
# print(data)
data.decode()

# print("after decoding")
# print(data)
tree = ET.fromstring(data)

# output <Element 'commentinfo' at 0x10a758868>
# print(type(tree))

# print(type(tree))
lst = tree.findall('comments/comment/count')
print('Count:', len(lst))

for item in lst:
    totalSum.append(int(item.text))

print("Sum: ",sum(totalSum))
