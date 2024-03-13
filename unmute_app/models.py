from django.db import models
from django.contrib.auth import get_user_model

class Thing(models.Model):
	owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	name = models.CharField(max_length=64)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.name
	
class AccessToken(models.Model):
    user = "1"
    token = models.CharField(max_length=255)
    expiration_time = models.DateTimeField()

    # Additional fields and methods as needed

    def __str__(self):
        return self.token