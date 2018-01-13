# Internet doesn't work so I'm storing all the requirements in a docker container

FROM python:3.4

COPY ./app/requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install -r requirements.txt
