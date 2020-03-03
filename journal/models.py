from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import date

class Journal(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    journal_date = models.DateField(default=date.today)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Plants(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

