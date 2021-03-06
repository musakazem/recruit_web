from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Profile(models.Model):

	user = models.OneToOneField(User, null = False, on_delete = models.CASCADE, primary_key = True)

	desc = models.TextField()
	designation = models.CharField(max_length = 150)
	addr = models.CharField(max_length = 100)
	link = models.CharField(max_length=100)
	
class ProfileAbout(models.Model):

	user = models.OneToOneField(User, blank = True,  null = False, on_delete = models.CASCADE, primary_key = True)

	about = models.TextField(default = "")
	
class ProfilePic(models.Model):

	user = models.OneToOneField(User, blank = True, null = False, on_delete = models.CASCADE, primary_key = True)

	profile_pic = models.ImageField(upload_to = 'pics/', default = "")

class JobPost(models.Model):
	position = models.CharField(max_length = 150)
	institution = models.CharField(max_length = 100)

	employment_choice = (

			("full-time" , "Full-time"),
			("part-time" , "Part-time"),
			("contract" , "Contract"),
			("temporary" , "Temporary"),
			("volunteer" , "Volunteer"),
			("internship" , "Internship"),

		)

	
	employment_type = models.CharField(max_length = 50, blank = True, choices = employment_choice)
	location = models.CharField(max_length = 50)
	pay = models.IntegerField()
	img = models.ImageField(upload_to = 'pics/', blank = True)
	user = models.ForeignKey(User, default = 1, null = True, on_delete = models.SET_NULL)
	desc = RichTextField(null = True, blank = True)
	date = models.DateTimeField(auto_now_add = True, null = True)
	status = models.BooleanField(default=True)


class Question(models.Model):

	question = RichTextField(null = True, blank = True)

	jobpost = models.OneToOneField(
		JobPost, 
		blank = True, 
		null = True, 
		on_delete = models.SET_NULL)

	date = models.DateTimeField(auto_now_add = True, null = True, blank = True)
 

class Answer(models.Model):

	answer = RichTextField(null = True, blank = True)

	question = models.ForeignKey(
		Question,
		blank = True,
		null = True,
		on_delete = models.CASCADE
		)

	user = models.ForeignKey(
		User,
		null = True,
		blank = True,
		on_delete = models.CASCADE
		)
	date = models.DateTimeField(auto_now_add = True, null = True, blank = True)