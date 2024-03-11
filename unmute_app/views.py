from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Thing
from .serializers import Unmute_AppSerializer
	
class Unmute_AppList(ListCreateAPIView):
	queryset = Thing.objects.all()
		
	# Serializing (making it easy to transport)
	serializer_class = Unmute_AppSerializer
		
	
class Unmute_AppDetail(RetrieveUpdateDestroyAPIView):
	queryset = Thing.objects.all()
	serializer_class = Unmute_AppSerializer