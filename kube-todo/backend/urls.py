from django.urls import path
from . import views
from backend.views import TodoListView, HealthCheckView

urlpatterns = [
    path('', TodoListView.as_view(), name="todolist"),
    path('healthz', HealthCheckView.as_view()),
    #path('<int:task_id>', updateDone, name="updateDone")
]