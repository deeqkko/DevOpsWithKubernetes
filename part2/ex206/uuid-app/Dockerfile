FROM python:3.9.2-slim-buster

WORKDIR /usr/src/app

RUN mkdir ./files

COPY ./uuid-app-http.py .

RUN pip install requests

EXPOSE 8083

CMD ["python","-u", "uuid-app-http.py"]