from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import AddGroupForm, UserprofileForm
from depart.models import Department, Project, Supervisor, Group, Progress
# Create your views here.
def homepage(request): 
    return render(request, 'home.html')

def departmentPage(request):
    departments= Department.objects.all()
    return render(request, 'department.html', {'departments' : departments})

def addDepartmentPage(request):

    return render(request, 'department.html') 

def adddepartmentformsubmission(request):
    departments = get_object_or_404(Department)
    if request.method == 'POST':
        department_name = request.POST["department_name"]
        hod_name = request.POST["hod_name"]
        hod_phone_number = request.POST["hod_phone_number"]
        hod_email = request.POST["hod_email"]

        departments = Department.objects.create(department_name=department_name, hod_name=hod_name, hod_phone_number=hod_phone_number, hod_email=hod_email)

    return render(request, 'department.html', {'departments': departments})

def department_details(request, pk=None):
    departments= Department.objects.get(pk=pk)
    projects = Project.objects.all()
    supervisors = Supervisor.objects.all()
    groups = Group.objects.all()
    context = {
        'departments': departments, 
        'projects':projects,
        'supervisors': supervisors,
        'groups': groups
        } 
    return render(request, 'is.html', context=context )


def create_group(request):
    if request.method == 'POST':
        form = AddGroupForm(request.POST)
    
        if form.is_valid():
            group = form.save(commit=False)
            group.save()
            print('CREATED')
            HttpResponseRedirect('department_details')
    else:
        form = AddGroupForm()
        print('NOT CREATED')
    return render(request, 'addgroup.html', {'form': form})

def userRegisterpage(request):
    if request.method == 'POST':
        form = UserprofileForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('department_details')
    else:
        form=UserprofileForm() 
    return render(request, 'students.html', {'form':form})

def singleGroup(request, pk):
    groups = Group.objects.get(pk=pk)
    projects = Project.objects.all()
    supervisors = Supervisor.objects.all()
    progress = Progress.objects.all()
    context = { 
        'projects':projects,
        'supervisors': supervisors,
        'groups': groups,
        'progress': progress
        }
       
    return render(request, 'group.html', context=context )






