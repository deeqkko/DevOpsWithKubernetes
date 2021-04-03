FROM python:3.9.2-slim-buster

WORKDIR /usr/src/app

RUN mkdir ./files

COPY ./hash-gen.py .

CMD ["python","-u", "hash-gen.py"]