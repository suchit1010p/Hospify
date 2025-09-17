from django.db import models
from apps.users.models import User
from apps.hospitals.models import Hospital, Department


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="doctor_profile")
    hospitals = models.ManyToManyField(Hospital, related_name="doctors")
    departments = models.ManyToManyField(Department, related_name="doctors")
    specialization = models.CharField(max_length=50)
    experience_years = models.PositiveIntegerField(verbose_name="Years of Experience")
    consultation_fee = models.PositiveBigIntegerField(verbose_name="Consultation Fee (in local currency)")
    available = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.name}, specialized: {self.specialization}"
