from django.db import models

class Genre(models.Model):
	genre_name = models.CharField(max_length=35)

	def __str__(self):
		return "{}".format(self.genre_name)

	class Meta:
		ordering = ('genre_name',)