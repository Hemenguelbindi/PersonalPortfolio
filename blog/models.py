import datetime
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField()
    
    
