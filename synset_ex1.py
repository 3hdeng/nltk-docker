from nltk.corpus import wordnet as wn

# w is the given word, e.g. 'motorcar'
w='motorcar'

# mm is the polysemy
mm=wn.synsets(w)
for x in mm:
    print(x.lemma_names())

def polysemy(w):
  mm=wn.synsets(w)
  poly=[]
  for x in mm:
     syns=[ y for y in  x.lemma_names() if y!=w ]
     if len(syns)>0 : poly= poly + [syns]
 
  return poly

wlist=['motorcar', 'face', 'draw', 'bat']
for w in wlist:
    print(polysemy(w))

