from django.db import models


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

