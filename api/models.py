from django.db import models
from taggit.managers import TaggableManager

class Category(models.Model):
	name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name

class News(models.Model):
	title = models.CharField(max_length=250)
	description = models.TextField()
	published = models.DateField(auto_now_add=True)
	slug = models.SlugField(unique=True, max_length=100)
	tags = TaggableManager()
	
	def __str__(self):
		return self.title

	