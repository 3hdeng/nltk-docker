#!/bin/bash
ver=3.6
if [[ "$#" == "1" ]]; then
  ver=$1
fi
echo $ver
docker build -f Dockerfile$ver  -t 3hdeng/nltk:$ver . 
