from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import User



class EmailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['email']
        extra_kwargs = {'email': {'validators': []}}


class KeySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['key']
