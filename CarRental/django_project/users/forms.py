from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

#
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#User Profile update form
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

#Employee Register Form
class EmployeeRegisterForm(UserCreationForm):
    email = forms.EmailField()
    employee_id = forms.CharField()
    user_states = (('New South Wales','New South Wales'), ('Queensland', 'Queensland'),('South Australia', 'South Australia'), ('Victoria', 'Victoria'), ('Tasmania', 'Tasmania'))
    user_state = forms.ChoiceField(choices = user_states)
    class Meta:
        model = User
        fields = ['username', 'email', 'employee_id', 'password1', 'password2', 'user_state']

    def save(self, commit=True):
        user = super(EmployeeRegisterForm, self).save(commit=False)
        user.employee_id = self.cleaned_data["employee_id"]
        if commit:
            user.save()
        return user

#Customer Register Form
class CustomerRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

    def save(self, commit=True):
        user = super(CustomerRegisterForm, self).save(commit=False)
        if commit:
            user.save()
        return user

#Manager Register Form
class ManagerRegisterForm(UserCreationForm):
    email = forms.EmailField()
    employee_id = forms.CharField()
    user_states = (('New South Wales','New South Wales'), ('Queensland', 'Queensland'),('South Australia', 'South Australia'), ('Victoria', 'Victoria'), ('Tasmania', 'Tasmania'))
    user_state = forms.ChoiceField(choices = user_states)
    class Meta:
        model = User
        fields = ['username', 'email', 'employee_id', 'password1', 'password2', 'user_state']

    def save(self, commit=True):
        user = super(ManagerRegisterForm, self).save(commit=False)
        user.employee_id = self.cleaned_data["employee_id"]
        if commit:
            user.save()
        return user
