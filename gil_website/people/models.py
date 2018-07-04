from django.db import models


class Student(models.Model):
    profile_picture = models.ImageField(upload_to="uploads")
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
    pass


class Staff(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    office_hours = models.CharField(max_length=100)


class Faculty(models.Model):
    profile_picture = models.ImageField(upload_to='uploads')
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    fax = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    research_interests = models.TextField()
