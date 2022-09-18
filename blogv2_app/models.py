from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

status_choices = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=250)
    page_title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    content = models.TextField()
    sum = models.CharField(max_length=125, null=True, blank=True)
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=250, choices=status_choices, default='draft')

    def __str__(self):
        return str(self.title) + '   |   ' + str(self.status)
    


    