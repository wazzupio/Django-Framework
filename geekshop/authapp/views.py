from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from authapp.validators import validate_min_length
from baskets.models import Basket


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
            messages.warning(request, 'Пожалуйста, введите правильное имя пользователя и пароль.')
    else:
        form = UserLoginForm()

    context = {
        'title': 'geekshop - авторизация',
        'form': form,
    }
    return render(request, 'authapp/login.html', context)


def register(request):
    validate_min_length_errors = ''
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        validate_min_length_errors = validate_min_length(form)
        if validate_min_length_errors == '':
            if form.is_valid():
                form.save()
                messages.success(request, 'Вы успешно зарегистрировались')
                return HttpResponseRedirect(reverse('authapp:login'))
            else:
                messages.warning(request, form.errors['password2'])
        else:
            messages.warning(request, validate_min_length_errors)
    else:
        form = UserRegisterForm()

    context = {
        'title': 'geekshop - регистрация',
        'form': form,
        'validate_min_length_errors': validate_min_length_errors,
    }
    return render(request, 'authapp/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        validate_min_length_errors = validate_min_length(form)
        if validate_min_length_errors == '':
            form.save()
            messages.success(request, 'Профиль успешно отредактирован')
            return HttpResponseRedirect(reverse('authapp:profile'))
        else:
            messages.warning(request, validate_min_length_errors)

    context = {
        'title': 'geekshop - профиль',
        'form': UserProfileForm(instance=request.user),
        'baskets': Basket.objects.filter(user=request.user),
    }
    return render(request, 'authapp/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
