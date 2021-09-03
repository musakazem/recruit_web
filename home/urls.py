from django.urls import path
from . import views

urlpatterns = [
	
	path('', views.home, name = 'home'),
	path('profile', views.profile, name = 'profile'),
	path('edit', views.edit_profile, name = 'edit_profile'),
	path('edit_about', views.edit_about, name = 'edit_about'),
	path('edit_pic', views.edit_pic, name = 'edit_pic'),
	path('job_post', views.job_post, name = 'job_post'),
	path('job_post/q_post', views.q_post, name = 'q_post'),
	path('joblist', views.joblist, name = 'joblist'),
	path('job_post/joblist/<str:jobpost_id>/', views.jobinfo, name = 'jobinfo'),
	path('a_post/<str:job_id>', views.a_post, name = 'a_post')
	
]