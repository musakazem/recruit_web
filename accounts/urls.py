from django.urls import path
from . import views
from home.views import edit_profile

urlpatterns = [
	
	path('register', views.register, name = 'register'),
	path('login', views.login, name = 'login'),
	path('logout', views.logout, name = 'logout'),
	path('edit',edit_profile, name = 'edit')
]