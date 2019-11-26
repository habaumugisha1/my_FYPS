from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from .forms import UserprofileForm


# Create your views here.
def userRegisterpage(request):
    form = UserprofileForm()
    if request.method == 'POST':
        form = UserprofileForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auth_login(request, user)
            return HttpResponseRedirect (reverse('home'))
            # return redirect('single_group')
    else:
        form = UserprofileForm()
    return render(request, 'accounts/students.html', {'form':form})


# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = auth.authenticate(username=username, password=password)

#         if user is not None:
#             auth.login(request, user)
#             messages.success(request,'You are loged In now')
#             return redirect('home')
#         else:
#             messages.error(request, 'Invalid credentials, Try again')
#         return redirect('login')

#     else:
#         return render(request, 'accounts/login.html')