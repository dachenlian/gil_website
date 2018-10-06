from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField


class Student(models.Model):
    profile_picture = ThumbnailerImageField(upload_to="uploads/people/", blank=True,
                                            default="static/people/profile_pic.png")
    eng_name = models.CharField("English name", max_length=100)
    zh_name = models.CharField("Chinese name", max_length=100)
    email = models.EmailField()
    research_interests = models.TextField()

    def __str__(self):
        return self.eng_name

    class Meta:
        abstract = True


class MasterStudent(Student):
    FIRST = 'FIRST'
    SECOND = 'SECOND'
    THIRD = 'THIRD'
    FOURTH = 'FOURTH'
    GRAD = 'GRAD'
    YEAR_OF_STUDY_CHOICES = (
        (FIRST, 'First'),
        (SECOND, 'Second'),
        (THIRD, 'Third'),
        (FOURTH, 'Fourth'),
        (GRAD, 'Graduated'),
    )
    year_of_study = models.CharField(
        max_length=10,
        choices=YEAR_OF_STUDY_CHOICES,
        default=FIRST,
    )


class DoctorateStudent(Student):
    CURRENT = 'CURRENT'
    GRAD = 'GRAD'
    YEAR_OF_STUDY_CHOICES = (
        (CURRENT, 'Current'),
        (GRAD, 'Graduated'),
    )
    year_of_study = models.CharField(
        max_length=10,
        choices=YEAR_OF_STUDY_CHOICES,
        default=CURRENT
    )


class Staff(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    office_hours = models.CharField(max_length=100)


class Faculty(models.Model):

    class Meta:
        verbose_name_plural = "Faculty"

    CURRENT = 'CURRENT'
    RETIRED = 'RETIRED'

    STATUS_CHOICES = (
        (CURRENT, 'Current'),
        (RETIRED, 'Retired')
    )

    profile_picture = ThumbnailerImageField(upload_to='uploads/faculty', blank=True)
    zh_name = models.CharField("Chinese name", max_length=100, blank=True)
    eng_name = models.CharField("English name", max_length=100, blank=True)
    title = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    fax = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    education = models.CharField(max_length=1000)
    research_interests = models.TextField()
    cv_upload = models.FileField(upload_to='uploads/faculty/cv', blank=True)
    status = models.CharField(default=CURRENT, max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.zh_name} / {self.eng_name}"
