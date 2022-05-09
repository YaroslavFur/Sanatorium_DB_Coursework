from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Employee, Patient, User


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('first_name', 'second_name', 'email', 'password', 'last_login')}),
        ('Permissions', {'fields': (
            'is_active', 
            'is_staff', 
            'is_superuser',
            'groups', 
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('first_name', 'second_name', 'email', 'password1', 'password2')
            }
        ),
    )

    list_display = ('first_name', 'second_name', 'email', 'is_staff', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, UserAdmin)
admin.site.register(Employee)
admin.site.register(Patient)