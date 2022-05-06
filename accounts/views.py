from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from .forms import RegistrationForm, UserEditForm
from .tokens import account_activation_token
from .models import Profile
from django.http import JsonResponse
from django.contrib.auth import login

# Create your views here.


@login_required
def edit(request):
    if request.method == 'POST':

        user_form = UserEditForm(instance=request.user ,data=request.POST)
        profile_form = UserProfileForm(
            request.POST, request.FILES, instance=request.user.profile)

        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.profile)

    return render(request,
                  'accounts/update.html',
                  {'user_form': user_form, 'profile_form': profile_form})


@login_required
def delete_user(request):

    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        user.is_active = False
        user.save()
        return redirect('accounts:login')

    return render(request, 'accounts/delete.html')



def accounts_register(request):
    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            request_context = RequestContext(request)
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = True
            user.save()
            return activate(request_context,user)

    else:
        registerForm = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': registerForm})


def activate(request, user):
    try:
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('login')
    except:
        return redirect('login')
