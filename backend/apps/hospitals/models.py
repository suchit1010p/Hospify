from django.db import models
from apps.users.models import User
# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Hospital(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hospitals')
    address = models.TextField()
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
class Department(models.Model):
    name = models.CharField(max_length=100)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='department')
    
    def __str__(self):
        return self.name

class HospitalAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='hospital_admin_profile')
    hospital = models.OneToOneField(Hospital, on_delete=models.CASCADE, related_name='admin_profile')

    def __str__(self):
        return f"{self.user.name} - {self.hospital.name}"
    
