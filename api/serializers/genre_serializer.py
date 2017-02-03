from rest_framework import serializers
from api.models import *

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = genre_model.Genre
        fields = ('genre_name',)

        #if it's one, then add a trailing comma