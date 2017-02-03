from rest_framework import viewsets
from api.serializers import *
from api.models import *

class AlbumViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows Artist to be viewed or edited
	"""
	queryset = album_model.Album.objects.all()
	serializer_class = album_serializer.AlbumSerializer