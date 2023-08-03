from django.db import models

# Create your models here.

class Major(models.Model):
    name = models.CharField(max_length=255)

class Student(models.Model):
    std_id = models.IntegerField()
    first_name = models.CharField(max_length=256)
    prefix = models.IntegerField(max_length=256)
    last_name = models.CharField(max_length=256)
    phone = models.CharField(max_length=10)
    address = models.TextField(max_length=256)
