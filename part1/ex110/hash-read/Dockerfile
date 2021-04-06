FROM python:3.9.2-slim-buster

WORKDIR /usr/src/app

RUN mkdir ./files

COPY ./hash-read.py .

EXPOSE 8083

CMD ["python","-u", "hash-read.py"]