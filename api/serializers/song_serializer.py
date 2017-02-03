from rest_framework import serializers
from api.models import *

class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = song_model.Song
        fields = ('artist', 'album', 'title', 'length')
        depth = 1
