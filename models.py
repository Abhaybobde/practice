from django.db import models

# Create your models here.
class PlatinumModel(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    dob = models.DateField()
    mobile = models.CharField(max_length=30)
    address = models.CharField(max_length=30)

class goldModel(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    dob = models.DateField()
    mobile = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
class silverModel(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    dob = models.DateField()
    mobile = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
