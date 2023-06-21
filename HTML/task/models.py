from django.db import models

# Create your models here.

class NewTaskModels(models.Model):
    task = models.CharField(max_length=200)
    priority = models.IntegerField()