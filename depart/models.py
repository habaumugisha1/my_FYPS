from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=100)
    hod_name = models.CharField(max_length=80)
    hod_phone_number = models.IntegerField()
    hod_email = models.CharField(max_length=250)

    def __str__(self):
        return self.department_name

class Supervisor(models.Model):
    department_id = models.ForeignKey(Department, related_name = 'supervisors', on_delete = models.CASCADE)
    supervisor_name = models.CharField(max_length=100)
    supervisor_email = models.CharField(max_length=250)

    def __str__(self):
        return self.supervisor_name

class Group(models.Model):
    department_id = models.ForeignKey(Department, related_name='group', on_delete = models.CASCADE)
    supervisor_id = models.ForeignKey(Supervisor, related_name='group', on_delete = models.CASCADE)
    group_name = models.CharField(max_length=50)
    group_email = models.CharField(max_length=250)

    def __str__(self):
        return self.group_name

class Member(models.Model):
    reg_number = models.IntegerField(unique=True)
    group_id = models.ForeignKey(Group, related_name='member', on_delete = models.CASCADE)
    member_name = models.ForeignKey(User, related_name='member', on_delete = models.CASCADE)
    department_name = models.ForeignKey(Department, related_name='member', on_delete = models.CASCADE)
    member_phone_number = models.IntegerField()
    member_email = models.CharField(max_length=250)

    def __str__(self):
        return self.member_name

class Project(models.Model):
    group_id = models.ForeignKey(Group, related_name='project', on_delete = models.CASCADE)
    project_title = models.CharField(max_length=500)
    project_description = models.CharField(max_length=200)

    def __str__(self):
        return self.project_title

class Message(models.Model):
    message_content = models.CharField(max_length=300)


class Files(models.Model):
    message_id: models.ForeignKey(Message, related_name='file', on_delete = models.CASCADE)
    file_name = models.CharField(max_length=200)

class Progress(models.Model):
    file_id = models.ForeignKey(Files, related_name='progress', on_delete = models.CASCADE)
    session_percentage = models.IntegerField()




