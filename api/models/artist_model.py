from django.db import models

class Artist(models.Model):
    artist_name = models.CharField(max_length=70)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    year_established = models.IntegerField(max_length=4, null='True')
    

    def __str__(self):
    	return "{}".format(self.artist_name)

    class Meta:
        ordering = ('artist_name',)
