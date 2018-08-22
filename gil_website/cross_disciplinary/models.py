from django.db import models
from django import forms


class Student(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'M'),
        (FEMALE, 'F')
    )

    student_id = models.CharField(max_length=100)
    eng_name = models.CharField(max_length=100)
    zh_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES,)
    college = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    reason = models.TextField()
    primary_email = models.EmailField()
    personal_page = models.URLField(blank=True)
    address = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to="uploads/cross/",
                                        blank=True)
    more_info = models.TextField(blank=True)

