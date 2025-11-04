from django.shortcuts import render
from rest_framework import generics , mixins
from .models import Item
from .serializer import ItemSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html')


# List all items and create new item
class TestItemView(generics.ListCreateAPIView , mixins.RetrieveModelMixin):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


# Retrieve, update, or delete single item
class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer