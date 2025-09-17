from django.db import models
from apps.appointments.models import Appointment
from apps.doctors.models import Doctor

# Create your models here.
class Queue(models.Model):
    def save(self, *args, **kwargs):
        # If status is completed, remove from queue
        if self.status == "completed" and self.pk is not None:
            self.delete()
            return
        if self._state.adding and not self.position:
            last_position = Queue.objects.filter(doctor=self.doctor).aggregate(models.Max('position'))['position__max']
            self.position = (last_position or 0) + 1
        super().save(*args, **kwargs)
        
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="queues")
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name="queue")
    position = models.PositiveIntegerField()
    estimated_time = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=[
        ("scheduled", "Scheduled"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ], default="scheduled") 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Queue #{self.id} - {self.appointment.patient.user.name} with {self.doctor.user.name} at {self.appointment.hospital.name} (Position: {self.position})"

    class Meta:
        ordering = ["position", "created_at"]
    