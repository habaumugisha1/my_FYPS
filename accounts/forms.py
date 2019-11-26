from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserprofileForm(UserCreationForm):
    first_name = forms.CharField( max_length = 250, required=True, widget=forms.TextInput())
    last_name = forms.CharField( max_length = 250, required=True, widget=forms.TextInput())
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    reg_number = forms.IntegerField(required=True, widget=forms.NumberInput())
    phone_number = forms.IntegerField(required=True, widget=forms.NumberInput())
    department_name = forms.CharField(max_length = 250, required=True, widget=forms.TextInput())
    
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','reg_number', 'phone_number', 'department_name', 'password1', 'password2']