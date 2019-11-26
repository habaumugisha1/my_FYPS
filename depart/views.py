from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import AddGroupForm, FileForm, AddSupervisorForm, AddProjectForm 
from django.core.files.storage import FileSystemStorage
from depart.models import Department, Project, Supervisor, Group, Progress, Files
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

def upload_file(request, pk):
    groups = Group.objects.get(pk=pk)
    if request.method == 'POST':
      form = FileForm(request.POST, request.FILES)
      if form.is_valid():
          form.save()
        #   return redirect(reverse('single_group'))
    else:
        form =FileForm()
    return render(request, 'upload_file.html', {'form': form, 'groups':groups})

def file_list(request, pk):
    groups = Group.objects.get(pk=pk)
    files = Files.objects.all()
    return render(request, 'file.html', {'files': files})

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

def addSupervisor (request):
    # departments= Department.objects.get(pk=pk,)
    if request.method == 'POST':
      form = AddSupervisorForm(request.POST)
      if form.is_valid():
          form.save()
        
    else:
        form =AddSupervisorForm()
    return render(request, 'addsup.html', {'form':form})

def addProject(request):
    if request.method == 'POST':
      form = AddProjectForm(request.POST)
      if form.is_valid():
          form.save()
        
    else:
        form =AddProjectForm()
    return render(request, 'addproject.html', {'form':form})

def dashboard(request):
    files = Files.objects.all()
    projects = Project.objects.all()
    supervisors = Supervisor.objects.all()
    groups = Group.objects.all()
    context = {
        'files':files,
        'projects':projects,
        'supervisors': supervisors,
        'groups': groups
        }
    return render(request, 'dashboard.html', context=context)






