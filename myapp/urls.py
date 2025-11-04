from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('users/', views.UserView.as_view({'get': 'list','post':'create'}), name='user-list'),
]
