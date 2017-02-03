from rest_framework import viewsets
from api.serializers import *
from api.models import *

class SongViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows Artist to be viewed or edited
	"""
	queryset = song_model.Song.objects.all()
	serializer_class = song_serializer.SongSerializer