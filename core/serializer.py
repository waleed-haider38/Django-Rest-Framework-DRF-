from rest_framework import serializers
from .models import Person , People, Element

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields= '__all__'

class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = '__all__'
