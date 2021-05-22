from django.forms import ModelForm, widgets
from .models import todo

class TodoForm(ModelForm):
    class Meta:
        model = todo
        fields = '__all__'
