from rest_framework import serializers
from api.models import *

class RecordLabelSerializer(serializers.HyperlinkedModelSerializer):
	"""
	Purpose: Class for data serialization for RecordLabel
	"""
	class Meta:
		model = record_label_model.RecordLabel
		fields = ('record_label_name', 'url')
		#if it's one, then add a trailing comma