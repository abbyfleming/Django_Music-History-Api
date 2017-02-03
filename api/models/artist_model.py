from django.db import models

class Artist(models.Model):
	"""
	Purpose: Class to create a table representing an artist
	Variables: 
		artist_name - string, name of artist (stagename)
		first_name - string, first name of artist
		last_name - string, last name of artist
		year established - interger, year established - max four YYYY
	"""

	artist_name = models.CharField(max_length=70)
	year_established = models.IntegerField(max_length=4, null='True', help_text="YYYY")
	

	def __str__(self):
		return "{}".format(self.artist_name)

	class Meta:
		ordering = ('artist_name',)
