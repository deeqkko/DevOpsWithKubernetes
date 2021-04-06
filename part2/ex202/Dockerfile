FROM python:3.9.2-slim-buster

WORKDIR /usr/src/app

RUN mkdir ./files

COPY ./dummy-db.py .

EXPOSE 8085

CMD ["python","-u", "dummy-db.py"]