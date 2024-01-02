from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from ckeditor.fields import RichTextField
from django.urls import reverse

class Event(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    event_image = ImageField(blank=False, null=False, upload_to='images/events')
    date_created = models.DateTimeField(auto_now=True)
    event_date = models.DateField(blank=False, null=False)
    start_time = models.TimeField(blank=False, null=False)
    end_time = models.TimeField(blank=False, null=False)
    price = models.IntegerField(default=0, blank=False, null=False)
    description = RichTextField(blank=False, null=False)
    # category = models.CharField(max_length = 255, default='chill')
    location = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.title + ' | ' + str(self.date_created)
    

class Story(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    story_image = ImageField(blank=False, null=False, upload_to='stories/')
    date_created = models.DateTimeField(auto_now=True)
    readtime = models.CharField(max_length=255)
    # category = models.CharField(max_length = 255, default='chill')
    Story = RichTextField(blank=False, null=False)

    def __str__(self):
        return str(self.author) + ' | ' + str(self.date_created)
    
    

STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)

class Initiative(models.Model):
    title =  models.CharField(max_length = 255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    organiser = models.ForeignKey(User, on_delete = models.CASCADE, related_name='initiative_posts', null=True)
    date_created = models.DateTimeField(auto_now_add = True)
    description = RichTextField()
    initiative_image = ImageField(upload_to="initiatives/")
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.IntegerField(choices=STATUS, default=0)
    goals = RichTextField()
    category = models.CharField(max_length = 255, default='Sustainabilility')

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    name = models.CharField(max_length = 255, blank = False, null=False)
    email = models.EmailField(blank = False, null=False)
    subject = models.CharField(max_length = 255)
    message = models.TextField()

    def __str__(self):
        return self.name

class Comments(models.Model):
    initiative = models.ForeignKey(Initiative, related_name='comments' ,on_delete = models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s - %s' % (self.initiative.title, self.name)