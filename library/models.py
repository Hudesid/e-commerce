from django.db import models
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    published_date = models.DateField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    descriptions = models.TextField()


    class Meta:
        ordering = ['-published_date']

