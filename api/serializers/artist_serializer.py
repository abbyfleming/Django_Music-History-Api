from rest_framework import serializers
from api.models import *

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
	"""
	Purpose: Class for data serialization for Album
	"""

	class Meta:
		model = artist_model.Artist
		fields = ('artist_name', 'first_name', 'last_name', 'year_established')

		#depth 1 allows you to see everything on a foreign key
		#depth 2 will look inside foreign keys on foreign key


