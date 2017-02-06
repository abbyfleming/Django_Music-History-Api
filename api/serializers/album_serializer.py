from rest_framework import serializers
from api.models import *

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
	"""
	Purpose: Class for data serialization for Album
	"""
	class Meta:
		model = album_model.Album
		fields = ('artist', 'genre', 'title', 'release_year', 'length', 'record_label', 'url')
		
		#depth = 1 #depth 1 allows you to see everything on a foreign key
		#depth allows you to see everything on a foreign key
		#depth 2 will look inside foreign keys on foreign key


