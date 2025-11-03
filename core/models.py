from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class TestAPI(models.Model):
    endpoint = models.CharField(max_length=200)
    method = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.method} {self.endpoint}"
    
class UserAPI(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name
