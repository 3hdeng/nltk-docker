# names= nltk.corpus.names
# NameError: name 'nltk' is not defined
import nltk
from nltk.corpus import names

print(names.fileids())


x= [w for w in names.words('female.txt') if w.startswith('el')] 
print(x)

x= [w for w in names.words('female.txt') if w.startswith('Elf')]
#['Elfie', 'Elfreda', 'Elfrida', 'Elfrieda']
print(x)

x= [w for w in names.words('male.txt') if w.startswith('Elf')]
#[ ]
print(x)

#=======
puzzle_letters = nltk.FreqDist('egivrvonl')
obligatory = 'r'
wordlist = nltk.corpus.words.words()
x=sorted(set([w for w in wordlist if len(w) ==4
         and obligatory in w
         and nltk.FreqDist(w) <= puzzle_letters]))
print(type(x))
print(x)

