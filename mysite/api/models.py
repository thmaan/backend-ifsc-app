from django.db import models
from taggit.managers import TaggableManager

class News(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=100)
	introduction = models.CharField(max_length=250)
	description = models.TextField()
	published = models.DateField(auto_now_add=True)
	slug = models.SlugField(unique=True, max_length=100)
	tags = TaggableManager()
	date_added = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.title
