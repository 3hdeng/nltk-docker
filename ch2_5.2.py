from nltk.corpus import wordnet as wn
motorcar = wn.synset('car.n.01')
types_of_motorcar = motorcar.hyponyms()
# print(types_of_motorcar)
for synset in types_of_motorcar:
  for lemma in synset.lemmas():
    print(lemma.name())



#===========
x= motorcar.hypernyms()
# [Synset('motor_vehicle.n.01')]
print(x)

x= motorcar.root_hypernyms()
print(x)


print("#=====================")
paths = motorcar.hypernym_paths()
print(paths)


print("#=====================")
x= [synset.name() for synset in paths[0]]
print(x)
