#This file is encoded as Latin-2, also known as ISO-8859-2. The function nltk.data.find() locates the file for us.
import nltk

#find the full path to the file
path = nltk.data.find('corpora/unicode_samples/polish-lat2.txt')
f = open(path, encoding='latin2')
for line in f:
     line = line.strip()
     print('latin-2 string: ', line)
     print('unicode-escape: ', line.encode('unicode-escape'))



#=============
nacute='\u0144'
print('nacute: ', nacute)
print('encode in utf8: ', nacute.encode('utf8') )
print('encode in latin2: ',  nacute.encode('latin2') )
# b'\xc5\x84'


#================
import unicodedata
lines = open(path, encoding='latin2').readlines()
line = lines[2]
print(line.encode('unicode_escape'))
for c in line:
    if ord(c) > 127:
      print('#=====================================')
      print('{}, U+{:04x},  {}'.format(c, ord(c), unicodedata.name(c)))
      print('{}, U+{:04x},  {}'.format(c.encode('latin2'), ord(c), unicodedata.name(c)))
      print('{}, U+{:04x},  {}'.format(c.encode('utf8'), ord(c), unicodedata.name(c)))

print( line.find('zosta\u0142y') ) #54
line = line.lower()
print( line )
# 'niemców pod koniec ii wojny światowej na dolny śląsk, zostały\n'
print(  line.encode('unicode_escape') )
# b'niemc\\xf3w pod koniec ii wojny \\u015bwiatowej na dolny \\u015bl\\u0105sk, zosta\\u0142y\\n'

# [Q] '\\uXXXX' or  '\uXXXX'
#=================
import re
m = re.search('\u015b\w*', line)
x=m.group()
print(x)
print(x.encode('utf32'))
print(x.encode('unicode_escape'))
# '\u015bwiatowe


