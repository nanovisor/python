#fname = raw_input("Enter file name: ")
fh = open('mbox-short.txt')
count = 0
total = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue

    line = line.strip()
    startp = line.find(":")
    line = line[startp+1: ]
    line = float(line)

    count = count + 1
    total = total + line
    #print line,count

print "Average spam confidence:", total / count
