#!/bin/python
#The Brown Corpus was the first million-word electronic corpus of English, created in 1961 at Brown University

import nltk
from nltk.corpus import brown

print(brown.categories())
#print(brown.words(categories='news'))
#xxx print(brown.words(categories='news').words(fileids='cg22'))

for fid in brown.fileids():
  print(fid, brown.raw(fid)[:65], '...')

"""
x= brown.sents(categories=['news', 'editorial', 'reviews'])
for s in x:
 print(' '.join(s))
"""

news_text = brown.words(categories='news')
fdist = nltk.FreqDist(w.lower() for w in news_text )
modals = ['can', 'could', 'may', 'might', 'must', 'will']
for m in modals:
   print(m + ':', fdist[m], end=' ')

print('\n=======================================\n')

fdist = nltk.FreqDist(w.lower() for w in news_text if w.startswith('wh'))
#print(fdist)
print(type(fdist))

for w in sorted(fdist):
   print(w, fdist[w])

print('\n============not work as expected ===========================\n')
for w in sorted(fdist,key=lambda t: t[1]):
   print(w, fdist[w])

print('\n============ use most_common instead ===========================\n')
print(fdist.most_common(20))


