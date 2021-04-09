#!/bin/sh

python manage.py migrate
gunicorn kube_todo.wsgi:application --bind 0.0.0.0:$PORT 