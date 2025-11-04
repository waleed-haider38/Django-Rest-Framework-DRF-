from django.shortcuts import render
from rest_framework.viewsets import ViewSet , ModelViewSet
from .models import User
from .serializer import UserSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html')

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer