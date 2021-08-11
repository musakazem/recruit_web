from django.urls import path
from . import views

urlpatterns = [
	
	path('', views.home, name = 'home'),
	path('profile', views.profile, name = 'profile'),
	path('edit', views.edit_profile, name = 'edit_profile'),
	path('edit_about', views.edit_about, name = 'edit_about'),
	path('edit_pic', views.edit_pic, name = 'edit_pic'),
	path('job_post', views.job_post, name = 'job_post'),
	path('joblist', views.joblist, name = 'joblist'),
	
]