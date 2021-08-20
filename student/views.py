from student.forms import StudentRegistraion
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import User
from django.contrib import messages

# Create your views here.
#this function is for create and show data
def add_show(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=StudentRegistraion(request.POST)
            if fm.is_valid():
                fm.save()
                fm=StudentRegistraion()
                messages.add_message(request, messages.SUCCESS,'Your Acount Has Been Created!!')
        else:
            fm=StudentRegistraion()
        stu=User.objects.all()
        return render(request,'student/addandshow.html',{'forms':fm,'students':stu})
    else:
        return HttpResponseRedirect('/')

#this function is for only delete data
def delete_data(request,id):
    if request.user.is_authenticated:
        fm=User.objects.get(pk=id)
        fm.delete()
        return HttpResponseRedirect('/addStudent/')
    else:
      return HttpResponseRedirect('/')  

#this function is for only update data
def update_data(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=User.objects.get(pk=id)
            fm=StudentRegistraion(request.POST,instance=pi)
            if fm.is_valid():
                fm.save()
                messages.add_message(request, messages.SUCCESS,'Your Data Has Been Updated!!')
        else:
            pi=User.objects.get(pk=id)
            fm=StudentRegistraion(instance=pi) 
        return render(request,'student/updateStudent.html',{'forms':fm})
    else:
      return HttpResponseRedirect('/') 
