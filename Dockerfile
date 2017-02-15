# to build 3hdeng/nltk:3.6
FROM python:3.6
MAINTAINER 3hdeng
RUN  pip install -U nltk &&  echo "nltk installed"
#RUN  pip install matplotlib && echo "matplotlib installed"
RUN  apt-get update &&  apt-get install -y  python-matplotlib && echo "matplotlib installed"

RUN  python -m nltk.downloader book && echo "nltk data for book downloaded" 

CMD []
