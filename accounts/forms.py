from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
 

class UserprofileForm(UserCreationForm):
    username = forms.IntegerField(required = True, label='Username', help_text="Here use student registration numbers")
    first_name = forms.CharField( max_length = 250, required=True, widget=forms.TextInput())
    last_name = forms.CharField( max_length = 250, required=True, widget=forms.TextInput())
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    


    
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already taken by other student")
        return username
    
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class StaffRegisterForm(UserCreationForm):
    username = forms.CharField(max_length = 50, required = True, label='Username')
    first_name = forms.CharField( max_length = 250, required=True, widget=forms.TextInput())
    last_name = forms.CharField( max_length = 250, required=True, widget=forms.TextInput())
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already taken by other staff")
        return username

    class Meta:
        model= User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UserLoginForm(forms.Form):
    # user=User.objects.filter(Role='student')
    # if user.Role=='student':
    #     username= forms.IntegerField()
    #     password=forms.CharField(widget=forms.PasswordInput)
    # else:
    username = forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')

        if username and password:
            user = authenticate(usernama=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not registered!')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password!')
        return super(UserLoginForm, self).clean(*args, **kwargs)

class ProfileForm(forms.ModelForm):
   
    class Meta:
        model=UserProfile
        fields = ['user', 'reg_number',
                  'phone_number', 'department_name', 'role']
    

