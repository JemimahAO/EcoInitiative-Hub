
from django.db import models
from django.contrib.auth.models import User
# from sorl.thumbnail import ImageField
# from ckeditor.fields import RichTextField
# from django.urls import reverse

class Event(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #event_image = ImageField(blank=False, null=False, upload_to='images/events')
    date_created = models.DateTimeField(auto_now=True)
    event_date = models.DateField(blank=False, null=False)
    start_time = models.TimeField(blank=False, null=False)
    end_time = models.TimeField(blank=False, null=False)
    description = models.extField(blank=False, null=False)
    location = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.title + ' | ' + str(self.date_created)