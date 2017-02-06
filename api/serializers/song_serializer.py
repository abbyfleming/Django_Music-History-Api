from rest_framework import serializers
from api.models import *

class SongSerializer(serializers.HyperlinkedModelSerializer):
	"""
	Purpose: Class for data serialization for Song
	"""
	class Meta:
		model = song_model.Song
		fields = ('artist', 'album', 'title', 'length', 'url')
		# depth = 1
