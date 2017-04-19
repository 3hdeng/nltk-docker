from nltk.corpus import wordnet as wn

# w is the given word, e.g. 'motorcar'
w='face'

# mm is the polysemy
mm=wn.synsets(w)
x=mm[0]
#for elem in x:
#print(dir(x))
print(x.pos())
print(x.definition())
print(x.lemma_names())

#exit()



def polysemy0(w):
  mm=wn.synsets(w)
  poly=[]
  for x in mm:
     syns=[ y for y in  x.lemma_names() if y!=w ]
     #syns=[ y for y in  x if y.lemma_name()!=w ]
     if len(syns)>0 : poly= poly + [syns]
 
  return poly
#==========
def polysemy(w_lma):
    mm=wn.synsets(w_lma)
    poly=[]
    for x in mm:
        lmas=x.lemma_names()
        lma=None
        c=len(lmas)
        if c==1 :
            lma=lmas[0]
        elif c >=2:            
            #lma= ','.join(lmas)
            i=0
            lma=lmas[i]
            while(lma == w_lma):
                i+=1
                lma=lmas[i]
                
            
        if lma:
            #poly=poly + [(x.pos(), lma, x.definition())]
            poly.append( ( x.pos(), lma, x.definition() ) )
    
    return poly



#=============
wlist=['face'] #['motorcar', 'face', 'draw', 'bat']
for w in wlist:
    print(polysemy(w))

