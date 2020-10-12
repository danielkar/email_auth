from rest_framework import serializers
from .models import User

class EmailSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['email']

class KeySerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['key']
