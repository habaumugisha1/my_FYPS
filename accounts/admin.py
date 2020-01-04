from django.contrib import admin
from accounts.models import UserProfile

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('reg_number', 'phone_number', 'department_name', 'role')


admin.site.register(UserProfile, UserAdmin)
