
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from .forms import TodoForm
from backend.models import todo


class TodoListView(ListView):
    model = todo
    template_name = 'todo_list.html'
    todoform = TodoForm()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] =  self.todoform
        return context
    
    def post(self, request, **kwargs):
        new_task = TodoForm(request.POST)
        if new_task.is_valid():
            new_task.save()
            return redirect('/')
        else:
            return HttpResponse('Failed...')
    

