from django.db import models
from .artist_model import Artist

class Album(models.Model):
	"""
	Purpose: Class to create a table representing an album
	Variables: 
		artist - FK to Artist
		title - string, title of album
		length - timefield, length of album
		record_label - string, record label 
	"""
	
	artist = models.ForeignKey(
		Artist, 
		on_delete=models.CASCADE,
		related_name='albums'
	)

	title = models.CharField(max_length=70)
	release_year = models.IntegerField(max_length=4, help_text="YYYY")
	length = models.TimeField(blank=True)
	record_label = models.CharField(max_length=35)

	def __str__(self):
		return "{}".format(self.title)

	class Meta:
		ordering = ('title',)