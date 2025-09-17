from django.db import models
from apps.hospitals.models import Hospital
from apps.doctors.models import Doctor
from apps.patients.models import Patient

# Create your models here.

class Appointment(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="appointments")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="appointments")
    appointment_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment #{self.id} - {self.patient.user.name} with {self.doctor.user.name} at {self.hospital.name}"

    
