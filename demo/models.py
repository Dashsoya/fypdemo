from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    STATUS_CHOICES = [
        ('covid', 'COVID'),
        ('normal', 'Normal'),
        ('not_applicable', 'Not Applicable'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    account_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    ROLE_CHOICES = [
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
        ('system_admin', 'System Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    # Additional fields if needed

