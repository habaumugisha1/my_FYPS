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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from accounts.views import login, profilepage, LoginView

from depart import views

urlpatterns = [   
    path('', views.homepage, name='home'),
    path('chat/', include('chat.urls', namespace='chat')),
    path('profile/', accounts_views.profilepage, name='profile'),
    # path('accounts/', include('accounts.urls', namespace='accounts')),
    path('departments/', views.departmentPage, name='departments'),
    path('departments/<int:pk>/', views.department_details, name='department_details'),
    path('addSupervisor/', views.addSupervisors, name='addsupervisor'),
    path('addProject/', views.addProject, name='addProject'),
    path('departments/<int:pk>/group/', views.group, name='all_groups'),
    path('group/<int:pk>/', views.singleGroup, name='single_group'),
    path('group/<int:pk>/upload/', views.upload_file, name='upload_file'),
    path('group/<int:pk>/files/', views.file_list, name='file_list'),
    path('add_group/', views.create_group, name='add_group'),
    path('student_register/', accounts_views.userRegisterpage, name='register_students'),
    path('staff_register/', accounts_views.staffRegister, name='register_staff'),
    path('login/', accounts_views.LoginView, name='login'),
    #path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('account/login/', loginPage, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('departments/<int:pk>/supervisor_dashboard/', views.supervisor_dash, name='supervisor_dashboard'),
    path('cordinator_dashboard/', views.cordinator_dash, name='cordinator_dashboard'),
    path('lectucturor_dashboard/', views.lectucturor_dash, name='lectucturor_dashboard'),
    path('principle_dashboard/', views.principle_dash, name='principle_dashboard'),
    path('add_department/', views.adddepartment, name='add_departments'),
    path('add_member/', views.add_member, name='add_membert'),
    #path('add_department_form_submission/', views.adddepartmentformsubmission, name='add_department_form_submission'),
    path('school/', views.schools, name='school'),
    path('school/<int:pk>/', views.school_detail, name='single_school'),
    path('addschool/', views.addschool, name='addschool'),
    path('create_project_store/', views.add_project_in_store, name='create_project_store'),
    path('project_in_store/', views.project_store, name='project_in_store'),
    path('single_project_store/<int:pk>/', views.single_project_store, name='single_project_store'),
    path('single_project_store/<int:pk>/comment',
         views.comment, name='comment'),

    path('reset/',
         auth_views.PasswordResetView.as_view(
             template_name='registration/password_reset.html',
             email_template_name='registration/password_reset_email.html',
             subject_template_name='registration/password_reset_subject.txt'
         ),
         name='password_reset'),

    path('reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'),
         name='password_reset_done'),

    path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
 
    path('admin/', admin.site.urls),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
