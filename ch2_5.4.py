from nltk.corpus import wordnet as wn
right = wn.synset('right_whale.n.01')
orca = wn.synset('orca.n.01')
minke = wn.synset('minke_whale.n.01')
tortoise = wn.synset('tortoise.n.01')
novel = wn.synset('novel.n.01')
print( right.lowest_common_hypernyms(minke) )
#[Synset('baleen_whale.n.01')]
print( right.lowest_common_hypernyms(orca))
#[Synset('whale.n.02')]Ggg


print( wn.synset('baleen_whale.n.01').min_depth() )
# 14
print( wn.synset('whale.n.02').min_depth())
#13
print( wn.synset('vertebrate.n.01').min_depth())
#8
print( wn.synset('entity.n.01').min_depth())
#0

for x in [minke, orca, tortoise, novel] :
 print( right.path_similarity(x) )

