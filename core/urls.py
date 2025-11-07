from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/test/', views.TestAPI.as_view(), name='test-api'),
    path('api/user/', views.UserAPI.as_view(), name='user-api'),
    path('api/person/', views.PersonAPI.as_view(), name='person-api'),
    path('api/people/', views.PeopleAPI.as_view(), name='people-api'),
    path('persons/', views.person_list, name='person-list'),
    path('people/', views.people_list, name='people-list'),
    path('api/element/', views.ElementAPI.as_view(), name='element-api'),
    path('api/element/<int:pk>/', views.ElementDetailAPIView.as_view(), name='element-detail'),
    path('api/subject', views.SubjectAPI.as_view(), name='subject-api'),
    path('api/subject/<int:pk>/', views.SubjectDetailAPI.as_view(), name='subject-api')

]