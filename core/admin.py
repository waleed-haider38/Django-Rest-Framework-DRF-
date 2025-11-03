from django.contrib import admin
from .models import Test
from .models import Person
# Register your models here.
admin.site.register(Test)
admin.site.register(Person)