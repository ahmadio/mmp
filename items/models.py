import os
from django.db import models
from django.conf import settings
from people.models import Person
from django.conf import settings

class Type(models.Model):
	"""docstring for Type"""

	# Items types
	SERIES = 'series'
	VIDEO = 'video'
	PHOTO = 'photo'
	AUDIO = 'audio'
	DOC = 'doc'
	ITEMS_TYPES = (
		(SERIES, 'Series'),
		(VIDEO, 'Video'),
		(PHOTO, 'Photo'),
		(AUDIO, 'Audio'),
		(DOC, 'Doc'),
		)

	name = models.CharField(max_length=7, choices=ITEMS_TYPES, default=VIDEO)
	icon = models.ImageField(upload_to='media/itmes/app/type/media/', null=True, blank=True)

	def __unicode__(self):
		return self.name


class Category(models.Model):
	"""docx"""

	name = models.CharField(max_length=50)
	icon = models.ImageField(upload_to='media/items/app/category/media/', null=True, blank=True)


class Item(models.Model):
	"""docstring for Item"""

	#Genders
	MALE = 'male'
	FEMALE = 'female'
	ALL = 'all'
	AUDIENCE_GENDER = (
		(MALE, 'Male'),
		(FEMALE, 'Female'),
		(ALL, 'All'),
		)

	#Publishing status
	PUBLISHED = 'published'
	DRAFT = 'draft'
	PUBLISHING_STATUS = (
		(PUBLISHED, 'Published'),
		(DRAFT, 'Draft'),
		)

	title = models.CharField(max_length = 254)
	description = models.TextField()
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	media_url = models.URLField(max_length=254)
	video_preview = models.URLField(max_length=254)
	type = models.ForeignKey(Type)
	categories = models.ManyToManyField(Category)
	# paren_series = models.ForeignKey(Item)
	# series_items_count = models.PositiveInteger()
	publishing_status = models.CharField(max_length=10, choices=PUBLISHING_STATUS, default=PUBLISHED)
	audience_gender = models.CharField(max_length=7, choices=AUDIENCE_GENDER, default=ALL)
	audience_age = models.CharField(max_length=3, default='1')
	creation_date = models.DateTimeField(auto_now_add=True)
	modification_date = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.title

