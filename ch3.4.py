import re
#import nltk
from  nltk.corpus import words as wc
wordlist = [w for w in wc.words('en') if w.islower()]
print(len(wordlist))
print(len(set(wordlist)))

#===============
from nltk.corpus import treebank as tb
wsj = sorted(set(tb.words()))
print( [w for w in wsj if re.search('^[0-9]+\.[0-9]+$', w)] )
# ['0.0085', '0.05', '0.1', '0.16', '0.2', '0.25', '0.28', '0.3', '0.4', '0.5',
# '0.50', '0.54', '0.56', '0.60', '0.7', '0.82', '0.84', '0.9', '0.95', '0.99',
# '1.01', '1.1', '1.125', '1.14', '1.1650', '1.17', '1.18', '1.19', '1.2', ...]

print( [w for w in wsj if re.search('^[A-Z]+\$$', w)] )
#['C$', 'US$']

print( [w for w in wsj if re.search('^[0-9]{4}$', w)] )
#['1614', '1637', '1787', '1901', '1903', '1917', '1925', '1929', '1933', ...]

print( [w for w in wsj if re.search('^[0-9]+-[a-z]{3,5}$', w)] )
#['10-day', '10-lap', '10-year', '100-share', '12-point', '12-year', ...]

print( [w for w in wsj if re.search('^[a-z]{5,}-[a-z]{2,3}-[a-z]{,6}$', w)] )
#['black-and-white', 'bread-and-butter', 'father-in-law', 'machine-gun-toting',
#'savings-and-loan']

x=[w for w in wsj if re.search('(ed|ing)$', w)]
print(x[:15])

#['62%-owned', 'Absorbed', 'According', 'Adopting', 'Advanced', 'Advancing', ...]
