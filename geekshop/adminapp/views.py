from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoriesAdminProfileForm, \
    CategoriesAdminRegisterForm, ProductsAdminRegisterForm, ProductAdminProfileForm
from authapp.models import User
from authapp.validators import validate_min_length
from mainapp.models import ProductCategory, Product


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    context = {
        'title': 'GeekShop - Admin',
        'copyright': 'Copyright © GeekShop 2024'
    }
    return render(request, 'adminapp/admin.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_read(request):
    context = {
        'users': User.objects.all(),
        'title': 'GeekShop - Пользователи',
        'copyright': 'Copyright © GeekShop 2024'
    }
    return render(request, 'adminapp/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        validate_min_length_errors = validate_min_length(form)
        if validate_min_length_errors == '':
            if form.is_valid():
                form.save()
                messages.success(request, 'Пользователь успешно создан')
                return HttpResponseRedirect(reverse('adminapp:admin_users_read'))
            else:
                messages.warning(request, form.errors['password2'])
        else:
            messages.warning(request, validate_min_length_errors)
    else:
        form = UserAdminRegisterForm()

    context = {
        'form': form,
        'title': 'GeekShop - Создание пользователя',
        'copyright': 'Copyright © GeekShop 2024',
    }
    return render(request, 'adminapp/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, instance=user, files=request.FILES)
        validate_min_length_errors = validate_min_length(form)
        if validate_min_length_errors == '':
            form.save()
            messages.success(request, 'Профиль успешно отредактирован')
            return HttpResponseRedirect(reverse('adminapp:admin_users_update', args=[user_id]))
        else:
            messages.warning(request, validate_min_length_errors)
    else:
        form = UserAdminProfileForm(instance=user)

    context = {
        'user': user,
        'form': form,
        'title': 'GeekShop - Редактирование пользователя',
        'copyright': 'Copyright © GeekShop 2024'
    }
    return render(request, 'adminapp/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_delete(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        user.is_active = False
        user.save()
        messages.success(request, 'Пользователь успешно удалён')
    return HttpResponseRedirect(reverse('adminapp:admin_users_read'))


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_read(request):
    context = {
        'product_categories': ProductCategory.objects.all(),
        'title': 'GeekShop - Категории',
        'copyright': 'Copyright © GeekShop 2024'
    }
    return render(request, 'adminapp/admin-categories-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_create(request):
    if request.method == 'POST':
        form = CategoriesAdminRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Категория успешно создана')
            return HttpResponseRedirect(reverse('adminapp:admin_categories_read'))
        else:
            messages.warning(request, form.errors)
    else:
        form = CategoriesAdminRegisterForm()

    context = {
        'form': form,
        'title': 'GeekShop - Создание категории',
        'copyright': 'Copyright © GeekShop 2024',
    }
    return render(request, 'adminapp/admin-categories-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_update(request, category_id):
    category = ProductCategory.objects.get(id=category_id)
    if request.method == 'POST':
        form = CategoriesAdminProfileForm(data=request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Категория успешно отредактирована')
            return HttpResponseRedirect(reverse('adminapp:admin_categories_update', args=[category_id]))
        else:
            messages.warning(request, form.errors)
    else:
        form = CategoriesAdminProfileForm(instance=category)

    context = {
        'category': category,
        'form': form,
        'title': 'GeekShop - Редактирование категории',
        'copyright': 'Copyright © GeekShop 2024'
    }
    return render(request, 'adminapp/admin-categories-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_delete(request, category_id):
    category = ProductCategory.objects.get(id=category_id)
    if request.method == 'POST':
        category.is_active = False
        category.save()
        messages.success(request, 'Категория успешно удалёна')
    return HttpResponseRedirect(reverse('adminapp:admin_categories_read'))


@user_passes_test(lambda u: u.is_superuser)
def admin_products_read(request):
    context = {
        'products': Product.objects.all(),
        'title': 'GeekShop - Продукты',
        'copyright': 'Copyright © GeekShop 2024'
    }
    return render(request, 'adminapp/admin-products-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_create(request):
    if request.method == 'POST':
        form = ProductsAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Продукт успешно создан')
            return HttpResponseRedirect(reverse('adminapp:admin_products_read'))
        else:
            messages.warning(request, form.errors)
    else:
        form = ProductsAdminRegisterForm()

    context = {
        'form': form,
        'title': 'GeekShop - Создание продукта',
        'copyright': 'Copyright © GeekShop 2024',
    }
    return render(request, 'adminapp/admin-products-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_update(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductAdminProfileForm(data=request.POST, instance=product, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Продукт успешно отредактирован')
            return HttpResponseRedirect(reverse('adminapp:admin_products_update', args=[product_id]))
        else:
            messages.warning(request, form.errors)
    else:
        form = ProductAdminProfileForm(instance=product)

    context = {
        'product': product,
        'form': form,
        'title': 'GeekShop - Редактирование продукта',
        'copyright': 'Copyright © GeekShop 2024'
    }
    return render(request, 'adminapp/admin-products-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_delete(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.is_active = False
        product.save()
        messages.success(request, 'Продукт успешно удалён')
    return HttpResponseRedirect(reverse('adminapp:admin_products_read'))
