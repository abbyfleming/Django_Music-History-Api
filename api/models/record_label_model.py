from django.db import models

class RecordLabel(models.Model):
	"""
	Purpose: Class to create a table representing a record label
	Variables: 
		name - string, name of record label
	"""
	record_label_name = models.CharField(max_length=70, default='')

	def __str__(self):
		return "{}".format(self.record_label_name)

	class Meta:
		ordering = ('record_label_name',)