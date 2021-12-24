from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'user_birthday', 'is_superuser')
    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2', 'email', 'user_birthday')
        }),)


# Register your models here.

admin.site.register(CustomUser, CustomUserAdmin)
