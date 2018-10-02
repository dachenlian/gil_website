from django.contrib import admin
from .models import Profile, Course
from easy_thumbnails.fields import ThumbnailerField
from easy_thumbnails.widgets import ImageClearableFileInput


class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        ThumbnailerField: {'widget': ImageClearableFileInput},
    }


admin.site.register(Profile, MyModelAdmin)
admin.site.register(Course)
