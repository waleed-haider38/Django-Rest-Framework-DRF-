from django.contrib import admin
from .models import Test,Person,People, Element
# Register your models here.
admin.site.register(Test)
admin.site.register(Person)
admin.site.register(People)
admin.site.register(Element)