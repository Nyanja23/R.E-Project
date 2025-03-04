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
        fields = '__all__'
        widgets = {
            'due_date':forms.DateInput(attrs={'type':'date'})
        }