from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from datetime import timedelta
from django.utils import timezone


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    key = models.CharField(max_length=30)
    expiry_time = models.DateTimeField(default=timezone.now() + timezone.timedelta(minutes=5))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def is_expired(self):
        if timezone.now() >= self.expiry_time:
            return True
        else:
            return False
