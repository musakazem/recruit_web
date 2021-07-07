from django.shortcuts import render, redirect
from .forms import ProfileForm, AboutForm, ImageForm
from django.contrib import messages
from .models import Profile


# Create your views here.

def home(request):
	return render(request, 'home.html')


def profile(request):

	return render(request, 'profile_page.html')

def edit_profile(request):

	form = ProfileForm()
	

	if request.method == "POST":

		form = ProfileForm(request.POST or None)
		

		
		

		if form.is_valid():
		
			obj = form.save(commit=False)
			obj.user_id = request.user.id

			obj.save()
			print("form saved")
			return redirect('profile')
		else:
		

			messages.info(request, "Form not saved")


	context = {'form':form}
	return render(request, 'edit_profile.html', context)


def edit_about(request):

	form = AboutForm()
	print("**************" + str(form))
	if request.method == "POST":

		form = AboutForm(request.POST)

		if form.is_valid():
			obj = form.save(commit = False)
			obj.user_id = request.user.id
			obj.save()
			print("******************about form saved")

			return redirect("profile")

		else:
		

			messages.info(request, "Form not saved")

	else:
		context = {"form": form}
		return render(request,"edit_about.html", context)

def edit_pic(request):

	form = ImageForm()

	if request.method == "POST":

		form = ImageForm(request.POST, request.FILES)
		print("*************" + str(form))

		if form.is_valid():

			obj = form.save(commit = False)
			obj.user_id = request.user.id
			obj.save()

			print("**********profile image uploaded")

			return redirect("profile")

		else:

			messages.info(request, "Form not saved")

	else:

		context = {"form": form}
		return render(request, "edit_pic.html", context)