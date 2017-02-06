from django.conf.urls import url, include
from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()
router.register(r'artists', artist_view.ArtistViewSet)
router.register(r'albums', album_view.AlbumViewSet)
router.register(r'genres', genre_view.GenreViewSet)
router.register(r'songs', song_view.SongViewSet)
router.register(r'labels', record_label_view.RecordLabelViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]