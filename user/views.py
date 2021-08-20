from django.contrib import messages
from django.shortcuts import render
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect

# Create your views here.
def user_register(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=RegistrationForm(request.POST)
            if fm.is_valid():            
                messages.success(request,'Account Created successfully!')
                fm.save()
        else:
            fm=RegistrationForm()
        return render(request,'user/registration.html',{'forms':fm})
    else:
        return HttpResponseRedirect('/addStudent/')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                username=request.POST['username']
                password=request.POST['password']
                user=authenticate(username=username,password=password)
                if user is not None:      
                    login(request,user)
                    return HttpResponseRedirect('/addStudent/')
            
        else:
            fm=AuthenticationForm()
        return render(request,'user/login.html',{'forms':fm})
    else:
       return HttpResponseRedirect('/addStudent/') 

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')