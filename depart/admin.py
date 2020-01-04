from django.contrib import admin
from .models import School, Department, Supervisor, Group, Member, Project, Files, ProjectStore
from import_export.admin import ImportExportModelAdmin
@admin.register(School, Department, Supervisor, Group, Project, Files, ProjectStore)
class ViewAdmin(ImportExportModelAdmin):
    pass


class UserAdmin(admin.ModelAdmin):
    list_display = ('reg_number', 'group', 'member_names',
                    'department_name', 'member_phone_number', 'member_email')


admin.site.register(Member, UserAdmin)

# Register your models here.
# admin.site.register(Department)
# admin.site.register(Supervisor)
# admin.site.register(Group)
# admin.site.register(Member)
# admin.site.register(Project)

