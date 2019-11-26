from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from simple_forms.apps.core.models import Userprofile, Group
from .models import Userprofile, Group, Files, Supervisor, Project, Member

class UserprofileForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    # reg_number = forms.Integer(required=True, widget=forms.reg_numberInput())
    # department_name = forms.CharField(max_length = 250, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AddGroupForm(forms.ModelForm):
    email = forms.CharField( max_length=250)
    class Meta:
        model = Group
        fields = ['department_id', 'supervisor_id', 'group_name', 'group_email']


class FileForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ('message_id', 'file_name', 'file' )

class AddSupervisorForm(forms.ModelForm):
    class Meta:
        model = Supervisor
        fields = ('department_id', 'supervisor_name', 'supervisor_email')


class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('group_id', 'project_title', 'project_description') 
