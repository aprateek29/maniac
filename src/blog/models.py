from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos/')
    tags = models.CharField(max_length=20)
    date = models.DateField(default=timezone.now)








