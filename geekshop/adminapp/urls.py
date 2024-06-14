from django.urls import path
from adminapp.views import index, admin_users_read, admin_users_create, admin_users_update, admin_users_delete, \
    admin_categories_read, admin_categories_create, admin_categories_update, admin_categories_delete, \
    admin_products_read, admin_products_create, admin_products_update, admin_products_delete

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users-read/', admin_users_read, name='admin_users_read'),
    path('users-create/', admin_users_create, name='admin_users_create'),
    path('users-update/<int:user_id>', admin_users_update, name='admin_users_update'),
    path('users-delete/<int:user_id>', admin_users_delete, name='admin_users_delete'),
    path('categories-read/', admin_categories_read, name='admin_categories_read'),
    path('categories-create/', admin_categories_create, name='admin_categories_create'),
    path('categories-update/<int:category_id>', admin_categories_update, name='admin_categories_update'),
    path('categories-delete/<int:category_id>', admin_categories_delete, name='admin_categories_delete'),
    path('products-read/', admin_products_read, name='admin_products_read'),
    path('products-create/', admin_products_create, name='admin_products_create'),
    path('products-update/<int:product_id>', admin_products_update, name='admin_products_update'),
    path('products-delete/<int:product_id>', admin_products_delete, name='admin_products_delete')
]
