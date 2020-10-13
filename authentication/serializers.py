from rest_framework import serializers
from .models import User


class EmailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['email']


class KeySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['key']
