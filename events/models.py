from __future__ import unicode_literals

from django.db import models

# Create your models here.
class EventType(models.Model):
	event_name = models.CharField(unique=True)
	date = models.DateField()
	time = models.DateField()
	url = models.CharField()
	andress = 
