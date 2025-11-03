from django.shortcuts import render
from rest_framework.views import APIView #type: ignore
from rest_framework.response import Response #type: ignore
from .models import Person
from .serializer import PersonSerializer


# Create your views here.
def home(request):
    return render(request, 'home.html')

class TestAPI(APIView):
    def get(self, request):
        data = {
            'message': 'Assalam-o-Alaikum! Kia hal ha? Mera name Muhammad Waleed Haider ha'
        }
        return Response(data)

    def post(self, request):
        data = {
            'message': 'Hello, this is a POST request!'
        }
        return Response(data)
    
class UserAPI(APIView):
    def get(self, request):
        data = {
            'name': 'Muhammad Waleed Haider',
            'email': 'waleed@haidergmail.com',
        }
        return Response(data)
    def post(self, request):
        data = {
            'message': 'User data received successfully!'
        }
        return Response(data)

class PersonAPI(APIView):
    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    
    
