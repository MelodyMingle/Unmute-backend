from django.urls import path
from .views import Unmute_AppList, Unmute_AppDetail, SpotifyRequestAccessToken, SpotifySearch
	
urlpatterns = [
	path("", Unmute_AppList.as_view(), name="thing_list"),
	path("<int:pk>/", Unmute_AppDetail.as_view(), name="thing_detail"),
  path("spotify/access_token", SpotifyRequestAccessToken.as_view({'post': 'create'}), name="spotify_access"),
  path("spotify/search", SpotifySearch.as_view({'get': 'list'}), name="spotify_list")
]
