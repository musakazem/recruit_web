from django.shortcuts import render

# Create your views here.

def register(request):

	return render(request, 'registration_form.html')

def login(request):

	return render(request, 'login_form.html')
