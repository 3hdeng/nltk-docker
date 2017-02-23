#!/bin/python
#The Brown Corpus was the first million-word electronic corpus of English, created in 1961 at Brown University

import nltk
from nltk.corpus import inaugural

def myprint(x, top50=50):
  print(len(x), x[:top50])
  print('\n=======================================\n')

x=inaugural.fileids()

myprint(x,10)
myprint(x)


cfd = nltk.ConditionalFreqDist(
   (target, fileid[:4])
   for target in ['america', 'citizen']     
   for fileid in inaugural.fileids()
   for w in inaugural.words(fileid)
   if w.lower().startswith(target)
)

cfd.plot()

