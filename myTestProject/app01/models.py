from django.db import models
import datetime


# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField()
    date = models.DateField()
    date_time = models.DateTimeField()

