from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=150)
    time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    author = models.CharField(max_length=150, blank=True, default="")