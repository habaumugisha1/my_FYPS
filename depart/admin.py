from django.contrib import admin
from .models import Department, Supervisor, Group, Member, Message, Project, Userprofile, Files
from import_export.admin import ImportExportModelAdmin
@admin.register(Department, Supervisor, Group, Member, Message, Project, Userprofile, Files)
class ViewAdmin(ImportExportModelAdmin):
    pass


# Register your models here.
# admin.site.register(Department)
# admin.site.register(Supervisor)
# admin.site.register(Group)
# admin.site.register(Member)
# admin.site.register(Project)

