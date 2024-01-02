from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from sorl.thumbnail import ImageField
from ckeditor.fields import RichTextField

class Profile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete = models.CASCADE,
        related_name = 'profile'
    )
    profile_image = ImageField(upload_to='images/profile')
    last_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    bio = RichTextField()
    proffession = models.CharField(max_length=255)

    def __str__(self):
        return str(self.user.username)
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    # create a new profile when a new django user is created
    if created:
        Profile.objects.create(user=instance)