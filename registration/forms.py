from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from registration.models import Extended_User

class Edit_SettingsForm(forms.ModelForm):

    class Meta:
        model = Extended_User
        fields = ("notifications","first_name","last_name","email",)

