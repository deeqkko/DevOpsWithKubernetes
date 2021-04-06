FROM python:3.9.2-slim-buster

WORKDIR /usr/src/app

COPY ./print_uuid-http.py .

EXPOSE 8083

CMD ["python","-u", "print_uuid-http.py"]