from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=200,null=True)
    email = models.EmailField(unique=True,null=True)

    avatar= models.ImageField(null=True,default='default.png')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Task(models.Model):
    title = models.CharField(max_length=200,null=True)
    description = models.TextField(null=True,blank=True)
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    PRIORITY_CHOICES = [
    ("HIGH","High"),
    ("MEDIUM","Medium"),
    ("LOW","Low")
   ]
    priority = models.CharField(max_length=100,choices = PRIORITY_CHOICES)
    due_date = models.DateField(null=True,blank=True)

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.title

class TaskActivity(models.Model):
    ACTION_CHOICES = [
        ("Created","Created"),
       ( "Updated","Updated"),
       ("Completed","Completed"),
       ("Deleted","Deleted")
    ]

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    action = models.CharField(max_length=20,choices = ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.user.name} {self.action} {self.task.title} on {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
    
