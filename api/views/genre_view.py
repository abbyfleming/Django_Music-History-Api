from rest_framework import viewsets
from api.serializers import *
from api.models import *

class GenreViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows Artist to be viewed or edited
	"""
	queryset = genre_model.Genre.objects.all()
	serializer_class = genre_serializer.GenreSerializer