from nltk.corpus import wordnet as wn

print( wn.synset('tree.n.01').part_meronyms() )
print( wn.synset('tree.n.01').substance_meronyms() )
print(wn.synset('tree.n.01').member_holonyms() )

print("#=========================")
for synset in wn.synsets('mint', wn.NOUN):
     print(synset.name() + ':', synset.definition())


print("#=========================")
for synset in wn.synsets('mint'):
     print(synset.name() + ':', synset.definition())

print("#=========================")
print( wn.synset('walk.v.01').entailments() )
# [Synset('step.v.01')]
print(wn.synset('eat.v.01').entailments())
# [Synset('chew.v.01'), Synset('swallow.v.01')]
print(wn.synset('tease.v.03').entailments())
# [Synset('arouse.v.07'), Synset('disappoint.v.01')]

print("#=========================")
print( wn.lemma('supply.n.02.supply').antonyms() )
# [Lemma('demand.n.02.demand')]
print( wn.lemma('rush.v.01.rush').antonyms() )
# [Lemma('linger.v.04.linger')]
print( wn.lemma('horizontal.a.01.horizontal').antonyms())
# [Lemma('inclined.a.02.inclined'), Lemma('vertical.a.01.vertical')]
print( wn.lemma('staccato.r.01.staccato').antonyms() )
#[Lemma('legato.r.01.legato')]


print("#=========================")
x= wn.synset('supply.n.02')

#xxx lma_names=[lma.name for lma in x.lemmas()]
lma_names=[lma.name() for lma in x.lemmas()]
for name in lma_names:   
   print(name)
   print(wn.lemma('supply.n.02.' + name).antonyms())

#xxx print( wn.lemma('supply.n.02').antonyms() )
#xxx print( wn.lemma('rush.v.01').antonyms() )

