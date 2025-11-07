from django.shortcuts import render
from rest_framework.views import APIView #type: ignore
from rest_framework.response import Response #type: ignore
from .models import Person, People, Element, Subject
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializer import PersonSerializer , PeopleSerializer, ElementSerializer,SubjectSerializer


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
    
#Here I write the code related to element where I can do get , post , put & patch(update) and delete request
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
    
class ElementDetailAPIView(APIView):
    def get(self, request, pk):
        element = get_object_or_404(Element , pk=pk)
        serializer = ElementSerializer(element)
        return Response(serializer.data)
    def put(self , request, pk):
        element = get_object_or_404(Element , pk=pk)
        serializer = ElementSerializer(element , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Element Updated Successfully','data':serializer.data},status = status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, pk):
        element = get_object_or_404(Element, pk=pk)
        serializer = ElementSerializer(element , data=request.data , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Element Partially Updated!','data':serializer.data},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self , request , pk):
        element = get_object_or_404(Element, pk=pk)
        element.delete()
        return Response({'message':'Element Deleted Successfully'},status=status.HTTP_204_NO_CONTENT)                          

#Subject API here I have write the code where I can get , post , put , patch (update) and delete my subject data
class SubjectAPI(APIView):
    def get(self , request):
        subject = Subject.objects.all()
        serializer = SubjectSerializer(subject , many=True)
        return Response(serializer.data)
    def post(self , request):
        serializer = SubjectSerializer(data=request.data , many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=201)
        return Response(serializer.errors , status=400)
    
class SubjectDetailAPI(APIView):
    def get(self , request, pk):
        subject = get_object_or_404(Subject, pk=pk)
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)
    def put(self , request, pk):
        subject = get_object_or_404(Subject , pk=pk)
        serializer = SubjectSerializer(subject ,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Subject Updated Successfully!','data':serializer.data}, status=status.HTTP_200_OK)
        return Response({'message':'Bad Request!'}, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request,pk):
        subject = get_object_or_404(Subject, pk=pk)
        serializer = SubjectSerializer(subject, data=request.data , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Subject Partial Updated Successfully!','data':serializer.data},status=status.HTTP_200_OK)
        return Response({'message':'Bad Request'},status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        subject = get_object_or_404(Subject , pk=pk)
        subject.delete()
        return Response({'message':'Subject Data Deleted Successfully'},status=status.HTTP_204_NO_CONTENT)