import nltk
gmr= nltk.CFG.fromstring("""
  S -> NP VP
  VP -> V NP | V NP PP
  PP -> P NP
  V -> "saw" | "ate" | "walked"
  NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
  Det -> "a" | "an" | "the" | "my"
  N -> "man" | "dog" | "cat" | "telescope" | "park"
  P -> "in" | "on" | "by" | "with"
  """)
 	
sent = "Mary saw Bob".split()
rd_parser = nltk.RecursiveDescentParser(gmr)
for tree in rd_parser.parse(sent):
     print(tree)

gmr1 = nltk.data.load('file:gmr1.cfg')
rd_parser = nltk.RecursiveDescentParser(gmr1)
for tree in rd_parser.parse(sent):
     print(tree)

for p in gmr1.productions(): print(p)

"""
Make sure that you put a .cfg suffix on the filename, and that there are no spaces in the string 'file:mygrammar.cfg'. If the command print(tree) produces no output, this is probably because your sentence sent is not admitted by your grammar.

call the parser with tracing set to be on: rd_parser =
nltk.RecursiveDescentParser(grammar1, trace=2). 

You can also check what productions are currently in the grammar with the command 
for p in grammar1.productions(): print(p)

"""

#==================
"""
When you write CFGs for parsing in NLTK, you cannot combine grammatical categories with lexical items on the righthand side of the same production. 
Thus, a production such as PP -> 'of' NP is disallowed. 

In addition, you are not permitted to place multi-word lexical items on the righthand side of a production. 
So rather than writing NP -> 'New York', you have to resort to something like 
NP -> 'New_York' instead. ???
"""

#=================
#A grammar is said to be recursive if a category occurring on the left hand side of a production also appears on the righthand side of a production, 
# Nom -> Adj Nom (where Nom is the category of nominals) involves direct recursion on the category Nom, 
# whereas indirect recursion on S arises from the combination of two productions, namely S -> NP VP and VP -> V S.

# the RecursiveDescentParser is unable to handle left-recursive productions of the form X -> X Y


gmr2 = nltk.CFG.fromstring("""
  S  -> NP VP
  NP -> Det Nom | PropN
  Nom -> Adj Nom | N
  VP -> V Adj | V NP | V S | V NP PP
  PP -> P NP
  PropN -> 'Buster' | 'Chatterer' | 'Joe'
  Det -> 'the' | 'a'
  N -> 'bear' | 'squirrel' | 'tree' | 'fish' | 'log'
  Adj  -> 'angry' | 'frightened' |  'little' | 'tall'
  V ->  'chased'  | 'saw' | 'said' | 'thought' | 'was' | 'put'
  P -> 'on'
""")



sent = "the angry bear chased the frightened little squirrel".split()
rd_parser = nltk.RecursiveDescentParser(gmr2)
for tree in rd_parser.parse(sent):
     print(tree)

