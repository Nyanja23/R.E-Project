from django.forms import ModelForm
from .models import User,Task
from django import forms

class UserForm(ModelForm):
    class Meta:
        model  = User
        fields = ['name','email','avatar']

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'due_date', 'completed']
        widgets = {
            'due_date':forms.DateInput(attrs={'type':'date'})
        }