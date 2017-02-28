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

#===========================================
#extract all consonant-vowel sequences from the words of Rotokas, such as ka and si. Since each of these is a pair, it can be used to initialize a conditional frequency distribution. We then tabulate the frequency of each pair:

 	
rotokas_words = nltk.corpus.toolbox.words('rotokas.dic')
cvs = [cv for w in rotokas_words for cv in re.findall(r'[ptksvr][aeiou]', w)]
cfd = nltk.ConditionalFreqDist(cvs)
cfd.tabulate()
#    a    e    i    o    u
#k  418  148   94  420  173
#p   83   31  105   34   51
#r  187   63   84   89   79
#s    0    0  100    2    1
#t   47    8    0  148   37
#v   93   27  105   48   49

# nltk.Index
cv_word_pairs = [(cv, w) for w in rotokas_words
            for cv in re.findall(r'[ptksvr][aeiou]', w)]
cv_index = nltk.Index(cv_word_pairs)
print( cv_index['su'] )
# ['kasuari']
print( cv_index['po'] )


#====== word stem, lemma, root
def stem(word):
   for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']:
       if word.endswith(suffix):
             return word[:-len(suffix)]
   return word

print(stem('shits'))
print(stem('idiots'))


#====================
def stem(word):
 regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'
 stem, suffix = re.findall(regexp, word)[0]
 return stem

print(stem('processing'))
print(stem('processes'))
print(stem('dog'))

#================
raw = """DENNIS: Listen, strange women lying in ponds distributing swords
... is no basis for a system of government.  Supreme executive power derives from
... a mandate from the masses, not from some farcical aquatic ceremony."""
tokens = nltk.word_tokenize(raw)
print([stem(t) for t in tokens])

