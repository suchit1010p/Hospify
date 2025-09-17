
from django.contrib import admin
from .models import City, Hospital, Department, HospitalAdmin


class CityAdmin(admin.ModelAdmin):
	list_display = ("id", "name", "state", "country")
	search_fields = ("name", "state", "country")

class DepartmentInline(admin.TabularInline):
	model = Department
	extra = 0

class HospitalAdminModel(admin.ModelAdmin):
	list_display = ("id", "name", "city", "phone", "email")
	search_fields = ("name", "city__name", "phone", "email")
	inlines = [DepartmentInline]


class DepartmentAdmin(admin.ModelAdmin):
	list_display = ("id", "name", "hospital")
	search_fields = ("name", "hospital__name")

class HospitalAdminProfileAdmin(admin.ModelAdmin):
	list_display = ("id", "user", "hospital")
	search_fields = ("user__email", "hospital__name")

admin.site.register(City, CityAdmin)
admin.site.register(Hospital, HospitalAdminModel)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(HospitalAdmin, HospitalAdminProfileAdmin)
