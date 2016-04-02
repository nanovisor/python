#name = raw_input("Enter file:")
#if len(name) < 1 : name = "mbox-short.txt"
handle = open('mbox-short.txt')

for line in handle:
    line = line.rstrip()
    line = line.lower()
    if line == '': continue
    
    words = line.split()
    if words[0] != 'from': continue

    emails = list()
    emails.append(words[1])
    print emails

    count = dict()
    for mail in emails:
        count[mail] = count.get(mail,0)+1
    print count



#    counts = dict()
#    for sender in senders:
#        counts[sender] = counts.get(sender,0) + 1

#    print counts.keys()

#    bigcount = None
#    bigword = None
#    for sender,count in counts.items():
#        if bigcount is None or count > bigcount:
#            bigword = sender
#            bigcount = count
#
#    print bigword, count
