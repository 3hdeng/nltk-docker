#!/bin/python
import nltk
from nltk.corpus import webtext

for fid in webtext.fileids():
  print(fid, webtext.raw(fid)[:65], '...')


# Naval Postgraduate School for research on automatic detection of Internet predators. 
from nltk.corpus import nps_chat
chatroom = nps_chat.posts('10-19-20s_706posts.xml')
print(' '.join(chatroom[123]))

