from django import forms
# from simple_forms.apps.core.models import Userprofile, Group
from .models import Userprofile, Group

class UserprofileForm(forms.ModelForm):

    class Meta:
        model = Userprofile
        fields = ['reg_number', 'user_names', 'department_name']


class AddGroupForm(forms.ModelForm):
    email = forms.CharField( max_length=250)
    class Meta:
        model = Group
        fields = ['department_id', 'supervisor_id', 'group_name', 'group_email']
