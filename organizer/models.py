from django.db import models
from datetime import datetime
from django.utils import timezone


class Review(models.Model):
	title = models.CharField(max_length=50)
	content = models.CharField(max_length=255)
	rating = models.FloatField(default = 0)

	class Meta:
		db_table = "review"

class Event(models.Model):
	event_name = models.CharField(max_length=50)
	event_description = models.CharField(max_length=50)
	event_type = models.CharField(max_length=50)
	start_date = models.DateField(default = datetime.now)
	end_date = models.DateField(default = datetime.now)
	start_time = models.TimeField(default = timezone.now)
	end_time = models.TimeField(default = timezone.now)
	isCanceled = models.BooleanField(default = False)
	isDeleted = models.BooleanField(default = False)
	isFinished = models.BooleanField(default = False)

	class Meta:
		db_table = "event"


class EventRequest(models.Model):
	description = models.CharField(max_length=255)
	date_sent = models.DateField(default = datetime.now)
	time_sent = models.TimeField(default = timezone.now)
	request_type = models.CharField(max_length=50)
	isPending = models.BooleanField(default = True)
	isConfirmed = models.BooleanField(default = False)
	isDeleted = models.BooleanField(default = False)

	class Meta:
		db_table = "event_request"

class Organizer(models.Model):
	request = models.ManyToManyField(EventRequest)
	events = models.ManyToManyField(Event, related_name = "organizer")

	class Meta:
		db_table= "organizer"   