from rest_framework import viewsets
from api.serializers import *
from api.models import *

class RecordLabelViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows Artist to be viewed or edited
	"""
	queryset = record_label_model.RecordLabel.objects.all()
	serializer_class = record_label_serializer.RecordLabelSerializer