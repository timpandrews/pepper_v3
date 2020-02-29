from django.conf import settings
from django.db import models
from django.utils import timezone

class Journal(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    journal_date = models.DateField
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
