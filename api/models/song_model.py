from django.db import models
from .artist_model import Artist
from .album_model import Album


class Song(models.Model):

	artist = models.ForeignKey(
	Artist, 
	on_delete=models.CASCADE,
	related_name='songs'
	)

	album = models.ForeignKey(
		Album,
		on_delete=models.CASCADE,
		related_name='songs'
	)

	title = models.CharField(max_length=70)
	length = models.TimeField(null='True')

	def __str__(self):
		return "{}".format(self.title)

	class Meta:
		ordering = ('artist',)