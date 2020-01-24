from django.contrib.auth import login as auth_login
from django.contrib.auth.models import auth
from django.core.mail import send_mail
from django.conf import settings
import socket
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import ( authenticate, login, logout)
from django.shortcuts import render, redirect, reverse
from depart.models import Department
from accounts.models import UserProfile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from .forms import UserprofileForm, StaffRegisterForm, UserLoginForm, ProfileForm
from depart.models import School, Department, Project, Supervisor, Group, Member, Progress, Files, ProjectStore, Comments



# Create your views here.
def userRegisterpage(request):
    if request.user.profile.role =='HOD':

        form = UserprofileForm()
        if request.method == 'POST':
            form = UserprofileForm(request.POST)
            
            if form.is_valid():
                email = form.cleaned_data.get('email')
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                first_name = form.cleaned_data.get('first_name')
                user = form.save(commit=False)
                subject = 'Registered on UR Final year project suprevision and management.'
                message = "Hi %s !, You have registered on UR Final year project suprevision and management. Your username is %s that you will using to log in and passwword is %s , please login after 30 minutes after receiving this email and change your password. thanks UR regards."%(
                    first_name, username, password)
                # some_html_message="""<h1>hi!</h1>"""
                #auth_login(request, user)
                user.save()
                # print(message)
                # socket.gethostbyname("smtp.gmail.com")
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=True
                )
                # send_mail.send()
                # print(send_mail)
                messages.success(request, 'Account created successfully')
                return HttpResponseRedirect (reverse('profile'))
                # return redirect('single_group')
        else:
            form = UserprofileForm()
    else:
        return HttpResponse("<h1 style='color=red;'>You are not allowed to access this resource</h1>")
    return render(request, 'accounts/students.html', {'form':form,})


def staffRegister(request):
    if request.user.profile.role == 'HOD':
        form = StaffRegisterForm()
        #department = Department.objects.get(pk=pk)
        if request.method == 'POST':
            form = StaffRegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                email = form.cleaned_data.get('email')
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                first_name = form.cleaned_data.get('first_name')
                user = form.save(commit=False)
                subject = 'Registered on UR Final year project suprevision and management.'
                message = "Hi <b>%s</b>!, You have registered on UR Final year project suprevision and management. Your username is <b>%s</b> that you will using to log in and passwword is <b>%s</b>, please login after 30 minutes after receiving this email and change your password. thanks UR regards." % (
                    first_name, username, password)
                #auth_login(request, user)
                # print(subject, message)
                form.save()
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=True
                )
                # print(send_mail)
                messages.success(request, 'Account created successfully')
                return HttpResponseRedirect(reverse('profile'))
                # return redirect('single_group')
        else:
            form = StaffRegisterForm()
    else:
        return HttpResponse("<h1 style='color=red;'>You are not allowed to access this resource</h1>")
    return render(request, 'accounts/staffregister.html', {'form':form})
    

def profilepage(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks profile added successfuly!!')
            return HttpResponseRedirect(reverse('school'))
    else:
        user = request.user
        profile = user.profile
        form = ProfileForm()
    return render(request, 'accounts/profile.html', {'form':form}) 

      
def LoginView(request, *args, **kwargs):
   
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if user.profile.role == 'student':                    
                    return HttpResponseRedirect(reverse("school"))
                elif user.profile.role== 'HOD':
                    return HttpResponseRedirect(reverse("school"))
                elif user.profile.role == 'dean':
                    return HttpResponseRedirect(reverse("school"))
                elif user.profile.role == 'lecturor':
                    return HttpResponseRedirect(reverse("lectucturor_dashboard"))
                elif user.profile.role == 'supervisor':
                    return HttpResponseRedirect(reverse("school"))
                elif user.profile.role == 'principle':
                    return HttpResponseRedirect(reverse("principle_dashboard"))
                else:
                    return HttpResponseRedirect(reverse("cordinator_dashboard"))
            else:
                print('enter valid credentails')
        else:
            print('enter valid credentails')
            messages.info(request, 'Please enter valid credentails.')
            form = AuthenticationForm()
    else:
        form = AuthenticationForm()
    
    context = {
        'form':form,
        # 'school':school,
        # 'count':count,
        # 'member':member,
        # 'departments':departments
         }

    return render(request, 'accounts/login.html', context=context)

            
        

        


