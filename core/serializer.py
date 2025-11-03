from rest_framework import serializers
from .models import Person , People

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model:People
        fields= '__all__'
