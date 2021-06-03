from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def register(request):

	if request.method == "POST":

		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		if password1 == password2:

			if(User.objects.filter(username = username).exists()):
				
				print("Username already taken")
				messages.info(request, "Username already taken")
				return redirect('register')

			elif(User.objects.filter(email = email).exists()):
				
				print("Email already taken")
				messages.info(request, "Email already taken")
				return redirect('register')

			else:

				user = User.objects.create_user(first_name = first_name, last_name = last_name, username = username, password = password1, email = email)
				user.save()
				print("User created")
				return redirect('login')

		else:
			print("password did not match")
			messages.info(request, "Password did not match")
			return redirect('register')

	else:

		return render(request, 'registration_form.html')

def login(request):

	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username = username, password = password)


		if user is not None:
			auth.login(request,user)
			print("user logged in")
			return redirect("/")

		else:
			print("incorrect login credentials")
			messages.info(request, "Incorrect login credentials")
			return redirect("login")


	return render(request, 'login_form.html')

def logout(request):

	auth.logout(request)
	print("user logged out")
	return redirect('/')