FROM python:3.7-alpine
MAINTAINER Enno

ENV PYTHONUNBUFERED 1

# current dir            the docker image
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt


# empty folder on docker image 
RUN mkdir /app
#  switch to default dir
WORKDIR /app
COPY ./app /app


RUN adduser -D user 
USER user