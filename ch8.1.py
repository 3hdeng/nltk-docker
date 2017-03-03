import nltk
gmr = nltk.CFG.fromstring("""
S -> NP VP
PP -> P NP
AP -> ADJ NP
ADJ -> 'Fighting'|'dangerous'
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP PP
Det -> 'an' | 'my'
N -> 'elephant' | 'pajamas' | 'animals'
V -> 'shot' | 'could' | 'be'
P -> 'in'
""")

sent = ['I', 'shot', 'an', 'elephant', 'in', 'my', 'pajamas']
s= "Fighting animals could be dangerous"
#[Q] how to handle 'could be' ?
sent=s.split()
print(sent)

parser = nltk.ChartParser(gmr)
for tree in parser.parse(sent):
   print(tree)


