FROM python:3.9.2-slim-buster

WORKDIR /usr/src/app

RUN mkdir ./files

COPY ./pong-app-http.py .

RUN pip3 install --upgrade pip

RUN pip3 install psycopg2-binary

EXPOSE 8084

CMD ["python","-u", "pong-app-http.py"]