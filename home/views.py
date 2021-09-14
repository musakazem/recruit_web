from django.shortcuts import render, redirect
from .forms import ProfileForm, AboutForm, ImageForm, JobPostForm, QuestionForm, AnswerForm
from django.contrib import messages
from .models import Profile, JobPost, Question
from django.urls import reverse


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


def  job_post(request):

	form = JobPostForm()

	if request.method == "POST":
		form = JobPostForm(request.POST, request.FILES)
		print("*************" + str(form))

		if form.is_valid():
			obj = form.save(commit = False)
			obj.user_id = request.user.id
			obj.save()

			print("**********post uploaded")



			return redirect("job_post/q_post")
	
	else:	
		context = {"form": form}
		return render(request, "jobpost_form.html", context)

def q_post(request):

	form = QuestionForm()
	if request.method == "POST":
		form = QuestionForm(request.POST, request.FILES)

		if form.is_valid():
			obj = form.save(commit = False)
			jobpost_obj = JobPost.objects.latest("id")
			obj.jobpost_id = jobpost_obj.id
			obj.save()

			
			addr1 = str(jobpost_obj.id)
			addr2 = "joblist/"
			addr = addr2 + addr1
			return redirect(addr)

	context = {"form": form}
	return render(request, 'qpost_form.html',context)

def a_post(request, job_id):

	if request.method == "GET":

		job_obj = JobPost.objects.get(id = job_id)
		q_id = int(job_obj.id)
		q_obj = Question.objects.get(jobpost_id = q_id)

		
		print("*****************" + str(q_id))
		
		form = AnswerForm()

		context = {"q_obj":q_obj, "form":form}

		return render(request, 'apost_form.html', context)

		
	if request.method == "POST":
		form = AnswerForm(request.FILES, request.POST)
		

		
		if form.is_valid():
			
			obj = form.save(commit = False)
			q_id = request.POST.get("question_id",None)
			ans_text = request.POST.get('answer', None)
			print("*****************" + str(q_id))
			print("*****************" + str(ans_text))
		
			obj.user_id = request.user.id
			obj.question_id = q_id
			obj.answer = ans_text
			obj.save()

			return redirect("/profile")

	

def joblist(request):

	jobs = JobPost.objects.all()
	timestamps = JobPost.objects.values_list('date')
	print("*******************", timestamps)
	print("*******************", jobs)
	context = {"jobs": jobs, "timestamps":timestamps}

	return render(request, 'joblist_page.html', context)

def jobinfo(request, jobpost_id):

	content  = JobPost.objects.get(id = jobpost_id)

	context = {"content":content}

	return render(request, 'jobinfo_page.html', context)



def post_status(request, user_id):

	jobposts = JobPost.objects.all().order_by('-date')

	user_jobposts = jobposts.filter(user_id = user_id)

	context = {"jobposts" : user_jobposts}

	return render(request, 'poststatus_page.html', context)

###############################################################
#####changes jobpost status to False. Deactivates jobpost.#####
###############################################################

def change_status_false(request, post_id):

	jobposts = JobPost.objects.all()

	print("*********************" + str(post_id))
	jobpost = jobposts.get(id = post_id)

	user_id = jobpost.user_id

	print("*********************" + str(jobpost))

	jobpost.status = False
	jobpost.save()

	addr1 = str(user_id)
	addr2 = "profile/post_status/"
	addr = addr2 + addr1
	return redirect("/" + addr)

############################################################
#####changes jobpost status to True. Activates jobpost.#####
############################################################

def change_status_true(request, post_id):

	jobposts = JobPost.objects.all()

	print("*********************" + str(post_id))
	jobpost = jobposts.get(id = post_id)

	user_id = jobpost.user_id

	print("*********************" + str(jobpost))

	jobpost.status = True
	jobpost.save()

	addr1 = str(user_id)
	addr2 = "profile/post_status/"
	addr = addr2 + addr1
	return redirect("/" + addr)

def alert_page(request, post_id):

	jobpost = JobPost.objects.get(id = post_id)

	context = { "jobpost": jobpost }

	return render(request, "alert_page.html", context)

def delete_post(request, post_id):

	jobpost = JobPost.objects.get(id = post_id)

	user_id = jobpost.user_id
	
	jobpost.delete()

	addr1 = str(user_id)
	addr2 = "profile/post_status/"
	addr = addr2 + addr1
	return redirect("/" + addr)
