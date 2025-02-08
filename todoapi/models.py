from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser (AbstractUser):
    username = models.CharField(max_length=50, blank=False, null=False, unique=True)
    email = models.EmailField(unique=True,  blank=False, null=False)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    phone_number = models.CharField(max_length=12, blank=False, null=False, unique=True)
    address = models.CharField(max_length=50, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.username