from django.db import models
from .artist_model import Artist
from .album_model import Album


class Song(models.Model):
	"""
	Purpose: Class to create a table representing a song
	Variables: 
		artist - FK to Artist
		album - FK to Album
		title - string, title of album
		length - interger, milliseconds length of song
	"""

	artist = models.ForeignKey(
		Artist,
		on_delete=models.CASCADE,
	)

	album = models.ForeignKey(
		Album,
		on_delete=models.CASCADE,
		# related_name='songs'
	)

	title = models.CharField(max_length=70)
	length = models.IntegerField(help_text="milliseconds", null='True', blank='True')

	def __str__(self):
		return "{}".format(self.title)

	class Meta:
		ordering = ('artist',)