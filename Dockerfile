# to build 3hdeng/nltk:3.6
FROM python:3.6
MAINTAINER 3hdeng
RUN  pip install -U nltk &&  echo "nltk installed"
#RUN  python -m nltk.downloader punkt && echo "nltk data for punkt downloaded" 

CMD []
