import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser (AbstractUser):
    username = models.CharField(
        max_length=50, blank=False, null=False, unique=True)
    email = models.EmailField(unique=True,  blank=False, null=False)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    phone_number = models.CharField(
        max_length=12, blank=False, null=False, unique=True)
    address = models.CharField(max_length=50, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username


class Task (models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending'
        COMPLETED = 'completed'
        CANCELLED = 'cancelled'

    task_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,)
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    status = models.CharField(
        max_length=11, default=Status.PENDING, choices=Status.choices)
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)
    start_time = models.TimeField(blank=False, null=False)
    end_time = models.TimeField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    trigger_notification_at = models.CharField(
    max_length=50, default=None, blank=True, null=True)


def __str__(self):
    return self.title
