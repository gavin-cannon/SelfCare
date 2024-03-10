from django.db import models

# Create your models here.

class SelfCareItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    completed = models.BooleanField(default=False)