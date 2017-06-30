from __future__ import print_function
import urllib
import re
from bs4 import BeautifulSoup as BS
file = open("ques.txt",'w')
sock = urllib.urlopen("http://www.hbs.edu/mba/find-answers/Pages/default.aspx")
soup = BS(sock,"html.parser")
ques_tag = soup.find_all("dt")
for tag in ques_tag:
	text = tag.string
	text = text.encode('ascii', 'ignore').decode('ascii')
	print (text , file = file)
query = raw_input("Enter your question:")
print(query, file = file)
file.close()