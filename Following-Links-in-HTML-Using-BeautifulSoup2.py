import urllib
from BeautifulSoup import *

enter = raw_input('Enter url human: ')
#url for parcing
url = enter
poslst = list()


for iter in range(7):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    #list of 3 tags <a>
    tags = soup('a')
    #search <a> tag 3 [2]
    link = tags[17]
    #convert to link
    link = link.get('href', None)
    print link
    url = link
