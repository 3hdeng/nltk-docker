#!/bin/bash
docker run -it --rm  --name mynltk \
  -v $(pwd):/mnt/work  -w /mnt/work \
  3hdeng/nltk:3.6 \
  /bin/bash


#    -v $gitRepo:/opt/$USER/repos \
#    -e "OPTION_NAME=OPTION_VALUE" \
