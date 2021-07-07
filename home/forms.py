from django.forms import ModelForm
from .models import Profile, ProfileAbout, ProfilePic



class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = ['desc','designation','addr','link']

class AboutForm(ModelForm):
	class Meta:
		model = ProfileAbout
		fields = ['about']

class ImageForm(ModelForm):
	class Meta:
		model = ProfilePic
		fields = ['profile_pic']