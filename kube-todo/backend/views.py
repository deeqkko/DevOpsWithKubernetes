#Project v0.3 (ex1.05) respond to GET request

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Todo-app</h1><p>DevOps with Kubernetes</p>')
