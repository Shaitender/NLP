from __future__ import print_function
import urllib
import re
from bs4 import BeautifulSoup as BS
from collections import defaultdict
from gensim import corpora,models,similarities
#from stemming.lovins import stem
import string
import re
import sys

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

stoplist = []
f=open('stopword.txt','r')
file = open('ques.txt','r')
for line in f :
    line=line[0:-2]
    stoplist.append(line)
f.close()

texts = []
for line in file :      
    line=line.strip()
    line=line.lower()
    line=re.sub("<.*?>","",line)
    for c in string.punctuation:
        line=line.replace(c,'')
    texts.append([word for word in line.split() if word not in stoplist]) 

#for i in texts:
#    for j in range (0,len(i)-1):        
#        k=stem(i[j])
#        i[j]=k

dictionary = corpora.Dictionary(texts)
dictionary.save('deerwester.dict') # store the dictionary, for future reference
c=len(dictionary)
#print "\n\n Dictionary to token id\n\n\n"
#print dictionary.token2id
#print c

vecSpace = [dictionary.doc2bow(text) for text in texts]
mm = corpora.MmCorpus.serialize('deerwester.mm', vecSpace) # store to disk, for later use
#print "\n\nVector Space\n\n\n"
#print vecSpace

corpus=corpora.MmCorpus('deerwester.mm')
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
  
#print "\n"

index = similarities.MatrixSimilarity(corpus_tfidf[:-1])
index.num_best = 3
sims = index[corpus_tfidf[-1]]
#print len(sims)
#print sims

ans = []
for i in sims:
	ans.append(i[0])
#print ans

file2 = open('ques.txt')
file3 = open('ans.txt','w')
lines = file2.readlines()
for i in ans:
	text = lines[i]
	print (text[:-1],file = file3)
file.close()
file2.close()
file3.close()

file = open("ans.txt",'r')
text = file.readlines()
file.close()
for line in text:
	line = line[:-1]
	print (soup.find('dt',text = line).find_next_sibling('dd').text)