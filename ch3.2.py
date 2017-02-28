import nltk
from nltk.corpus import gutenberg
raw = gutenberg.raw('melville-moby_dick.txt')
fdist = nltk.FreqDist(ch.lower() for ch in raw if ch.isalpha())
print( fdist.most_common(5) )
#[('e', 117092), ('t', 87996), ('a', 77916), ('o', 69326), ('n', 65617)]
x=[char for (char, count) in fdist.most_common()]
print(x) #26 english letters sorted in order of freq
