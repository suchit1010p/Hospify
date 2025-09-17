from django.db import models
from apps.users.models import User
# Create your models here.


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

BLOOD_GROUP_CHOICE = (
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B-', 'B-'),
    ('B+', 'B+'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
)


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patients')
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICE)
    emergency_contact = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Patient({self.user.name})"