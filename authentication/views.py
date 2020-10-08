from email_auth import settings
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED,
)
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import EmailKey
import random


class Email(APIView):

    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email_code = generate_email_code(serializer.data['email'])

        send_token(serializer.data['email'], email_code)

        return Response(status=status.HTTP_201_CREATED)


class Key(APIView):

    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = EmailKey.objects.get(key=request.data)
        token, _ = Token.objects.get_or_create(user=user)

        if user.is_exprired():
            return Response({"error": "time-out"}, status=status.HTTP_400_BAD_REQUEST)

        if key_check(request.data):
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Wrong key"}, status=status.HTTP_400_BAD_REQUEST)


def key_check(sent_key):
    try:
        user = EmailKey.objects.get(key=sent_key)
        return True
    except:
        return False


def generate_email_code(email):
    email_code = random.randint(1, 100)

    user = EmailKey.objects.get_or_create(email=email, key=email_code)
    user.save()

    return email_code


def send_token(email, token):
    send_mail('Confirm your login', token, settings.DEFAULT_FROM_EMAIL, [email], fail_silently=False)
