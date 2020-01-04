from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from simple_forms.apps.core.models import Userprofile, Group
from .models import School, Department, Group, Files, Supervisor, Project, Member, ProjectStore
from accounts.models import UserProfile

# class UserprofileForm(UserCreationForm):
#     email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
#     # reg_number = forms.Integer(required=True, widget=forms.reg_numberInput())
#     # department_name = forms.CharField(max_length = 250, required=True)
    
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['school_name']

class AddDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields=['department_name','school']

class AddGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('department', 'group_name', 'group_email')


class FileForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ('sender', 'title', 'file')

class AddSupervisorForm(forms.ModelForm):    
    supervisor_name = UserProfile.role == 'S'
    class Meta:
        model = Supervisor
        fields = ('department_id', 'supervisor_name', 'group', 'supervisor_email')


class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('group_id', 'department', 'project_title', 'project_description')

class AddMemberForm(forms.ModelForm):
    class Meta:
        model=Member
        fields = ('reg_number', 'group', 'member_names',
                  'department_name', 'member_phone_number', 'member_email')

class AddToStoreForm(forms.ModelForm):
    class Meta:
        model = ProjectStore
        fields = ('project', 'description', 'technology',
                   'category', 'member_1', 'member_2', 'member_3', 'supervisor', 'marks', 'years', 'school', 'department', 'hosted_link')
