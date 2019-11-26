"""FYP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views

from depart import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('departments/', views.departmentPage, name='departments'),
    path('departments/<int:pk>/', views.department_details, name='department_details'),
    path('addSupervisor/', views.addSupervisor, name='addsupervisor'),
    path('addProject/', views.addProject, name='addProject'),
    path('group/<int:pk>/', views.singleGroup, name='single_group'),
    path('group/<int:pk>/upload/', views.upload_file, name='upload_file'),
    path('group/<int:pk>/files/', views.file_list, name='file_list'),
    path('add_group/', views.create_group, name='add_group'),
    path('student_register/', accounts_views.userRegisterpage, name='register_students'),
    #path('login/', accounts_views.login, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_department/', views.addDepartmentPage, name='add_departments'),
    path('add_department_form_submission/', views.adddepartmentformsubmission, name='add_department_form_submission'),
 
    path('admin/', admin.site.urls),
]
