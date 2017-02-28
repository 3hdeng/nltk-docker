#Let's look for all sequences of two or more vowels in some text, and determine their relative frequency:
import nltk
import re
from nltk.corpus import treebank as tb
 	
wsj = sorted( set(tb.words()) )
fd = nltk.FreqDist(vs for word in wsj
            for vs in re.findall(r'[aeiou]{2,}', word))
print( fd.most_common(12) )
# [('io', 549), ('ea', 476), ('ie', 331), ('ou', 329), ('ai', 261), ('ia', 253),
# ('ee', 217), ('oo', 174), ('ua', 109), ('au', 106), ('ue', 105), ('ui', 95)]

# to convert the string '2009-12-31' to a list of integers [2009, 12, 31]:

x=[int(n) for n in re.findall(r'[0-9]+', '2009-12-31')]
print(x)

#=====================
# it is still easy to read when word-internal vowels are left out. For example, declaration becomes dclrtn, and inalienable becomes inlnble
# matches initial vowel sequences, final vowel sequences, and all consonants; everything else is ignored
regexp = r'^[AEIOUaeiou]+|[AEIOUaeiou]+$|[^AEIOUaeiou]'
def compress(word):
    pieces = re.findall(regexp, word)
    return ''.join(pieces)

print( compress('declaration') )


