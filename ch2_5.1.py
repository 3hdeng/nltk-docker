from nltk.corpus import wordnet as wn

x=wn.synsets('motorcar')
print(x)
# [Synset('car.n.01')]
# y=wn.synset(x[0].lemma_name)
y=x[0]
print(type(y))
print(y.lemma_names())
print(y.definition())
print(y.examples())
print(y.lemmas())

for lemma in y.lemmas():
   print(lemma.name())
   print(lemma.synset())


def print_synsets(s) :
 x=wn.synsets(s)
 print(x)
 for synset in x:
  print(synset.lemma_names())


x=wn.lemmas('car')
print(x)
   

print_synsets('car')
print_synsets('dish')


