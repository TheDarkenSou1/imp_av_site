from django.shortcuts import render, redirect
from .forms import RegistrationUserForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    """
    This function provides user to login on the site.

    :param request: request
    :return: login on the site if form is valid.
    """
    form = UserLoginForm(request.POST or None)
    next_get = request.GET.get('next')
    if form.is_valid():
        password = form.cleaned_data['password']
        username = form.cleaned_data['username']

        user = authenticate(username=username, password=password)
        login(request, user)

        next_post = request.POST.get('next')

        return redirect(next_get or next_post or '/')
    return render(request, 'login.html', context={'form': form})


def registration_view(request):
    """
    This function provides user to register on the site.

    :param request: request
    :return: registeration done if form is valid or return to registration form to refill it.
    """
    form = RegistrationUserForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()

        return render(request, 'registration_done.html', context={'user': new_user})
    return render(request, 'registration.html', context={'form': form})


def logout_view(request):
    """
    This function is used to logout user and redirect him to the main page.

    :param request: request.
    :return: redirecting user to the main page.
    """
    logout(request)
    return redirect('/')
