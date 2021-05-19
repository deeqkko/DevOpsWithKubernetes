from django.urls import path
from . import views
from backend.views import TodoListView, HealthCheckView

urlpatterns = [
    path('', TodoListView.as_view()),
    path('healthz', HealthCheckView.as_view())
]