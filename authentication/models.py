from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone

class EmailKey(models.Model):
    
    key = models.CharField(max_length=30)
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    expiry_time = models.DateTimeField(default=timezone.now() + timezone.timedelta(minutes=5))

    def is_expired(self):
        if timezone.now() >= self.expiry_time:
            return True
        else:
            return False

class AllowedDomains(models.Model):
    domain = models.CharField(max_length=30)
