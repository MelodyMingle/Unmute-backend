from rest_framework import serializers
from .models import Thing
	
class Unmute_AppSerializer(serializers.ModelSerializer):
	class Meta:
		fields = ("id", "owner", "name", "description", "created_at")
		model = Thing