# names= nltk.corpus.names
# NameError: name 'nltk' is not defined
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
