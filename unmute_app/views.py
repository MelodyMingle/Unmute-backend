from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Thing, AccessToken
from .serializers import Unmute_AppSerializer
import base64
import requests
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from datetime import datetime, timedelta


def store_code(code:str, user_id: str):
	raise NotImplemented

class Unmute_AppList(ListCreateAPIView):
	queryset = Thing.objects.all()	
	# Serializing (making it easy to transport)
	serializer_class = Unmute_AppSerializer
		
	
class Unmute_AppDetail(RetrieveUpdateDestroyAPIView):
	queryset = Thing.objects.all()
	serializer_class = Unmute_AppSerializer

	def store_code(access_token: str):
		print(access_token)

class SpotifyRequestAccessToken(GenericViewSet):
	permission_classes = (AllowAny,)

	def create(self, request):
			grant_type = "client_credentials"
			client_id = "2947c2a7e7de405e9acd1c475962c1f2"
			client_secret = "c1526e2de18748d5b698b34a97c67a18"

			url = "https://accounts.spotify.com/api/token"
			data = {
					"grant_type": grant_type,
					"client_id": client_id,
					"client_secret": client_secret
			}

			headers = {
					"Content-Type": "application/x-www-form-urlencoded"
			}

			response = requests.post(url, data=data, headers=headers)

			data = Response(status=status.HTTP_200_OK, data=response.json())

			access_token = response.json().get('access_token')
			expiration_time = datetime.now() + timedelta(seconds=response.json().get('expires_in'))
			AccessToken.objects.create(token=access_token, expiration_time=expiration_time)

			return Response(response.json(), status=status.HTTP_200_OK)

class SpotifySearch(GenericViewSet):
	permission_classes = (AllowAny,)

	def list(self, request):
		query = request.query_params.get("query")
		token = AccessToken.objects.get(id="1")
		headers = {"Authorization": f"Bearer {token}"}
		type_of_search = "track"
		limit = 20
		offset = 0
		params = {"q": query, "type": type_of_search, "limit": limit, "offset": offset}
		url = "https://api.spotify.com/v1/search"

		response = requests.get(url, headers=headers, params=params)

		return Response(status=status.HTTP_200_OK, data=response.json())

	
