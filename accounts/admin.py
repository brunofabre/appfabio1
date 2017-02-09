from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import Team, UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Team)
