from rest_framework import serializers
from api.models import *

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = album_model.Album
        fields = ('artist','release_year', 'length', 'record_label')
        #depth = 1 #depth 1 allows you to see everything on a foreign key

        #depth allows you to see everything on a foreign key
        #depth 2 will look inside foreign keys on foreign key


