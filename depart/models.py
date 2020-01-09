from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
#from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class School(models.Model):
    school_name = models.CharField(max_length=450)

    def __str__(self):
        return self.school_name


class Department(models.Model):
    department_name = models.CharField(max_length=100)
    school = models.ForeignKey(School, related_name='department', on_delete=models.CASCADE)

    def __str__(self):
        return self.department_name


class Supervisor(models.Model):
    department_id = models.ForeignKey(Department, related_name = 'supervisors', on_delete = models.CASCADE)
    supervisor_name = models.CharField(max_length=250, null=True)
    supervisor_email = models.EmailField(max_length=250)

    def __str__(self):
        return self.supervisor_name

class Group(models.Model):
    department = models.ForeignKey(Department, related_name='group', on_delete = models.CASCADE)
    group_name = models.CharField(max_length=50)
    supervisor = models.ForeignKey(Supervisor, related_name='group', on_delete=models.CASCADE)
    group_email = models.EmailField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.group_name
        # 'Group: {} {} {} {}'.format(self.department, self.supervisor, self.group_name, self.group_email)


class Member(models.Model):
    reg_number = models.IntegerField()
    group = models.ForeignKey(Group, related_name='member', on_delete = models.CASCADE)
    member_names = models.CharField(max_length=250)
    department_name = models.ForeignKey(Department, related_name='member', on_delete = models.CASCADE)
    member_phone_number = models.IntegerField()
    member_email = models.EmailField(max_length=250)

    def __str__(self):
        return self.member_names


# members = Group.objects.get(id=id).member_set.all()


class Project(models.Model):
    group_id = models.ForeignKey(Group, related_name='project', on_delete = models.CASCADE)
    department = models.ForeignKey(Department, related_name='project', on_delete=models.CASCADE)
    project_title = models.CharField(max_length=500)
    project_description = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_titletext


class Files(models.Model):
    # message_id = models.ForeignKey(Message, related_name='file', on_delete = models.CASCADE, default=1)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='file', on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='files/', null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Progress(models.Model):
    file_id = models.ForeignKey(Files, related_name='progress', on_delete = models.CASCADE)
    session_percentage = models.IntegerField()



class ProjectStore(models.Model):
    project = models.CharField(max_length=250)
    description = models.FileField(upload_to='store/', null=False)
    technology = models.CharField(max_length=250)
    category = models.CharField(max_length=100)
    member_1 = models.CharField(max_length=100)
    member_2 = models.CharField(max_length=100)
    member_3 = models.CharField(max_length=100)
    supervisor = models.ForeignKey(Supervisor, related_name='projectstore', on_delete=models.CASCADE)
    marks = models.CharField(max_length=50)
    years = models.CharField(max_length=50)
    school = models.ForeignKey(School, related_name='projectstore', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, related_name='projectstore', on_delete=models.CASCADE)
    hosted_link = models.URLField(max_length=128, unique=True, blank=True)
    stored_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project

class Comments(models.Model):
    project = models.ForeignKey(ProjectStore, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField()
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    commented_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


