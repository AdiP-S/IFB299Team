from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class EmployeeRegisterForm(UserCreationForm):
    email = forms.EmailField()
    employee_id = forms.CharField()
    user_types = (('Customer', 'Customer'), ('Employee', 'Employee'), ('Manager', 'Manager'))

    user_type = forms.ChoiceField(choices = user_types)

    class Meta:
        model = User
        fields = ['username', 'email', 'employee_id', 'password1', 'password2', 'user_type']

    def save(self, commit=True):
        user = super(EmployeeRegisterForm, self).save(commit=False)
        user.employee_id = self.cleaned_data["employee_id"]
        if commit:
            user.save()
        return user

class ManagerRegisterForm(UserCreationForm):
    email = forms.EmailField()
    managerid = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'managerid', 'password1', 'password2']
