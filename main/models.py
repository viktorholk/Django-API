from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=65)
    author = models.CharField(max_length=65)
    release_date = models.DateTimeField()
    pages = models.IntegerField()

    def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=45)

    def __str__(self):
        return self.username