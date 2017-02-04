from django.db import models

class Genre(models.Model):
	"""
	Purpose: Class to create a table representing a genre
	Variables: 
		name - string, name of genre
	"""
	genre_name = models.CharField(max_length=35, default='')

	def __str__(self):
		return "{}".format(self.genre_name)

	class Meta:
		ordering = ('genre_name',)