from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'M'),
        (FEMALE, 'F')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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