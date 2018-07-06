from django.db import models
from django.utils.timezone import now


class Event(models.Model):
    NEWS = 'NEWS'
    TALKS_EVENTS = 'TALKS_EVENTS'
    TYPE_OF_EVENT_CHOICES = [
        (NEWS, 'News'),
        (TALKS_EVENTS, 'Talks/Events'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    time_posted = models.DateTimeField(default=now)
    link = models.CharField(max_length=200, blank=True)
    file = models.FileField(upload_to='uploads/news', blank=True)
    type_of_event = models.CharField(max_length=200,
                                     choices=TYPE_OF_EVENT_CHOICES,
                                     default=NEWS)
