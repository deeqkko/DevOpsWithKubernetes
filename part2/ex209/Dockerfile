FROM python:3.9.2-slim-buster

WORKDIR /usr/src/app

RUN pip3 install --upgrade pip

RUN pip3 install requests

COPY ./insert_task.py .

CMD ["python","-u", "insert_task.py"]