from django.urls import path
from . import views
from .views import ItemDetailView, TestItemView, AnimalView, AnimalDetailView

urlpatterns = [
    path("", views.index, name="index"),
    path("api/", TestItemView.as_view(), name="item-list"),  # API list/create
    path("api/<int:pk>/", ItemDetailView.as_view(), name="item-detail"),
    path("animal/", AnimalView.as_view(), name="animal"),
    path("animal/<int:pk>/", AnimalDetailView.as_view(), name="animal-id"),
]
