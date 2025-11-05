from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=150)
    description = models.TextField()
    power = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class Count(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    age = models.IntegerField(max_length=100)

    def __str__(self):
        return self.name