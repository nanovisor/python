#name = raw_input("Enter file:")
#if len(name) < 1 : name = "mbox-short.txt"
handle = open('mbox-short.txt')

counts = dict()

for line in handle:
    line = line.strip()
    if line == '': continue
    words = line.split()
    if words[0] != 'From': continue

    hours = words[5]
    time = hours[:2]

    counts[time] = counts.get(time,0) + 1


list = list()

for k, v in counts.items():
    newtup = (k,v)
    list.append(newtup)
    #print k,v

list.sort()

for k,v in list:
    print k,v
