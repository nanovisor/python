import re
fhand = open('regex_sum_260426.txt')
numlist = list()

for line in fhand:
    line = line.rstrip()
    if line == '': continue
    #print line
    numbers = re.findall('[0-9]+', line)
    #print numbers
    if len(numbers) < 1: continue
    numlist.append(numbers)

print numlist
numbers = list()
for sublist in numlist:
    for numbr in sublist:
        numbr = int(numbr)
        numbers.append(numbr)
        print numbr

print 'sum is', sum(numbers)



#read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.
