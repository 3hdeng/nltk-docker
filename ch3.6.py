import nltk

raw = """DENNIS: Listen, strange women lying in ponds distributing swords
... is no basis for a system of government.  Supreme executive power derives from
... a mandate from the masses, not from some farcical aquatic ceremony."""
tokens = nltk.word_tokenize(raw)

# NLTK includes several off-the-shelf stemmers
# the Porter stemmer correctly handles the word lying (mapping it to lie), while the Lancaster stemmer does not.

"""
The Porter Stemmer is a good choice if you are indexing some texts and want to support search using alternative forms of words 
"""
porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()
x=porter.stem('lying')
print(x)
x=lancaster.stem('lying')
print(x)

x=[porter.stem(t) for t in tokens]
print(x)
x=[lancaster.stem(t) for t in tokens]
print(x)



#=============
class IndexedText(object):

    def __init__(self, stemmer, text):
        self._text = text
        self._stemmer = stemmer
        self._index = nltk.Index((self._stem(word), i)
                                 for (i, word) in enumerate(text))

    def concordance(self, word, width=40):
        key = self._stem(word)
        wc = int(width/4)                # words of context
        for i in self._index[key]:
            lcontext = ' '.join(self._text[i-wc:i])
            rcontext = ' '.join(self._text[i:i+wc])
            ldisplay = '{:>{width}}'.format(lcontext[-width:], width=width)
            rdisplay = '{:{width}}'.format(rcontext[:width], width=width)
            print(ldisplay, rdisplay)

    def _stem(self, word):
        return self._stemmer.stem(word).lower()



grail = nltk.corpus.webtext.words('grail.txt')
text = IndexedText(porter, grail)
x=text.concordance('lie')
print( type(x) )

#=================
wnl = nltk.WordNetLemmatizer()
print( [wnl.lemmatize(t) for t in tokens] )
