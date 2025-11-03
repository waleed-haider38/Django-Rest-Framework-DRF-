from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/test/', views.TestAPI.as_view(), name='test-api'),
    path('api/user/', views.UserAPI.as_view(), name='user-api'),
    path('api/person/', views.PersonAPI.as_view(), name='person-api'),
    path('persons/', views.person_list, name='person-list'),
]