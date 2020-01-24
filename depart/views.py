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
from depart.forms import AddGroupForm, FileForm, AddDepartmentForm, AddMemberForm, AddSupervisorForm, AddProjectForm, SchoolForm, AddToStoreForm, AddCommentForm
from django.core.files.storage import FileSystemStorage
from accounts.models import UserProfile
from depart.models import School, Department, Project, Supervisor, Group, Member, Progress, Files, ProjectStore, Comments
# Create your views here.
def homepage(request):
    user = User.objects.all() 
    return render(request, 'home.html', {'user':user})


def schools(request):
    count = School.objects.count()
    schools = School.objects.all()
    return render(request, 'school.html', {'schools': schools, 'count': count})

def school_detail(request, pk, *args, **kwargs):
    group = Group.objects.get(pk=pk)
    groups = Group.objects.all()
    user = User.objects.get(pk=pk)
    member = Member.objects.get(pk=pk)
    members = Member.objects.all()
    count = Department.objects.filter(school=pk).count()
    departments = Department.objects.filter(school=pk)
    department = Department.objects.get(pk=pk)
    school = School.objects.get(pk=pk)
    if request.user.profile.role == 'student':
        for department in departments:
            if request.user.profile.department_name == department:
                if group in groups:
                    if member.group==group:
                        # if request.user.is_authenticated == member.reg_number:
                        return redirect('all_groups', department.pk)
                        # else:
                        #     return HttpResponse("<h1 style='color=red;'>user name is not the same as your reg number </h1>")
                    else:
                        return HttpResponse("<h1 style='color=red;'>You are not a member of any group</h1>")

                else:
                    return HttpResponse("<h1 style='color=red;'>You don't have <b>Group</b>. Please contact your HOD.</h1>")
            else:
                return HttpResponse("<h1 style='color=red;'>This is not your <b>Department</b></h1>")
        
    elif request.user.profile.role == 'HOD':
        if request.user.profile.department_name == department:
            return redirect('department_details', pk=department.pk)
        else:
            return HttpResponse("<h1 style='color=red;'>This is not your <b>Department</b></h1>")
    elif request.user.profile.role == 'supervisor':
        for department in departments:
            if request.user.profile.department_name == department:
                return redirect('supervisor_dashboard', pk=department.pk)
            else:
                return HttpResponse("<h1 style='color=red;'>Kindly, Your department is not in this school you are trying to access</h1>")
    elif request.user.profile.role == 'dean':
        if school:
            pass
        else:
            return HttpResponse("<h1 style='color=red;'>Kindly, This is not your <b>school</b></h1>")


    context = {
        'school':school,
        'count':count,
        'member':member,
        'departments':departments
         }

    return render(request, 'school_detail.html', context )

def addschool(request):
    user = User.objects.all()
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

    return render(request, 'addschool.html', {'form': form, 'user':user})


def departmentPage(request):
    departments= Department.objects.all()
    count = Department.objects.count()
    return render(request, 'department.html', {'departments' : departments, 'count':count})

# def addDepartmentPage(request):

#     return render(request, 'department.html') 

def adddepartment(request):
    user = User.objects.all()
    # school= School.objects.get(pk=pk)
    if request.method == 'POST':
        form = AddDepartmentForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Department successful created')
        return HttpResponseRedirect(reverse('school'))
    else:
        form = AddDepartmentForm()

    return render(request, 'add_department.html', {'form': form, 'user':user})

def add_member(request):
    user = User.objects.all()
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

    return render(request, 'addmember.html', {'form':form, 'user':user})



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

def group(request, pk, *args, **kwargs):
    departments = Department.objects.filter(school=pk)
    groups = Group.objects.filter(department=pk)
    group = Group.objects.get(pk=pk)
    members = Member.objects.filter(group=pk)
    # if request.user.profile.department_name == members.reg_number:
    #     print(members.group)
    # else:
    #     print('bad request!!')
    
    # print(members.group)

    return render(request, 'allgroups.html', {'groups':groups, 'departments':departments})

def singleGroup(request, pk, *args, **kwargs):
    group = Group.objects.get(pk=pk)
    projects = Project.objects.filter(group_id=pk)
    supervisors = Supervisor.objects.filter(group=pk)
    members = Member.objects.filter(group=pk)
    member = Member.objects.get(pk=pk)
    progress = Progress.objects.all()
    if request.user.profile.role== 'student':
        if request.user.profile.reg_number == member.reg_number:
            pass
            print('next!')
        else:
            print('not allowed')
            return HttpResponse("<h1 style='color=red;'>kindly access only your group </h1>")

    else:
        pass
    
    # print(member.reg_number)
        # if member in members:
        # if member.reg_number==request.user.username:
        #     return redirect('single_group', pk=group.pk)           
        # else:
        #     print(member.reg_number)
        #     print(request.user.username)
        #     return HttpResponse("<h1 style='color=red;'>user name is not the same as your reg number </h1>")
        # else:
        #     return HttpResponse("<h1 style='color=red;'>You are not a member </h1>")

    context = {
        'projects': projects,
        'supervisors': supervisors,
        'group': group,
        'members': members,
        'progress': progress
    }
    return render(request, 'group.html', context=context)

def addSupervisors(request):
    if request.user.profile.role == 'HOD':
        # department = Department.objects.get(pk=pk)
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

    return render(request, 'addsup.html', {'form': form})

def addProject(request):
    if request.user.profile.role == 'HOD':
        if request.method == 'POST':
            form = AddProjectForm(request.POST, request.FILES)
            # form.owner = request.user
            if form.is_valid():
                form.save()
                messages.success(request, 'Project successful added to group')
                return HttpResponseRedirect(reverse('school'))
            
        else:
            form =AddProjectForm()
    else:
        # form =AddSupervisorForm()
        return HttpResponse("<h1>You are not allowed to access this resource</h1>")
    
    return render(request, 'addproject.html', {'form':form})


@login_required()
def dashboard(request, pk, *args, **kwargs):
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

    
def supervisor_dash(request, pk, *args, **kwargs):
    supervisors = Supervisor.objects.filter(department_id=pk)
    for supervisor in supervisors:        
        supervisor = Supervisor.objects.get(pk=pk)

    projects = Project.objects.filter(group_id=pk) 
    groups = Group.objects.filter(supervisor=supervisor)
    print(supervisor)
    context={
     'groups':groups,
     'projects':projects,
     'supervisors': supervisors

    }
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

    supervisors = UserProfile.objects.filter(role='supervisor')
    supcount = UserProfile.objects.filter(role='supervisor').count()
    context={
        'departments':departments,
        'depcount':depcount,
        'schools': schools,
        'count': count,
        'supervisors':supervisors,
        'supcount': supcount

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

def project_store(request):
    stores = ProjectStore.objects.all()
    context= {
        'stores':stores
    }
    return render(request, 'project_store.html', context=context)

def single_project_store(request, pk):
    store = ProjectStore.objects.get(pk=pk)
    comments= Comments.objects.filter(project=pk)
    commentscount =Comments.objects.filter(project=pk).count()
    context= {
        'store':store,
        'comments':comments,
        'commentscount': commentscount
    }
    return render(request, 'single_project_store.html', context=context)

@login_required
def comment(request, pk):
    store = ProjectStore.objects.get(pk=pk)
    if request.method =='POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('single_project_store', pk=store.pk)
    else:
        form = AddCommentForm()
    context = {
        'store': store,
        'form':form
    }
    return render(request, 'comment.html', context=context)

