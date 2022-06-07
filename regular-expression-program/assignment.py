import re
total = 0

name = "regex_sum_377141.txt"
fh = open(name)
# re.findall('[0-9]+',x)
for line in fh:
    if line is not None:
        total_list = re.findall('[0-9]+',line)
        for number in total_list:
                total = total + int(number)


print (total)
        # if len(total_list) != 0 :
        #     # print(total_list)
        #     global_list.append(total_list)
        #     print(global_list)
