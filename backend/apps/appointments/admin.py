from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", "hospital", "doctor", "patient", "appointment_date", "created_at")
    list_filter = ("hospital", "doctor", "patient", "appointment_date")
    search_fields = ("hospital__name", "doctor__user__name", "patient__user__name")
