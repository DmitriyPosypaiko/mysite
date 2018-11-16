from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms



class Profile(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name','last_name','email')
    def equal(self,object):
        pass
