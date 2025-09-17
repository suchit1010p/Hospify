from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
	list_display = ("id", "user", "specialization", "available")
	list_filter = ("hospitals", "departments", "specialization")
	search_fields = ("user__name", "specialization", "hospitals__name", "departments__name")