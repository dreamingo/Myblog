from django.db import models

# Create your models here.

class Tag(models.Model):
	""" Docstring for Tags """
	tag_name = models.CharField(max_length=20, blank=True)
	create_Time = models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
		return self.tag_name

class User(models.Model):
	"""docstring for User"""
	name = models.CharField(max_length = 30)
	Email = models.EmailField(max_length = 30)
	gender = models.CharField(max_length = 1)
	password = models.TextField()
	avatar = models.ImageField(upload_to = 'avatar', blank=True)

	def __unicode__(self):
		return self.name

class Category(models.Model):
	'''Docstring for Category'''
	name = models.TextField()
	def __unicode__(self):
		return self.name

class Blog(models.Model):
	caption = models.CharField(max_length = 50)
	author = models.ForeignKey(User)
	tags = models.ManyToManyField(Tag, blank=True)
	content = models.TextField()
	publish_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now_add=True)
	category = models.ForeignKey(Category)


class Photos(models.Model):
	description = models.TextField()
	img = models.ImageField(upload_to = 'photo')
	publish_time = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User)

class Comments(models.Model):
	author = models.CharField( max_length=100)
	email = models.EmailField()
	publish_time = models.DateTimeField(auto_now_add=True)
	content = models.TextField()
	blog = models.ForeignKey(Blog)
