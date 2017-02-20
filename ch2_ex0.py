#!/bin/python
import nltk
#from nltk.book import FreqDist
from nltk.corpus import gutenberg

emma=nltk.Text(gutenberg.words('austen-emma.txt'))
freqdist=nltk.FreqDist(emma)

# print(freqdist)
# print(freqdist.most_common(50))
sum=0
for w in freqdist:
  #tmp=freqdist.freq(w)
  tmp=freqdist[w]
  sum += tmp

V=len(set(emma))
print('vocab size',V)
avgCount=sum/V
# freqdist.N()
print('avgCount=', avgCount)

for fileid in gutenberg.fileids():
  num_chars = len(gutenberg.raw(fileid))
  num_words = len(gutenberg.words(fileid))
  num_sents = len(gutenberg.sents(fileid))
  num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))

print(round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab), fileid)


