from rest_framework import serializers
from .models import User, Count, Tree


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ["id", "username", "description", "power"]


class CountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Count
        fields = "__all__"


class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tree
        fields = "__all__"
