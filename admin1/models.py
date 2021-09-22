from django.db import models
from datetime import datetime
from django.utils import timezone

class Admin(models.Model):
	userID = models.CharField(max_length=50)
	organizerID = models.CharField(max_length=50)
	dateOrganizer = models.DateField(default = datetime.now)
	isAccepted = models.BooleanField(default = False)
	isDenied = models.BooleanField(default = False)

	class Meta:
		db_table = "admin1"

class UserRequest(models.Model):
	description = models.CharField(max_length=255)
	date_sent = models.DateField(default = datetime.now)
	time_sent = models.TimeField(default = timezone.now)
	request_type = models.CharField(max_length=50)
	isPending = models.BooleanField(default = True)
	isConfirmed = models.BooleanField(default = False)
	isDeleted = models.BooleanField(default = False)

	class Meta:
		db_table = "user_request" 