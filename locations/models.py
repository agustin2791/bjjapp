from __future__ import unicode_literals

from django.db import models
from django.db.models import permalink

# Create your models here.
class BjjLocation(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50, unique=True)
	address = models.CharField(max_length=150, unique=True)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=2)
	zip_code = models.IntegerField(max_length=5)
	phone_number = models.IntegerField(max_length=10)

	def __unicode__(self):
		return self.name

	@permalink
	def get_absolute_url(self):
		return ('view_type_of_entry', None, {'slug': self.slug})