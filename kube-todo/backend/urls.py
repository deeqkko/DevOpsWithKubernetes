from django.urls import path
from . import views
from backend.views import TodoListView

urlpatterns = [
    path('', TodoListView.as_view())
]