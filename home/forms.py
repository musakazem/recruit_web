from django.forms import ModelForm
from .models import Profile, ProfileAbout, ProfilePic, JobPost



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

class JobPostForm(ModelForm):
	class Meta:
		model = JobPost
		fields = ['position','institution','location','pay','desc','img','employment_type']