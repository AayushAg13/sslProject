from django import forms
from django.contrib.auth.models import User
from .models import *
from .constants import * #LOGIN_SERVER, ROLES
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['name', 'webmail', 'department', 'hostel']


class FacultyForm(forms.ModelForm):

    class Meta:
        model = Faculty
        fields = ['webmail', 'department','name']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Webmail')
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    login_server = forms.ChoiceField(required=True, choices=LOGIN_SERVER)
    role = forms.ChoiceField(required=True, choices=ROLES)

    def clean_role(self):
        valid_roles = [
       "Student", "Faculty", "Lab", "Caretaker", "Warden", "Gymkhana", "OnlineCC", "CC", "Thesis Manager", "Library", "Assistant Registrar", "HOD", "Account", "Admin"
        ]
        role = self.cleaned_data.get('role')
        if role not in valid_roles:
            raise  ValidationError(_('Invalid Role'), code='invalid')
        return role

    def clean_login_server(self):
        valid_servers = ['202.141.80.9', '202.141.80.10', '202.141.80.11',
                         '202.141.80.12', '202.141.80.13']
        login_server = self.cleaned_data.get('login_server')
        if login_server not in valid_servers:
            raise ValidationError(_('Invalid Login Server'), code='invalid')
        return login_server
