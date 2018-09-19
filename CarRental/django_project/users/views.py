from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, EmployeeRegisterForm


# Create your views here.
def register(request):

    if request.method == 'POST':
        form = EmployeeRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = user.userprofile
            employee_id = form.cleaned_data.get('employee_id')
            user_group = form.cleaned_data.get('user_type')
            profile.user_type = user_group
            profile.employee_id = employee_id
            profile.save()
            #form.save()
            username = form.cleaned_data.get('username')
            user_group = form.cleaned_data.get('user_type')
            employee_id = form.cleaned_data.get('employee_id')
            messages.success(request, f'Account has been created. Log In now!')
            return redirect('login')
    else:
        form = EmployeeRegisterForm()
    return render(request, 'users/register.html', {'form':form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Profile has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context ={
        'u_form': u_form
    }
    return render(request, 'users/profile.html', context)
