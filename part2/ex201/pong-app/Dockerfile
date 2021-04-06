FROM python:3.9.2-slim-buster

WORKDIR /usr/src/app

RUN mkdir ./files

COPY ./pong-app-http.py .

EXPOSE 8084

CMD ["python","-u", "pong-app-http.py"]