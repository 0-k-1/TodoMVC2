from django.db import models
#from django.contrib.auth.models import User

class Todo(models.Model):
    title = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)

