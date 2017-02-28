# Text number 2554 is an English translation of Crime and Punishment, and we can access it as follows.

 	
#from urllib import request
from urllib.request import Request, urlopen
#url = "http://www.gutenberg.org/files/2554/2554.txt"
"""
url="http://www.gutenberg.org/files/2554/2554-0.txt"
user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'
req=Request(url, headers={'User-Agent': user_agent})
response = urlopen(req)
raw = response.read().decode('utf8')
"""

#=========================
with open('gutenburg2554.txt', 'r') as f:
    read_data = f.read()

#f.closed
print(type(read_data))

raw= read_data # .deccode('utf8')
print(type(raw))
# <class 'str'>
print(len(raw))
#1176893
print(raw[:75])
#'The Project Gutenberg EBook of Crime and Punishment, by Fyodor Dostoevsky\r\n'

u=raw.encode('utf8')
print(type(u))
print(u[:75])


import nltk
tokens = nltk.word_tokenize(raw)
print( type(tokens) )
#<class 'list'>
print( len(tokens) )
# 254354
print( tokens[:10] )
# ['The', 'Project', 'Gutenberg', 'EBook', 'of', 'Crime', 'and', 'Punishment', ',', 'by']

text = nltk.Text(tokens)
print( type(text) )
#<class 'nltk.text.Text'>


#====================
pos1= raw.find("PART I")
# 5338
pos2= raw.rfind("End of Project Gutenberg's Crime") 
#1157743
raw = raw[pos1:pos2] 
#print( raw )
print(pos1, pos2)
print( raw.find("PART I"))

#The find() and rfind() ("reverse find") methods help us get the right index values to use for slicing the string

#===============
def myprint_type(x):
 print("type(x)= " , type(x))

url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
data=urlopen(url).read()
print("type(data)= " , type(data))
html = data.decode('utf8')
print("type(html)= " , type(html))
print(html[:60])
# '<!doctype html public "-//W3C//DTD HTML 4.0 Transitional//EN'


#============
# To get text out of HTML we will use a Python library called BeautifulSoup, available from http://www.crummy.com/software/BeautifulSoup/:

# import bs4 	
from bs4 import BeautifulSoup
raw = BeautifulSoup(html,"html.parser").get_text()
tokens = nltk.word_tokenize(raw)
print(tokens[:10])
# ['BBC', 'NEWS', '|', 'Health', '|', 'Blondes', "'to", 'die', 'out', ...]

#========
tokens = tokens[110:390]
text = nltk.Text(tokens)
print( text.concordance('gene') )



#==============
import feedparser
llog = feedparser.parse("http://languagelog.ldc.upenn.edu/nll/?feed=atom")
print( llog['feed']['title'] )
#'Language Log'
print( len(llog.entries))
# 15
post = llog.entries[2]
print(post.title)
#"He's My BF"
content = post.content[0].value
print( content[:70] )
# '<p>Today I was chatting with three of our visiting graduate students f'
raw = BeautifulSoup(content, "html.parser").get_text()
print(nltk.word_tokenize(raw) )


#==================
s=input("Pls input sth\n")
tokens=nltk.word_tokenize(s)
print(s)
print(tokens)
