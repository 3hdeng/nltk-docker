import nltk
from nltk.corpus import cmudict
entries=cmudict.entries()


# finds all words whose pronunciation len is 3 and starts with P and ends with T
for word, pron in entries:
    if len(pron) == 3:
        ph1, ph2, ph3 = pron
        if ph1 == 'P' and ph3 == 'T':
            print(word, ph2, end='\n')


# finds all words whose pronunciation ends with a syllable sounding like nicks. You could use this method to find rhyming words.
syllable = ['N', 'IH0', 'K', 'S']
x=[w for w,p in entries if p[-4:]== syllable]
print(x)

y=[ p for w, p in entries if w=="atlantic's" ]
print(y)


# word endswith n and pronunciation endswith M
x=[w for w, pron in entries if pron[-1] == 'M' and w[-1] == 'n']
print(x)
#['autumn', 'column', 'condemn', 'damn', 'goddamn', 'hymn', 'solemn']


# pron. startswith N and word not startswith n; take the first 2 letters from word
x= sorted(set(w[:2] for w, pron in entries if pron[0] == 'N' and w[0] != 'n'))
print(x)

x= [w for w, pron in entries if pron[0] == 'N' and w[0] != 'n' ]
fdist=nltk.FreqDist(x)
print(fdist)
for w in fdist:
  print(w, fdist[w])


def w2p(word):
  y=[ p for w, p in entries if w==word ]
  print(y)

w2p('mnemonic')

w2pdict=cmudict.dict()
print(w2pdict['mnemonic'])
print(w2pdict['test'])
print("w2pdict[] return list of list, [[], [], ... ]")
text = ['natural', 'language', 'processing']
x= [ph for w in text for ph in w2pdict[w][0]]
print(x)

#=========
# The phones contain digits to represent 
# primary stress (1), secondary stress (2) and no stress (0).
def stress(pron):
  return [char for phone in pron for char in phone if char.isdigit()]

x=[ w for w, pron in entries if stress(pron)==['0','1'] ]
print(x[0:10])






