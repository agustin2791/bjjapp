from __future__ import unicode_literals

from django.db import models
from django.db.models import permalink
from ckeditor.fields import RichTextField

# Create your models here.
class BlogCategories(models.Model):
	category = models.CharField(max_length=120, unique=True)
	slug = models.SlugField(max_length=120, unique=True)

	def __unicode__(self):
		return "%s" % self.category

	@permalink
	def get_absolute_url(self):
		return ('view_blog_category', None, {'slug': self.slug})

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
	body = RichTextField()
	posted = models.DateField(db_index=True, auto_now_add=True)
	author = models.ForeignKey('posts.BlogAuthor')

	def __unicode__(self):
		return "%s" % self.title

	@permalink
	def get_absolute_url(self):
		return ('view_blog_post', None, {'slug': self.slug})

class BlogAuthor(models.Model):
	author = models.CharField(max_length=60)
	slug = models.SlugField(max_length=60)
	bio = RichTextField()
	short_bio = RichTextField()
	image = models.ImageField(upload_to='author/profile/')
	thumbnail = models.ImageField(upload_to='author/profile/thumbnail/')

	def __unicode__(self):
		return self.author

	def create_thumbnail(self):
		# if no images
		if not self.image:
			return

		from PIL import Image
		from cStringIO import StringIO
		from django.core.files.uploadedfile import SimpleUploadedFile
		import os

		# max thumbnail size
		THUMBNAIL_SIZE = (150, 150)

		DJANGO_TYPE = self.image.file.content_type

		if DJANGO_TYPE == 'image/jpeg':
			PIL_TYPE = 'jpeg'
			FILE_EXTENTION = 'jpg'
		elif DJANGO_TYPE == 'image/png':
			PIL_TYPE = 'png'
			FILE_EXTENTION = 'png'

		#open Original photo
		image = Image.open(StringIO(self.image.read()))

		image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

		# save thumbnail
		temp_handle = StringIO()
		image.save(temp_handle, PIL_TYPE)
		temp_handle.seek(0)

		#save image to a SimpleUploadedFile to save into ImageField
		suf = SimpleUploadedFile(os.path.split(self.image.name)[-1],
			temp_handle.read(), content_type=DJANGO_TYPE)
		# Save SimpleUploadedFile into ImageField
		self.thumbnail.save('%s_thumbnail.%s' % (os.path.splitext(suf.name)[0], FILE_EXTENTION), suf, save=False)

	def save(self):
		# create thumbnail
		self.create_thumbnail()
		# self.resizeImage()
		super(BlogAuthor, self).save()

	@permalink
	def get_absolute_url(self):
		return ('authors', None, {'slug': self.slug})