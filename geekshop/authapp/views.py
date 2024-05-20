from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from authapp.forms import UserLoginForm, UserRegisterForm
from authapp.validators import validate_min_length


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors)
    else:
        form = UserLoginForm()

    context = {
        'title': 'geekshop - авторизация',
        'form': form,
    }
    return render(request, 'authapp/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        validate_min_length_errors = validate_min_length(form)
        if validate_min_length_errors == '':
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('authapp:login'))
            else:
                print(form.errors)
        else:
            print(validate_min_length_errors)
    else:
        form = UserRegisterForm()

    context = {
        'title': 'geekshop - регистрация',
        'form': form,
    }
    return render(request, 'authapp/register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
