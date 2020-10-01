from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    STATUS_CHOICE = (('draft','Draft'),('published','Published'))
    title   = models.CharField(max_length=250)
    slug    = models.SlugField(max_length=250,unique_for_date='publish')
    author  = models.ForeignKey(User,on_delete=models.CASCADE)
    body    = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status  = models.CharField(max_length=10,
    choices=STATUS_CHOICE, default='draft')
    class Meta:
        ordering = ('-publish',)
    def get_absolute_url(self):
        return reverse('Blog:post_details',
        args=[
        self.publish.year,
        self.publish.month,
        self.publish.day,
        self.slug]
        )
        

    def __str__(self):
        return self.title
