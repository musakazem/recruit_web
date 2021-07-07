from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):

	user = models.OneToOneField(User, null = False, on_delete = models.CASCADE, primary_key = True)

	desc = models.TextField()
	designation = models.CharField(max_length = 100)
	addr = models.CharField(max_length = 100)
	link = models.CharField(max_length=100)
	
class ProfileAbout(models.Model):

	user = models.OneToOneField(User, null = False, on_delete = models.CASCADE, primary_key = True)

	about = models.TextField(default = "")
	
class ProfilePic(models.Model):

	user = models.OneToOneField(User, null = False, on_delete = models.CASCADE, primary_key = True)

	profile_pic = models.ImageField(upload_to = 'pics/', default = "")