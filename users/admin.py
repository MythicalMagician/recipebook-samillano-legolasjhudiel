# users/admin.py
""""""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile


class ProfileInLine(admin.StackedInLine):
    """"""
    model = Profile
    can_delete = False


class UserAdmin(admin.BaseUserAdmin):
    """"""
    inlines = [ProfileInLine,]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
