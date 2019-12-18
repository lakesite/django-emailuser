from django.contrib import admin
import django.contrib.auth.admin
from django.utils.translation import ugettext_lazy as _

from .forms import UserCreationForm, UserChangeForm
from .models import User


class UserAdmin(django.contrib.auth.admin.UserAdmin)):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User

    # list settings
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    search_fields = ('email',)
    ordering = ('email',)

    # detail settings
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'password1', 'password2')}),
    )


admin.site.register(User, UserAdmin)