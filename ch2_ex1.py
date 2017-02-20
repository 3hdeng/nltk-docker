#!/bin/python
import nltk
from nltk.corpus import gutenberg

num_chars=len(gutenberg.raw('shakespeare-macbeth.txt'))
print('total number of chars/bytes? in macbeth: ', num_chars)

num_words=len(gutenberg.words('shakespeare-macbeth.txt'))
print('total number of words in macbeth: ', num_words)

num_sents=len(gutenberg.sents('shakespeare-macbeth.txt'))
print('total number of sents in macbeth: ', num_sents)

mac_sents=gutenberg.sents('shakespeare-macbeth.txt')
print('sents', mac_sents)
print('sents[1116]',mac_sents[1116])
len_max=max(len(s) for s in mac_sents)
x=[s for s in mac_sents if len(s) == len_max ]
for s in x: 
   print(' '.join(s))

