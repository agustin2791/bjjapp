from __future__ import unicode_literals

from django.db import models
from django.db.models import permalink
from ckeditor.fields import RichTextField

# Create your models here.
class BjjLocation(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50)
	address = models.CharField(max_length=150, unique=True)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=2)
	zip_code = models.IntegerField()
	phone_number = models.IntegerField()
	lon = models.IntegerField()
	lat = models.IntegerField()
	instructor = models.ForeignKey('locations.BjjInstructor')

	def __unicode__(self):
		return self.name

	@permalink
	def get_absolute_url(self):
		return ('location_spec', None, {'slug': self.slug})

class BjjInstructor(models.Model):
	name = models.CharField(max_length=60)
	slug = models.SlugField(max_length=60)
	lineage = RichTextField()
	bio = RichTextField()
	img = models.ImageField(upload_to='instructor/profile', blank=True, null=True)
	thumbnail = models.ImageField(upload_to='instructor/profile/thumbnail', blank=True, null=True)

	def __unicode__(self):
		return self.name

	def create_thumbnail(self):
		# if no images
		if not self.img:
			return

		from PIL import Image
		from cStringIO import StringIO
		from django.core.files.uploadedfile import SimpleUploadedFile
		import os

		# max thumbnail size
		THUMBNAIL_SIZE = (150, 150)

		DJANGO_TYPE = self.img.file.content_type

		if DJANGO_TYPE == 'image/jpeg':
			PIL_TYPE = 'jpeg'
			FILE_EXTENTION = 'jpg'
		elif DJANGO_TYPE == 'image/png':
			PIL_TYPE = 'png'
			FILE_EXTENTION = 'png'

		#open Original photo
		image = Image.open(StringIO(self.img.read()))

		image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

		# save thumbnail
		temp_handle = StringIO()
		image.save(temp_handle, PIL_TYPE)
		temp_handle.seek(0)

		#save image to a SimpleUploadedFile to save into ImageField
		suf = SimpleUploadedFile(os.path.split(self.img.name)[-1],
			temp_handle.read(), content_type=DJANGO_TYPE)
		# Save SimpleUploadedFile into ImageField
		self.thumbnail.save('%s_thumbnail.%s' % (os.path.splitext(suf.name)[0], FILE_EXTENTION), suf, save=False)

	def save(self):
		# create thumbnail
		self.create_thumbnail()
		# self.resizeImage()
		super(BjjInstructor, self).save()