from __future__ import unicode_literals

from django.db import models
from django.db.models import permalink

# Create your models here.
class BlogCategories(models.Model):
	category = models.CharField(max_length=120, unique=True)
	slug = models.SlugField(max_length=120, unique=True)

	def __unicode__(self):
		return "%s" % self.category

	@permalink
	def get_absolute_url(self):
		return ('view_blog_category', None, {'slug': slef.slug})

class TypeOfEntry(models.Model):
	type_of = models.CharField(max_length=60, unique=True)
	slug = models.SlugField(max_length=60, unique=True)

	def __unicode__(self):
		return "%s" % self.type_of

	@permalink
	def get_absolute_url(self):
		return ('view_type_of_entry', None, {'slug': self.slug})

class BlogPost(models.Model):
	title = models.CharField(max_length=160)
	slug = models.SlugField(max_length=160)
	category = models.ForeignKey('posts.BlogCategories')
	body = models.TextField()
	posted = models.DateField(db_index=True, auto_now_add=True)
	type_of = models.ForeignKey('posts.TypeOfEntry')

	def __unicode__(self):
		return "%s" % self.title

	@permalink
	def get_absolute_url(self):
		return ('view_blog_post', None, {'slug': self.slug})