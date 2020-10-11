from django.contrib.auth.models import User
from rest_framework import serializers
from .models import EmailKey

class EmailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['email']

class KeySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmailKey
        fields = ['key']
