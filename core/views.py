from django.shortcuts import render
from rest_framework.views import APIView #type: ignore
from rest_framework.response import Response #type: ignore
from .models import Person, People, Element
from .serializer import PersonSerializer , PeopleSerializer, ElementSerializer


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


    

def person_list(request):
    persons = Person.objects.all()
    return render(request, 'person_list.html', {'persons': persons})

class PeopleAPI(APIView):
    def get(self, request):
        person = People.objects.all()
        serializer = PeopleSerializer(person, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = PeopleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


def people_list(request):
    people = People.objects.all()
    return render(request, 'people_list.html', {'people': people})
    
class ElementAPI(APIView):
    def get(self , request):
        elements = Element.objects.all()
        serializer = ElementSerializer(elements, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ElementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=201)
        return Response(serializer.errors , status=400)
    