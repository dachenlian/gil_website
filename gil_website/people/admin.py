from django.contrib import admin
from easy_thumbnails.fields import ThumbnailerField
from easy_thumbnails.widgets import ImageClearableFileInput

from .models import DoctorateStudent, MasterStudent, Faculty


class StudentAdmin(admin.ModelAdmin):
    list_display = ('zh_name', 'eng_name', 'year_of_study')
    formfield_overrides = {
        ThumbnailerField: {'widget': ImageClearableFileInput},
    }


class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        ThumbnailerField: {'widget': ImageClearableFileInput},
    }


admin.site.register(MasterStudent, StudentAdmin)
admin.site.register(DoctorateStudent, StudentAdmin)
admin.site.register(Faculty, MyModelAdmin)
