from django.urls import path
from .views import Unmute_AppList, Unmute_AppDetail
	
urlpatterns = [
	path("", Unmute_AppList.as_view(), name="thing_list"),
	path("<int:pk>/", Unmute_AppDetail.as_view(), name="thing_detail")
]