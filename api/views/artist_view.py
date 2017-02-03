from rest_framework import viewsets
from api.serializers import *
from api.models import *

class ArtistViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows Artist to be viewed or edited
	"""
	queryset = artist_model.Artist.objects.all()
	serializer_class = artist_serializer.ArtistSerializer



