import urllib
from BeautifulSoup import *

html = urllib.urlopen('http://python-data.dr-chuck.net/comments_260431.html').read()
soup = BeautifulSoup(html)

counts = list()
tags = soup('span')
for tag in tags:
    number = int(tag.contents[0])
    counts.append(number)

print sum(counts)
