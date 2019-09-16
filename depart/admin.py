from django.contrib import admin
from .models import Department, Supervisor, Group, Member,  Project
# Register your models here.
admin.site.register(Department)
admin.site.register(Supervisor)
admin.site.register(Group)
admin.site.register(Member)
admin.site.register(Project)