#!/bin/python
#The Brown Corpus was the first million-word electronic corpus of English, created in 1961 at Brown University

import nltk
from nltk.corpus import reuters as reuter

print(reuter.categories())
print('\n=======================================\n')

x=reuter.words(categories='barley')
len1=len(x)
print(len1, x[:65])
print('\n=======================================\n')

x=reuter.words(categories=['barley','corn'])
len1=len(x)
print(len1, x[:65])
#xxx print(brown.words(categories='news').words(fileids='cg22'))
print('\n=======================================\n')

i=0
for fid in reuter.fileids():
  if i < 50 :
    print(fid, reuter.raw(fid)[:65], '...')
    i += 1
  else :
    break  

"""
x= brown.sents(categories=['news', 'editorial', 'reviews'])
for s in x:
 print(' '.join(s))
"""
print('\n=======================================\n')

def myprint(x, top50=50):
  print(len(x), x[:top50])
  print('\n=======================================\n')

x=reuter.words(categories=['barley','corn'])
myprint(x,10)
myprint(x)

