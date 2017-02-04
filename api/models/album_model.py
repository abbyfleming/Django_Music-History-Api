from django.db import models
from .artist_model import Artist
from .genre_model import Genre

class Album(models.Model):
	"""
	Purpose: Class to create a table representing an album
	Variables: 
		artist - FK to Artist
		title - string, title of album
		length - integer, length of album in ms
		record_label - string, record label 
	"""
	
	artist = models.ForeignKey(
		Artist, 
		on_delete=models.CASCADE,
		related_name='albums'
	)

	genre = models.ForeignKey(
		Genre,
		on_delete=models.CASCADE,
		related_name='albums'
		)

	title = models.CharField(max_length=70)
	release_year = models.IntegerField(max_length=4, help_text="YYYY")
	length = models.IntegerField(help_text="milliseconds", null='True', blank='True')
	record_label = models.CharField(max_length=35)

	def __str__(self):
		return "{}".format(self.title)

	class Meta:
		ordering = ('title',)
