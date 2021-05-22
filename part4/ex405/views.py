import time
import os
import logging
import json
import logging_loki
from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from django.views import View
from django.views.generic.list import ListView
from .forms import TodoForm
from backend.models import todo, Potd
from backend.potd import load_image
from backend.dummyconnector import get_dummy_tasks
from django.views.decorators.csrf import csrf_exempt

handler = logging_loki.LokiHandler(
    url=os.getenv('LOG_URL'), 
    tags={"application": "kube-todo"},
    version="1"
)


logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)
logger.addHandler(handler)


class TodoListView(ListView):
    model = todo
    template_name = 'todo_list.html'
    todoform = TodoForm()
    
    def get_context_data(self, **kwargs):
        if not Potd.objects.exists():
            load_image()
            Potd(1,'potd/potd.jpg').save()
            logger.info('No image reference found. Creating ["potd/potd.jpg]')
        if time.time() - os.path.getmtime('backend/potd/potd.jpg') > 86400:
            load_image()
        context = super().get_context_data(**kwargs)
        context["form"] = self.todoform
        context["update"] = self.updateform
        context["potd"] = Potd.objects.get()
        context["dummy_tasks"] = get_dummy_tasks()
        uri = self.request.build_absolute_uri()
        method = self.request.method
        logger.info('%s %s', method, uri)
        return context

    def post(self, request, **kwargs):
        new_task = TodoForm(request.POST)
        if new_task.is_valid():
            new_task.save()
            req_data = self.request.POST['task']
            logger.info('Task ["%s"] inserted.', req_data)
            return redirect('/')
        else:
            logger.error(new_task.errors.as_data())
            return HttpResponseBadRequest(new_task.errors)

    def put(self, request):
        if request.method == "PUT":
            task_id = json.loads(request.body)["btn_id"]
            task = get_object_or_404(todo, pk=task_id)
            task.done = not task.done
            task.save()
            return HttpResponse(status=200)


class HealthCheckView(View):
    def get(self, request, *args, **kwargs):
        try:
            with connection.cursor() as cursor:
                cursor.execute("select 1")
                one = cursor.fetchone()[0]
        except:
            one = 0
        if one != 1:
            logger.error('Server unhealthy. DB connection failed.')
            return HttpResponse(status=500)
        else:
            logger.info('Server healthy.')
            return HttpResponse(status=200)
            

