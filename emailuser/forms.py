import django.contrib.auth.forms
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class UserCreationForm(django.contrib.auth.forms.UserCreationForm):

    class Meta(django.contrib.auth.forms.UserCreationForm):

        model = User
        fields = ('email',)


class UserChangeForm(django.contrib.auth.forms.UserChangeForm):

    class Meta:
        
        model = User
        fields = ('email',)

