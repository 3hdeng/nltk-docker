#!/bin/python
#The Brown Corpus was the first million-word electronic corpus of English, created in 1961 at Brown University

import nltk
from nltk.corpus import inaugural

def myprint(x, top50=50):
  print(len(x), x[:top50])
  print('\n=======================================\n')


from nltk.corpus import udhr

languages = ['Chickasaw', 'English', 'German_Deutsch',
     'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
cfd = nltk.ConditionalFreqDist(
           (lang, len(word))
           for lang in languages
           for word in udhr.words(lang + '-Latin1'))

cfd.plot(cumulative=True)i

# nltk.ConditionalFreqDist() api ?
