import urllib
import re
from bs4 import BeautifulSoup as BS
file = open("ans.txt",'r')
sock = urllib.urlopen("http://www.hbs.edu/mba/find-answers/Pages/default.aspx")
soup = BS(sock,"html.parser")
text = file.readlines()
file.close()
for line in text:
	line = line[:-1]
	print soup.find('dt',text = line).find_next_sibling('dd').text
	