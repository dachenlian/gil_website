from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from easy_thumbnails.fields import ThumbnailerImageField


class Course(models.Model):
    level = models.IntegerField()
    name = models.CharField(max_length=255)
    credit = models.IntegerField()
    department = models.CharField(max_length=255)
    required = models.CharField(max_length=255)
    professor = models.CharField(max_length=255)
    note = models.TextField(blank=True, default="")
    selected = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Profile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'M'),
        (FEMALE, 'F')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)
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
    profile_picture = ThumbnailerImageField(upload_to="uploads/cross/", blank=True)
    more_info = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.zh_name} / {self.eng_name} / {self.student_id}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
