from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    bbody = models.TextField(max_length=10000)
    image = models.ImageField(upload_to='images/')
