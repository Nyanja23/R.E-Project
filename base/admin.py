from django.contrib import admin
from .models import User,Task,TaskActivity

admin.site.register(User)
admin.site.register(Task)
admin.site.register(TaskActivity)