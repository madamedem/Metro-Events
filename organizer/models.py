from django.db import models
from django.contrib.auth.models import User


# Create your models here.
GENDER_CHOICES = [('M', 'Male'),
                  ('F', 'Female')]

class Account(models.Model):
    username = models.CharField(max_length=15, primary_key=True)
    password = models.CharField(max_length=15)
    firstName = models.CharField(max_length=255)
    middleName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)

    def __str__(self):
        return self.firstName + ' ' + self.lastName

class Organizer(Account):
    birthday = models.DateField(default=False, blank=True, null=True)
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.firstName + ' ' + self.lastName



