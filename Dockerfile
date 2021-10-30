FROM python:3.7-alpine
MAINTAINER Enno

ENV PYTHONUNBUFERED 1

# current dir            the docker image
COPY ./requirements.txt /requirements.txt
# apk is the package manager that comes with alpine
RUN apk add --update --no-cache postgresql-client
# virtual set up alias to remove deps later 
# these are dep of postgres client
# getting rid of this after postgres client is removed 
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc musl-dev postgresql-dev
    # gcc, libc-dev linux-headers postgresql-dev
    # gcc python-dev musl-dev postgresql-dev
# lots of searching for this list. No easy dep list for alpine image

RUN pip install -r /requirements.txt
# RUN apk del .tmp-build-deps

# empty folder on docker image 
RUN mkdir /app
#  switch to default dir
WORKDIR /app
# should error when not exist /app
COPY ./app /app

# create user
RUN adduser -D someuser 
# use user
USER someuser