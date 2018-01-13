FROM tiangolo/uwsgi-nginx-flask:python3.6
MAINTAINER Vikash Kothary <kothary.vikash@gmail.com>
COPY ./app /app
WORKDIR /app
ENTRYPOINT ["python"]
CMD ["main.py"]