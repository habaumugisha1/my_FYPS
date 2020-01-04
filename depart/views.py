import os
from django.conf import settings
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Files 
from depart.forms import AddGroupForm, FileForm, AddDepartmentForm, AddMemberForm, AddSupervisorForm, AddProjectForm, SchoolForm, AddToStoreForm
from django.core.files.storage import FileSystemStorage
from accounts.models import UserProfile
from depart.models import School, Department, Project, Supervisor, Group, Member, Progress, Files, ProjectStore
# Create your views here.
def homepage(request): 
    return render(request, 'home.html')


def schools(request):
    count = School.objects.count()
    schools = School.objects.all()
    return render(request, 'school.html', {'schools': schools, 'count': count})

def school_detail(request, pk, *args, **kwargs):
    group = Group.objects.get(pk=pk)
    count = Department.objects.filter(school=pk).count()
    departments = Department.objects.filter(school=pk)
    if request.user.profile.role == 'student':
        # return HttpResponseRedirect(reverse('single_group'))
        return redirect('single_group', pk=group.pk)
    # elif request.user.profile.role == 'HOD':
    #     return redirect('epartment_details', departments.pk)


    school = School.objects.get(pk=pk)
    context = {
        'school':school,
        'count':count,
        'departments':departments
         }

    return render(request, 'school_detail.html', context )

def addschool(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        user = User.objects.first()
        if form.is_valid():
            school = form.save(commit=False)
            user=user
            school.save()
            messages.success(request, 'School has been successful created.')
            return HttpResponseRedirect(reverse('school'))
    else:
      form = SchoolForm(initial = {})

    return render(request, 'addschool.html', {'form': form})


def departmentPage(request):
    departments= Department.objects.all()
    count = Department.objects.count()
    return render(request, 'department.html', {'departments' : departments, 'count':count})

# def addDepartmentPage(request):

#     return render(request, 'department.html') 

def adddepartment(request):
    # school= School.objects.get(pk=pk)
    if request.method == 'POST':
        form = AddDepartmentForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Department successful created')
        return HttpResponseRedirect(reverse('school'))
    else:
        form = AddDepartmentForm()

    return render(request, 'add_department.html', {'form': form})

def add_member(request):
    if request.user.profile.role =='HOD':
        if request.method =='POST':
            form = AddMemberForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Member successful added to group')

        else:
            form = AddMemberForm()
    else:
        return HttpResponse("<h1 style='color=red;'>You are not allowed to to add members. so, turn back</h1>")

    return render(request, 'addmember.html', {'form':form})



def department_details(request, pk=None, *args, **kwargs):
    departments= Department.objects.get(pk=pk)
    projects = Project.objects.filter(department=pk)
    countpro = Project.objects.filter(department=pk).count()
    supervisors = Supervisor.objects.filter(department_id=pk)
    countsup = Supervisor.objects.filter(department_id=pk).count()
    groups = Group.objects.filter(department=pk)
    countgro = Group.objects.filter(department=pk).count()
    context = {
        'departments': departments, 
        'projects':projects,
        'supervisors': supervisors,
        'groups': groups,
        'countsup': countsup,
        'countgro': countgro,
        'countpro':countpro
        } 
    return render(request, 'is.html', context=context )


def upload_file(request, pk, *args, **kwargs):
    group = Group.objects.get(pk=pk)
    if request.method == 'POST':
      form = FileForm(request.POST, request.FILES)
      if form.is_valid():
        #   group = form.save(commit=False)
          form.save()
          return redirect('file_list', pk=group.pk)
    else:
        form =FileForm()
    
    context={
        'form': form,
        'group': group
    }
    return render(request, 'upload_file.html', context=context)

def file_list(request, pk):
    groups = Group.objects.get(pk=pk)
    files = Files.objects.all()
    return render(request, 'file.html', {'files': files, 'groups':groups})

def create_group(request):   
    if request.user.profile.role == 'HOD':
        if request.method == 'POST':
            form = AddGroupForm(request.POST)
            if form.is_valid():
                # group = form.save(commit=False)
                form.save()
                messages.success(request, 'Group createed successful')
                return HttpResponseRedirect(reverse('add_membert'))
        else:
            messages.error(request, 'Group not created please try again')
            form = AddGroupForm()
            print('NOT CREATED')
    else:
        return HttpResponse("<h1 style='color=red;'>You are not allowed to create Group. so, turn back</h1>") 

    return render(request, 'addgroup.html', {'form':form})


def singleGroup(request, pk, *args, **kwargs):
    group = Group.objects.get(pk=pk)
    projects = Project.objects.filter(group_id=pk)
    supervisors = Supervisor.objects.filter(group=pk)
    members = Member.objects.filter(group=pk)
    progress = Progress.objects.all()
    context = { 
        'projects':projects,
        'supervisors': supervisors,
        'group': group,
        'members':members,
        'progress': progress
        }
       
    return render(request, 'group.html', context=context)

def addSupervisors(request, pk, *args, **kwargs):
    if request.user.profile.role == 'HOD':
        department = Department.objects.get(pk=pk)
        if request.method == 'POST':
            form = AddSupervisorForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'supervisor successful created')
                return HttpResponseRedirect(reverse('school'))
        else:
            form = AddSupervisorForm()
        
    else:
        # departments/<int: pk > /
        # form =AddSupervisorForm()
        return HttpResponse("<h1>You are not allowed to access this resource</h1>")

    return render(request, 'addsup.html', {'form': form, 'department': department})

def addProject(request):
    if request.user.profile.role == 'HOD':
        if request.method == 'POST':
            form = AddProjectForm(request.POST, request.FILES)
            # form.owner = request.user
            if form.is_valid():
                form.save()
                messages.success(request, 'Project successful added to group')
                return HttpResponseRedirect(reverse('departments'))
            
        else:
            form =AddProjectForm()
    else:
        # form =AddSupervisorForm()
        return HttpResponse("<h1>You are not allowed to access this resource</h1>")
    
    return render(request, 'addproject.html', {'form':form})


@login_required()
def dashboard(request, *args, **kwargs):
    if request.user.profile.role=='student':
        count = School.objects.count()
        schools = School.objects.all()
        departments = Department.objects.all()
        depcount = Department.objects.count()
        members = Member.objects.select_related('group')
        files = Files.objects.all()
        projects = Project.objects.all()
        rols = UserProfile.objects.filter(role='supervisor')
        data = {'user': request.user}
        supervisors = Supervisor.objects.select_related('group')
        groups = Group.objects.all()
        context = {
            'schools': schools,
            'count': count,
            'departments': departments,
            'depcount': depcount,
            'files': files,
            'projects': projects,
            'members':members,
            'rols': rols,
            'data': data,
            'supervisors': supervisors,
            'groups': groups
        }
    else:
        return HttpResponse("<h1 style='color=red;'>You are not allowed to access this resource</h1>")
    return render(request, 'dashboard.html', context=context)

def supervisor_dash(request):
    context={}
    return render(request, 'dashboard/sup_dash.html', context=context)

def cordinator_dash(request):
    stores = ProjectStore.objects.all()
    context = {'stores': stores}
    return render(request, 'dashboard/cord_dash.html', context=context)

def lectucturor_dash(request):
    stores = ProjectStore.objects.all()
    context={'stores':stores}
    return render(request, 'dashboard/lecture_dash.html', context=context)

def principle_dash(request):
    count = School.objects.count()
    schools = School.objects.all()
    departments = Department.objects.all()
    depcount = Department.objects.count()
    context={
        'departments':departments,
        'depcount':depcount,
        'schools': schools,
        'count': count

    }
    return render(request, 'dashboard/principle_dash.html', context=context)

def add_project_in_store (request):
    if request.user.profile.role == 'HOD':
        if request.method == 'POST':
            form = AddToStoreForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        else:
            form =AddToStoreForm()
    else:
        return HttpResponse("<h1 style='color=red;'>You are not allowed to access this resource</h1>")
    context= {
        'form':form
    }
    return render (request, 'createstore.html', context=context)







