from django.contrib import admin

from .models import DoctorateStudent, MasterStudent

admin.site.register(MasterStudent)
admin.site.register(DoctorateStudent)

