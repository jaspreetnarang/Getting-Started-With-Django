from django.shortcuts import render,redirect,HttpResponse
from polls.forms import SignUpForm
from django.contrib.auth.models import User
def home(request):
	numbers=[1,2,3,4,5]
	name = 'Jaspreet'
	args = {'myName': name}
	return render(request,'polls/login.html',args)

def signup(request):
	if request.method =='POST':
		form=SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/polls')
	else:
			 form= SignUpForm()
			 args= {'form':form}
			 return render(request,'polls/signup_form.html',args)


def profile(request):
	args={'user':request.user}
	return render(request,'polls/profile.html',args)
