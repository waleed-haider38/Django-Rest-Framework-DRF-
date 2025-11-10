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

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class People(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class Element(models.Model):
    element_name = models.CharField(max_length=100)
    element_formula = models.CharField(max_length=1000)
    element_description = models.TextField()

    def __str__(self):
        return self.element_name

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    subject_marks = models.IntegerField()
    subject_detail = models.TextField()

    def __str__(self):
        return self.subject_name
    
class School(models.Model):
    school_name = models.CharField(max_length=1000)
    school_branch = models.CharField(max_length=1200)
    school_detail = models.TextField()

    def __str__(self):
        return self.school_name
    