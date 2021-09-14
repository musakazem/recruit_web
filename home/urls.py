from django.urls import path
from . import views

urlpatterns = [
	
	path('', views.home, name = 'home'),
	path('profile', views.profile, name = 'profile'),
	path('profile/post_status/<str:user_id>', views.post_status,  name = 'post_status_false'),
	path('profile/change_status_false/<str:post_id>', views.change_status_false, name = 'change_status_false'),
	path('profile/change_status_true/<str:post_id>', views.change_status_true, name = 'change_status_true'),
	path('profile/alert_page/<str:post_id>', views.alert_page, name = "alert_page"),
	path('delete_post/<str:post_id>', views.delete_post, name = "delete_post"),
	path('edit', views.edit_profile, name = 'edit_profile'),
	path('edit_about', views.edit_about, name = 'edit_about'),
	path('edit_pic', views.edit_pic, name = 'edit_pic'),
	path('job_post', views.job_post, name = 'job_post'),
	path('job_post/q_post', views.q_post, name = 'q_post'),
	path('joblist', views.joblist, name = 'joblist'),
	path('job_post/joblist/<str:jobpost_id>/', views.jobinfo, name = 'jobinfo'),
	path('a_post/<str:job_id>', views.a_post, name = 'a_post')
	
]