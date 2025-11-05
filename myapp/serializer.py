from rest_framework import serializers
from .models import User , Count

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Count
        fields = '__all__'