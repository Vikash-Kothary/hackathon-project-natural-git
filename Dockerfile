# Internet doesn't work so I'm storing all the requirements in a docker container

FROM python:3.4

RUN apt-get -qq update && apt-get install -y portaudio19-dev python-all-dev

COPY ./app/requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install -r requirements.txt
