from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField, TextField

class login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    

    def __str__(self):
        return self.username

class Tag(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class Snippet(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

