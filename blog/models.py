from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='static/')
    image2 = models.ImageField(upload_to='static/', blank=True)
    image3 = models.ImageField(upload_to='static/', blank = True)

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
