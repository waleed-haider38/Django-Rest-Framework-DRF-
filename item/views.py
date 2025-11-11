from django.shortcuts import render
from rest_framework import generics, mixins
from .models import Item, Animal
from .serializer import ItemSerializer, AnimalSerializer


# Create your views here.
def index(request):
    return render(request, "index.html")


# List all items and create new item
class TestItemView(generics.ListCreateAPIView, mixins.RetrieveModelMixin):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


# Retrieve, update, or delete single item
class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class AnimalView(generics.ListCreateAPIView, mixins.RetrieveModelMixin):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class AnimalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
