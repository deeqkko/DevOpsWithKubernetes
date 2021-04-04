from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Todo-app</h1><p>DevOps with Kubernetes</p>')
