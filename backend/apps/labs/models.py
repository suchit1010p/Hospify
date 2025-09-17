from django.db import models
from apps.hospitals.models import Hospital
# Create your models here.

class LabService(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='labs')
    name = models.CharField(max_length=30)
    description = models.TextField()
    avg_wait_time = models.PositiveIntegerField()

    def __str__(self):
        return self.name