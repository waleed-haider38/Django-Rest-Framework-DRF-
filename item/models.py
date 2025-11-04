from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
