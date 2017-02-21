#!/bin/bash
docker run -it --rm  --name mynltk \
  -v $(pwd):/mnt/work  -w /mnt/work \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  3hdeng/nltk:3.6 \
  /bin/bash


#    -v $gitRepo:/opt/$USER/repos \
#    -e "OPTION_NAME=OPTION_VALUE" \
