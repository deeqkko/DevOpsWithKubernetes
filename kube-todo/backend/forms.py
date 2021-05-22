from django.forms import ModelForm
from .models import todo

class TodoForm(ModelForm):
    class Meta:
        model = todo
        fields = ['task']
